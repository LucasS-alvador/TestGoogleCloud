@echo off
REM Script para iniciar a aplicacao

echo ========================================
echo   Google OAuth Login Setup
echo ========================================
echo.

REM Check if .env file exists
if not exist ".env" (
    echo ERRO: Arquivo .env nao encontrado!
    echo.
    echo Por favor, siga os passos:
    echo 1. Crie um arquivo .env na raiz do projeto
    echo 2. Adicione suas credenciais do Google:
    echo    GOOGLE_CLIENT_ID=seu_id_aqui
    echo    GOOGLE_CLIENT_SECRET=seu_secret_aqui
    echo    SECRET_KEY=sua_chave_secreta
    echo.
    pause
    exit /b 1
)

REM Check if env variables are set
for /f "tokens=*" %%A in ('findstr /I "GOOGLE_CLIENT_ID" .env') do set CLIENT_ID=%%A
if "%CLIENT_ID:YOUR_GOOGLE_CLIENT_ID_HERE=%"=="%CLIENT_ID%" (
    echo ERRO: Credenciais do Google nao configuradas!
    echo.
    echo Edite o arquivo .env e adicione:
    echo - GOOGLE_CLIENT_ID
    echo - GOOGLE_CLIENT_SECRET
    echo.
    pause
    exit /b 1
)

echo Iniciando aplicacao...
echo.
echo [1] Backend Flask (http://localhost:5000)
echo [2] Frontend Next.js (http://localhost:3000)
echo.
echo Abra dois terminais e execute:
echo.
echo Terminal 1:
echo   python app.py
echo.
echo Terminal 2:
echo   cd flask-google-login-frontend
echo   npm run dev
echo.
echo Depois acesse: http://localhost:3000
echo.
pause
