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


# Wan 2.1

This is required CUDA Toolkit 
```shell
conda install -c conda-forge cudatoolkit-dev -y
```

After your setup CUDA and restart, you need to set 
```shell
export PATH=/usr/local/cuda-12.8/bin${PATH:+:${PATH}}
```

nvtop and nvidia-smi are tools for GPU monitoring.


# Setup gcc/g++ alternatives for compiling cuda-samples

For CUDA 12.8, we need gcc/g++ 11

```shell
sudo apt install  g++-11 gcc-11
# update alternatives
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100 # default: the last number is priority. Higher priority is higher value
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100 # default
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 50

# set a specific version
sudo update-alternatives --config gcc  
sudo update-alternatives --config g++
```
### Fix for cmake pointing to wrong gcc/g++ version 
```shell
# Now even after doing this cmake was picking wrong gcc version as it was pointing to /usr/bin/c++ which was using system version of 14.2. So we override it.
cmake -DCMAKE_C_COMPILER=/usr/bin/gcc-11 -DCMAKE_CXX_COMPILER=/usr/bin/g++-11 .
```

