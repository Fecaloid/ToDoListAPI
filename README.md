### How to prepare project and run docker compose
1) Create .env file.
    ```
    cp .env_example .env
    ```
   If you want to use local python virtual env
    ```
    cp .env_local .env
    ```
2) Create and start containers
    ```
    docker-compose build
    docker-compose up -d
    ```
   
3) Run tests
    ```
   docker exec todolistapi_tdl_web_1 pytest
   ```
4) Read the docs
   ```
   http://127.0.0.1:8002/docs # docker venv
   http://127.0.0.1:8000/docs # local venv
   ```