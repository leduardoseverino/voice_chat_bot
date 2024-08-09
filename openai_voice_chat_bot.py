from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from audio_recorder_streamlit import audio_recorder
from openai import OpenAI
import streamlit as st
import os

st.set_page_config(page_title="OpenAI Voice & Chat Bot", page_icon="🎙️")
st.title("OpenAI Voice & Chat Bot 🎙️")

def llm_selector():
    models=["gpt-4o-mini","gpt-4o", "gpt-3.5-turbo" ]
    with st.sidebar:
        return st.selectbox("Model", models)

# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
if len(msgs.messages) == 0:
    msgs.add_ai_message("How can I help you?")

# Get an OpenAI API Key before continuing
if "openai_api_key" in st.secrets:
    openai_api_key = st.secrets.openai_api_key
else:
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Enter an OpenAI API Key to continue")
    st.stop()

# Set up the LangChain, passing in Message History

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI chatbot having a conversation with a human."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

chain = prompt | ChatOpenAI(api_key=openai_api_key, model=llm_selector())
chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,
    input_messages_key="question",
    history_messages_key="history",
)

client = OpenAI(api_key=openai_api_key)

# Speech to text
def speech_to_text(audio_data):
    transcript = ''
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript

# Text to speech
def text_to_speech(input_text):
    speech_file_path = f"temp_audio_play.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input=input_text,
    ) as response:
        response.stream_to_file(speech_file_path)

    return speech_file_path


# Play audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        audio_bytes = f.read()

    st.audio(audio_bytes, format="audio/mpeg", autoplay=True)

# Get LLM response
def get_llm_response(input: str) -> str:

    # Note: new messages are saved to history automatically by Langchain during run
    config = {"configurable": {"session_id": "any"}}
    response = chain_with_history.invoke({"question": input}, config)

    return response

audio_bytes = None

# Render current messages from StreamlitChatMessageHistory
for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

with st.sidebar:
    audio_bytes = audio_recorder(pause_threshold=1.0, sample_rate=16_000)

# If user inputs a new prompt, generate and draw a new response
if prompt := st.chat_input():
    st.chat_message("human").write(prompt)
    msgs.add_user_message(prompt)
    audio_bytes = None

# If audio bytes are available, transcribe and add to chat history
if audio_bytes is not None:
    # Write the audio bytes to a file
    with st.spinner("Transcribing..."):
        file_path = f"temp_audio.mp3"
        with open(file_path, "wb") as f:
            f.write(audio_bytes)

        # Reset the buffer position to the beginning
        transcript = speech_to_text(file_path)
        if transcript:
            st.chat_message("human").write(transcript)
            msgs.add_user_message(transcript)

# If last message is not from the AI, generate a new response
if st.session_state.langchain_messages[-1].type != "ai":
    with st.chat_message("ai"):
        with st.spinner("Thinking🤔..."):
            response = get_llm_response(st.session_state.langchain_messages[-1].content)

        st.write(response.content)
        with st.spinner("Generating audio response..."):
            audio_file = text_to_speech(response.content)
            autoplay_audio(audio_file)
        
        os.remove(audio_file)
