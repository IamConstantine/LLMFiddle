# Index of Tools being used


#### LLM Observability
    
1. Lunary
   
    - Easy to setup
    - Async mode only
    - The code requires a pip dependency and a Lunary Key. You can then setup the monitor in the code with one line
    ```python
    monitor(client)
   ``` 
   - Self-Hosting is supported
   - LLM caching - Reduce latency and save costs on LLM calls by caching responses on the edge
     - Saves Money
     - Low Latency and reduce load on backend
     - Cache seeding- isolate cache by seed
   - Apache 2.0
   - Support for GDPR compliance where users can opt out of usage monitoring.
2. Helicone
    
    - Helicone seems to be better than Lunary in terms of Features 
    - Supports Async and Proxy mode
      - Async sets up an async monitor thread in background and lets you do your normal calls to LLM endpoint
      - Proxy sits in between client and LLM provider
    - Helicone has a better request trace interface and its easier to setup.This one just needs a Helicone rest endpoint with an API key
    - MIT License ie Free to copy and modify. This doesn't respect Patent rights but allows for widespread adoption.
    - Supports more LLM providers 
    - Similar Caching features as Lunary
    - Can omit logs using custom headers. It's useful for removing traces for sensitive prompts and responses


#### Vector DBs

1. SingleStore - https://portal.singlestore.com
    
    - has a Free tier to play around

#### Embedding Models

1. Voyage - https://www.voyageai.com/
   
   - This one seems to provide a better text embedding model
   - The Free usage tier has higher limits compared to OpenAi embedding models

