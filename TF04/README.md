# Projeto de Load Balancer 

Estrutura do projeto:

- `README.md`
- `docker-compose.yml`
- `nginx/`
  - `nginx.conf`
  - `ssl/`
    - `cert.pem`
    - `key.pem`
  - `conf.d/`
    - `load-balancer.conf`
    - `ssl.conf`
- `frontend/`
  - `Dockerfile`
  - `index.html`
  - `produtos.html`
  - `carrinho.html`
  - `css/style.css`
- `backend/`
  - `Dockerfile`
  - `app.py`
  - `requirements.txt`
  - `config.py`
- `admin/`
  - `Dockerfile`
  - `dashboard.html`
  - `css/admin.css`
- `docs/`
  - `nginx-config.md`
  - `load-balancing.md`

## Uso

1. Construir e subir os servi�os:
   ```bash
   docker-compose up --build
   ```

2. Adicionar no `/etc/hosts`:
   ```text
   127.0.0.1 api.localhost
   127.0.0.1 admin.localhost
   127.0.0.1 frontend.localhost
   ```

3. Acessar via HTTPS:
   - `https://api.localhost`
   - `https://admin.localhost`
   - `https://frontend.localhost`
