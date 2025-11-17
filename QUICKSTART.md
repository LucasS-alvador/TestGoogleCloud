# QUICK START GUIDE

## 1. Configurar `.env` (PRIMEIRO!)

```bash
# Edite o arquivo .env com:
GOOGLE_CLIENT_ID=seu_client_id_do_google
GOOGLE_CLIENT_SECRET=seu_client_secret_do_google
SECRET_KEY=chave_secreta_aleatoria
FLASK_ENV=development
```

## 2. Instalar Dependências

```bash
# Backend
pip install -r requirements.txt

# Frontend
cd flask-google-login-frontend
npm install
```

## 3. Iniciar Aplicação

### Terminal 1 - Backend
```bash
python app.py
# Acesse: http://localhost:5000
```

### Terminal 2 - Frontend
```bash
cd flask-google-login-frontend
npm run dev
# Acesse: http://localhost:3000
```

## 4. Testar

1. Abra: http://localhost:3000
2. Clique em "Login with Google"
3. Faça login com sua conta Google
4. Você será redirecionado para o dashboard

---

## Estrutura de Rotas

### Backend (Flask)

```
GET /                    - Página inicial
GET /login               - Inicia fluxo OAuth
GET /login/callback      - Callback do Google
GET /protected           - Rota protegida (requer JWT)
GET /logout              - Logout
```

### Frontend (Next.js)

```
GET /                           - Página de login
GET /auth/callback?token=xxx    - Callback do OAuth
GET /dashboard                  - Dashboard (protegido)
```

---

## Troubleshooting

| Erro | Solução |
|------|---------|
| ModuleNotFoundError | `pip install -r requirements.txt` |
| CORS error | Confira `CORS(app, origins=[...])` em app.py |
| Invalid Client ID | Edite `.env` com credenciais corretas |
| Redirect URI mismatch | Configure em https://console.cloud.google.com/ |
| Token not saved | Verifique localStorage no navegador (F12) |

---

## Arquivos Principais

- `app.py` - Backend Flask
- `requirements.txt` - Dependências Python
- `.env` - Variáveis de ambiente (EDITAR!)
- `flask-google-login-frontend/pages/index.tsx` - Login
- `flask-google-login-frontend/pages/dashboard.jsx` - Dashboard

---

**Leia `README.md` para documentação completa!**
