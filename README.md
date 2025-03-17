# Open WebUI and LiteLLM Proxy integration

### Setup open webUI

1. Install open-webui
```shell
pip install openweb-ui
```
2. Start the server
```shell
open-webui serve
```

Open WebUI only support OpenAI and Ollama out of the box. We can make it support other providers by using a AI gateway 

### Setup LLMLite proxy

1. Clone repo
```shell
# Get the code
git clone https://github.com/BerriAI/litellm

# Go to folder
cd litellm
```

2. Create .env file
```text
LITELLM_MASTER_KEY="sk-1234"
LITELLM_SALT_KEY="your_random_salt_key"
PROXY_ADMIN_ID=admin
```

3. Start server
```shell
docker-compose up -d
```

4. Create admin user
```shell
curl --location 'http://localhost:4000/user/new' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data-raw '{"user_email": "admin@example.com", "user_id": "admin"}'
```
This step is not in official README and the bug is tracked [here](https://github.com/BerriAI/litellm/issues/9243) 

1. Once you login LiteLLM using Master key and admin user, you can add models
2. Create a virtual key for the required models and copy the key
3. Go to Open WebUI and replace OpenAI key with the new virtual key
4. You are set and can start interacting with the LLM models on chat window