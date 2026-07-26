import urllib.request

try:
    #codigo para acessar o site com um user-agent, pois se tentar acessar sem isso ele pode perceber q e um "robo" e dar captcha 
    req = urllib.request.Request('https://pudim.com.br/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    response = urllib.request.urlopen(req)
    print("Tudo certo! O site foi acessado com sucesso.")
except urllib.error.URLError as e:
    print(f"Erro ao acessar o site: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")