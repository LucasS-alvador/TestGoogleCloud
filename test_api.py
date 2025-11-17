#!/usr/bin/env python3
"""
Script para testar a API Flask localmente
"""

import requests
import json
from requests.auth import HTTPBasicAuth

# URL base do servidor Flask
BASE_URL = "http://localhost:5000"

def test_index():
    """Testa a rota raiz"""
    print("\n[TEST 1] GET /")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
    except Exception as e:
        print(f"Erro: {e}")

def test_protected_without_token():
    """Testa rota protegida SEM token"""
    print("\n[TEST 2] GET /protected (sem token)")
    try:
        response = requests.get(f"{BASE_URL}/protected")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro: {e}")

def test_protected_with_invalid_token():
    """Testa rota protegida com token inválido"""
    print("\n[TEST 3] GET /protected (com token inválido)")
    headers = {
        "Authorization": "Bearer invalid_token_12345"
    }
    try:
        response = requests.get(f"{BASE_URL}/protected", headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Erro: {e}")

def test_cors():
    """Testa CORS headers"""
    print("\n[TEST 4] CORS Headers")
    headers = {
        "Origin": "http://localhost:3000"
    }
    try:
        response = requests.options(f"{BASE_URL}/", headers=headers)
        print(f"Status: {response.status_code}")
        cors_header = response.headers.get('Access-Control-Allow-Origin')
        print(f"Access-Control-Allow-Origin: {cors_header}")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    print("=" * 50)
    print("  Testes da API Flask - Google OAuth")
    print("=" * 50)
    
    print("\nCertifique-se que o servidor Flask está rodando em http://localhost:5000")
    print("Execute: python app.py")
    
    input("\nPressione ENTER para iniciar os testes...")
    
    test_index()
    test_protected_without_token()
    test_protected_with_invalid_token()
    test_cors()
    
    print("\n" + "=" * 50)
    print("Testes concluídos!")
    print("=" * 50)
    print("\nNota: Para testar o fluxo completo de autenticação:")
    print("1. Abra http://localhost:3000")
    print("2. Clique em 'Login with Google'")
    print("3. Faça login com sua conta Google")
    print("4. Você será redirecionado para o dashboard")

if __name__ == "__main__":
    main()
