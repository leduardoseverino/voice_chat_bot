# Documentação Técnica dos Arquivos

## 📁 Estrutura Geral

A estrutura de diretórios do projeto Retrofit é organizada da seguinte maneira:

```
retrofit/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/
│   │   │   │       └── example/
│   │   │   │           └── retrofit/
│   │   │   │               ├── ApiService.java
│   │   │   │               ├── RetrofitClient.java
│   │   │   │               └── Main.java
│   │   │   ├── res/
│   │   │   └── AndroidManifest.xml
│   │   └── test/
│   │       └── java/
│   │           └── com/
│   │               └── example/
│   │                   └── retrofit/
│   │                       └── ExampleUnitTest.java
│   ├── build.gradle
├── build.gradle
└── settings.gradle
```

## 🔧 Arquivos Principais

### `build.gradle` (Groovy)

**Propósito:** Este arquivo define as configurações de build do projeto, incluindo dependências e plugins.

**Localização:** `retrofit/build.gradle`

#### 📋 Funcionalidades:
- Define o plugin Gradle.
- Configura as dependências do projeto.
- Define tarefas de build.

### `settings.gradle` (Groovy)

**Propósito:** Este arquivo configura os módulos do projeto e suas dependências.

**Localização:** `retrofit/settings.gradle`

#### 📋 Funcionalidades:
- Inclui os módulos do projeto.
- Configura as dependências entre módulos.

### `app/build.gradle` (Groovy)

**Propósito:** Este arquivo define as configurações de build específicas para o módulo `app`.

**Localização:** `retrofit/app/build.gradle`

#### 📋 Funcionalidades:
- Define o plugin Android.
- Configura as dependências do módulo `app`.
- Define tarefas de build específicas.

### `ApiService.java` (Java)

**Propósito:** Esta interface define os endpoints da API que serão usados pelo Retrofit.

**Localização:** `retrofit/app/src/main/java/com/example/retrofit/ApiService.java`

#### 📋 Funcionalidades:
- Define métodos para chamadas de API usando anotações do Retrofit.

#### 🔧 Funções Principais:
- `getUsers()`: Método que define uma chamada GET para o endpoint `/users`.

```java
import retrofit2.Call;
import retrofit2.http.GET;

public interface ApiService {
    @GET("users")
    Call<List<User>> getUsers();
}
```

### `RetrofitClient.java` (Java)

**Propósito:** Esta classe configura e fornece uma instância do cliente Retrofit.

**Localização:** `retrofit/app/src/main/java/com/example/retrofit/RetrofitClient.java`

#### 📋 Funcionalidades:
- Configura a base URL da API.
- Adiciona conversores de resposta.

#### 🔧 Funções Principais:
- `getRetrofitInstance()`: Método que retorna uma instância configurada do cliente Retrofit.

```java
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClient {
    private static Retrofit retrofit = null;

    public static Retrofit getRetrofitInstance() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl("https://api.example.com/")
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
        }
        return retrofit;
    }
}
```

### `Main.java` (Java)

**Propósito:** Este arquivo contém o ponto de entrada principal do aplicativo, onde são feitas chamadas à API usando Retrofit.

**Localização:** `retrofit/app/src/main/java/com/example/retrofit/Main.java`

#### 📋 Funcionalidades:
- Cria uma instância da interface `ApiService`.
- Faz uma chamada assíncrona para o endpoint `/users`.

#### 🔧 Funções Principais:
- `main(String[] args)`: Método principal que inicia a aplicação e faz a chamada à API.

```java
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Main {
    public static void main(String[] args) {
        ApiService apiService = RetrofitClient.getRetrofitInstance().create(ApiService.class);
        Call<List<User>> call = apiService.getUsers();

        call.enqueue(new Callback<List<User>>() {
            @Override
            public void onResponse(Call<List<User>> call, Response<List<User>> response) {
                if (response.isSuccessful()) {
                    List<User> users = response.body();
                    // Processar a lista de usuários
                }
            }

            @Override
            public void onFailure(Call<List<User>> call, Throwable t) {
                // Tratar erro
            }
        });
    }
}
```

### `ExampleUnitTest.java` (Java)

**Propósito:** Este arquivo contém testes unitários para o módulo `app`.

**Localização:** `retrofit/app/src/test/java/com/example/retrofit/ExampleUnitTest.java`

#### 📋 Funcionalidades:
- Define testes unitários para verificar a funcionalidade do aplicativo.

```java
import org.junit.Test;

public class ExampleUnitTest {
    @Test
    public void addition_isCorrect() {
        assertEquals(4, 2 + 2);
    }
}
```

### `AndroidManifest.xml` (XML)

**Propósito:** Este arquivo define as configurações do manifesto para o aplicativo Android.

**Localização:** `retrofit/app/src/main/AndroidManifest.xml`

#### 📋 Funcionalidades:
- Define componentes e permissões necessárias para o aplicativo.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.retrofit">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

## 📝 Observações

- **Versões Compatíveis**: Certifique-se de que as versões do Retrofit e das bibliotecas relacionadas são compatíveis entre si.
- **Configuração de Proxy**: Se você estiver atrás de um proxy, configure o Gradle para usar o proxy adequado.
- **Documentação Adicional**: Consulte a [documentação oficial do Retrofit](https://square.github.io/retrofit/) para mais detalhes e exemplos avançados.

---

Este guia deve permitir que qualquer desenvolvedor entenda a estrutura dos arquivos do projeto Retrofit e como eles interagem entre si. Se tiver dúvidas ou encontrar problemas, sinta-se à vontade para abrir uma issue no repositório do GitHub.