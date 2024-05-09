import os
import requests
from dotenv import load_dotenv

load_dotenv()

proxycheck_url = os.getenv("PROXYCHECK_URL")

def get_proxy_data(ip):
    url = f"{proxycheck_url}{ip}?vpn=1&asn=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter dados do proxy: {response.status_code}")
        return None

def main():
    ip = input("Digite o IP: ")
    proxy_data = get_proxy_data(ip)
    if proxy_data:
        proxy_status = proxy_data.get("status")
        if proxy_status == "ok":
            proxy_info = proxy_data.get(ip)
            if proxy_info:
                proxy_status = proxy_info.get("proxy")
                proxy_type = proxy_info.get("type")
                if proxy_status == "yes":
                    print("É um proxy.")
                    print(f"Tipo de proxy: {proxy_type}")
                else:
                    print("Este não é um proxy.")
            else:
                print("IP não encontrado na resposta.")
        else:
            print("Status da resposta não é 'ok'.")
    else:
        print("Não foi possível obter os dados do proxy.")

if __name__ == "__main__":
    main()
