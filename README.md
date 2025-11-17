# Google OAuth Login - Flask + Next.js

Sistema completo de autenticação com Google OAuth usando Flask como backend e Next.js como frontend.

## 📋 Requisitos

- Python 3.8+
- Node.js 16+
- Conta Google (para obter credenciais OAuth)

## 🚀 Instalação Rápida

### 1. Clonar/Baixar o Projeto
```bash
cd c:\Users\lucas\3D Objects\progs\web\login
```

### 2. Criar e Configurar `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_CLIENT_ID=seu_client_id_aqui
GOOGLE_CLIENT_SECRET=seu_client_secret_aqui
SECRET_KEY=sua_chave_secreta_aleatoria
FLASK_ENV=development
```

**Como obter as credenciais:**

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto
3. Ative "Google+ API"
4. Vá para "Credenciais" → "Criar Credenciais" → "ID do cliente OAuth 2.0"
5. Selecione "Aplicação da Web"
6. Configure os URIs:
   - **JavaScript origins**: `http://localhost:3000`, `http://localhost:5000`
   - **Authorized redirect URIs**: `http://localhost:5000/login/callback`
7. Copie o **Client ID** e **Client Secret**

### 3. Instalar Dependências

**Backend (Python):**
```bash
pip install -r requirements.txt
```

**Frontend (Node.js):**
```bash
cd flask-google-login-frontend
npm install
```

## ▶️ Executar a Aplicação

### Terminal 1 - Backend
```bash
python app.py
```
Backend disponível em: `http://localhost:5000`

### Terminal 2 - Frontend
```bash
cd flask-google-login-frontend
npm run dev
```
Frontend disponível em: `http://localhost:3000`

## 🔄 Fluxo de Autenticação

```
┌─────────────────────────────────────────────────────┐
│  1. User acessa http://localhost:3000               │
│     e clica "Login with Google"                      │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  2. Frontend redireciona para                        │
│     http://localhost:5000/login                      │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  3. Flask redireciona para Google OAuth             │
│     User faz login com conta Google                 │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  4. Google redireciona de volta para                │
│     http://localhost:5000/login/callback            │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  5. Flask cria JWT e redireciona para               │
│     http://localhost:3000/auth/callback?token=xxx   │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  6. Frontend salva token em localStorage            │
│     e redireciona para /dashboard                    │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│  7. Dashboard exibe dados do usuário                │
│     (obtidos via /protected com token JWT)          │
└─────────────────────────────────────────────────────┘
```

## 📁 Estrutura do Projeto

```
login/
├── app.py                          # Backend Flask
├── requirements.txt                # Dependências Python
├── .env                           # Variáveis de ambiente (criar)
├── SETUP_GUIDE.md                 # Guia detalhado
├── start.bat                       # Script para iniciar
│
└── flask-google-login-frontend/   # Frontend Next.js
    ├── package.json
    ├── tsconfig.json
    ├── pages/
    │   ├── _app.tsx
    │   ├── _document.tsx
    │   ├── index.tsx               # Página de login
    │   ├── dashboard.jsx           # Dashboard (protegido)
    │   ├── api/
    │   │   └── hello.ts
    │   └── auth/
    │       └── callback.jsx        # Callback do OAuth
    ├── public/
    ├── styles/
    │   └── globals.css
    └── .next/                      # Build output
```

## 🔧 Rotas da API

### Públicas
- `GET /` - Página inicial (HTML)
- `GET /login` - Inicia o fluxo de autenticação Google
- `GET /login/callback` - Callback do Google OAuth

### Protegidas (requerem JWT token)
- `GET /protected` - Retorna dados do usuário autenticado
  - Header: `Authorization: Bearer <jwt_token>`

### Gerenciamento
- `GET /logout` - Faz logout (limpa session)

## 📊 Dados do JWT

O token JWT contem:
```json
{
  "sub": "email@example.com",
  "name": "Nome do Usuário",
  "email": "email@example.com",
  "picture": "https://...",
  "exp": 1234567890,
  "iat": 1234567800
}
```

## ❌ Troubleshooting

### Erro: "No module named 'flask'"
```bash
pip install flask flask-cors authlib pyjwt python-dotenv
```

### Erro: "CORS error"
- Verifique se `http://localhost:3000` está na configuração CORS do backend
- Verifique se as URLs autorizadas estão corretas no Google Console

### Erro: "Invalid Client ID"
- Confira se `GOOGLE_CLIENT_ID` está correto no `.env`
- Regenere as credenciais no Google Console se necessário

### Erro: "Redirect URI mismatch"
- O `redirect_uri` deve ser exatamente `http://localhost:5000/login/callback`
- Configure corretamente no Google Console

### Token não é salvo no localStorage
- Verifique se o navegador permite localStorage
- Verifique o console do navegador para erros

### Página dashboard não carrega dados
- Certifique-se que o backend está rodando
- Verifique se o token está sendo enviado corretamente no header `Authorization`

## 🔐 Segurança

- Os tokens JWT expiram em 1 hora
- A chave secreta deve ser forte em produção (altere em `SECRET_KEY`)
- Nunca commite o arquivo `.env` no git
- Use HTTPS em produção

## 📝 Próximos Passos

1. Adicionar refresh tokens
2. Salvar dados do usuário em banco de dados
3. Implementar logout do lado do servidor
4. Adicionar proteção contra CSRF
5. Usar HTTPS em desenvolvimento com certificados auto-assinados

## 📚 Referências

- [Authlib Documentation](https://authlib.org/)
- [Google OAuth 2.0](https://developers.google.com/identity/protocols/oauth2)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Next.js Documentation](https://nextjs.org/docs)

## 📄 Licença

MIT

## 👨‍💻 Autor

Desenvolvido como exemplo de autenticação OAuth com Flask e Next.js.

---

**Dúvidas?** Consulte o arquivo `SETUP_GUIDE.md` para instruções mais detalhadas.
