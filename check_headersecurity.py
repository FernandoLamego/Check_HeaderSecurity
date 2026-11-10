import requests
import argparse
import pprint

parser = argparse.ArgumentParser(description='Verifica a segurança dos cabeçalhos HTTP de um site.')
parser.add_argument('url', type=str, help='URL do site a ser verificado')

args = parser.parse_args()

def requesicao(url):
    try:
        response = requests.get(f"https://api.securityheaders.com/?q={url}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return None

response = requesicao(args.url)
pprint.pprint(response['headers']) if response else print("Não foi possível obter os cabeçalhos de segurança.")