# Voice Chat Bot
A repository for voice chat bots 

## Setup 
#### Install the requirements.
```bash
pip install -r requirements.txt
```
#### Setup Ollama server for `llama_voice_chat_bot`
First, follow these [instructions](https://github.com/ollama/ollama) to set up and run a local Ollama instance:

- Download and install Ollama onto the available supported platforms (including Windows Subsystem for Linux)
  - Fetch available LLM model via `ollama pull <name-of-model>` 
  - e.g., `ollama pull llama3.1`
- This will download the default tagged version of the model. Typically, the default points to the latest, smallest sized-parameter model.
- To view all pulled models, use `ollama list`
- To chat directly with a model from the command line, use `ollama run <name-of-model>`
- Find the running model with `ollama ps`
- Run `ollama help` in the terminal to see available commands too.

## OpenAI Voice Chat Bot
A Voice & Chat Bot 🎙️ backed by OpenAI, Streamlit and LangChain

Find the story in Medium [An OpenAI Voice & Chat Bot](https://medium.com/@yuxiaojian/an-openai-voice-chat-bot-b4cbe553f3ca)

### Setup OpenAI API Key
1. You need to have an OpenAI API key. You can  get it from [here](https://platform.openai.com/account/api-keys). Two ways to add your API key to the project:
- add it to the `.streamlit/secrets.toml` file of the current directory
```bash
openai_api_key = "your_api_key"
```
- input it in the browser

2. Run the app.
```bash
streamlit run openai_voice_chat_bot.py
```

<p align="center">
  <img src="assets/media/openai_voice_chat_bot.gif">
</p>


## Llama Voice Chat Bot
Use the same framework as `openai_voice_chat_bot` but with different engines:
- LLM: Ollama 3.1
- STT: Whisper
- TTS: Google TTS

#### Run the app.
```bash
streamlit run llama_voice_chat_bot.py
```

## Run remotely
The audio recording works with HTTPS (not HTTP). You will need a certificate and key to run the streamlit app in HTTPS. 

```bash
cat  ~/.streamlit/config.toml
...
[server]
port = 8443
sslCertFile = "<path to your certificate>"
sslKeyFile = "<path to your key>"
...
```

For testing purposes, you can use a self-signed certificate.
```bash
openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -subj "/CN=streamlit" -keyout streamlit.key -out streamlit.crt

```


## Credits
- [llm-voice-bot](https://github.com/iamaziz/llm-voice-bot)
- [openai-conversational-voice-chatbot](https://github.com/sulaiman-shamasna/openai-conversational-voice-chatbot)
- [local-talking-llm](https://github.com/vndee/local-talking-llm.git)

