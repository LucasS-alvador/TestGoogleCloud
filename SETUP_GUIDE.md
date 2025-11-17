# Guia de Configuração - Google OAuth

## 1. Obter Credenciais do Google

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto (ou selecione um existente)
3. Ative a API "Google+ API"
4. Vá para "Credenciais" > "Criar Credenciais" > "ID do cliente OAuth 2.0"
5. Selecione "Aplicação da Web"
6. Configure os URIs autorizados:
   - **JavaScript origins:** `http://localhost:3000`, `http://localhost:5000`
   - **Authorized redirect URIs:** `http://localhost:5000/login/callback`

7. Copie o **Client ID** e **Client Secret**

## 2. Configurar Variáveis de Ambiente

Edite o arquivo `.env` na raiz do projeto:

```
GOOGLE_CLIENT_ID=seu_client_id_aqui
GOOGLE_CLIENT_SECRET=seu_client_secret_aqui
SECRET_KEY=sua_chave_secreta_aleatoria
FLASK_ENV=development
```

## 3. Iniciar a Aplicação

### Terminal 1 - Backend Flask:
```bash
cd c:\Users\lucas\3D Objects\progs\web\login
python app.py
```

### Terminal 2 - Frontend Next.js:
```bash
cd c:\Users\lucas\3D Objects\progs\web\login\flask-google-login-frontend
npm run dev
```

## 4. Testar o Fluxo

1. Abra http://localhost:3000
2. Clique em "Login with Google"
3. Faça login com sua conta Google
4. Você será redirecionado para http://localhost:3000/auth/callback
5. O token JWT será salvo em `localStorage`
6. Você será redirecionado para http://localhost:3000/dashboard

## Estrutura do Fluxo

```
1. User clica em "Login with Google" (http://localhost:3000)
   ↓
2. Frontend redireciona para http://localhost:5000/login
   ↓
3. Flask redireciona para Google OAuth
   ↓
4. User faz login no Google
   ↓
5. Google redireciona de volta para http://localhost:5000/login/callback
   ↓
6. Flask cria JWT e redireciona para http://localhost:3000/auth/callback?token=xxx
   ↓
7. Frontend salva token em localStorage
   ↓
8. Frontend redireciona para http://localhost:3000/dashboard
```

## Troubleshooting

### Erro: "No module named 'flask'"
```bash
pip install flask flask-cors authlib pyjwt python-dotenv
```

### Erro: "CORS error"
Verifique se as origens estão corretamente configuradas no backend.

### Erro: "Invalid Client ID"
- Verifique se o GOOGLE_CLIENT_ID está correto no `.env`
- Certifique-se de que as URLs autorizadas estão configuradas no Google Console

### Erro: "Redirect URI mismatch"
O `redirect_uri` no callback deve ser exatamente `http://localhost:5000/login/callback`
