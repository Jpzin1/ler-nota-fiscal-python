import os # serve para verificar se o arquivo existe
import csv
import requests

# Função para ler as notas fiscais usando uma lista de arquivos CSV
def ler_notas_fiscais(arquivos_csv):
    notas_fiscais = []
    for arquivo_csv in arquivos_csv:
        print(f"Verificando o arquivo: {arquivo_csv}")
        if not os.path.isfile(arquivo_csv):
            print(f"Arquivo não encontrado: {arquivo_csv}")
            continue
        try:
            with open(arquivo_csv, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    notas_fiscais.append(row)
        except PermissionError:
            print(f"Erro de permissão ao tentar abrir o arquivo: {arquivo_csv}")
    return notas_fiscais

# Função para enviar as notas fiscais para o site (no caso preciso achar a API do site, enquanto isso estou usando um jsonplaceholder como teste)
def enviar_notas_fiscais(notas_fiscais, url):
    for nota in notas_fiscais:
        response = requests.post(url, json=nota)
        if response.status_code == 201:
            print(f"Nota fiscal enviada com sucesso: {nota}")
        else:
            print(f"Falha ao enviar nota fiscal: {nota}")

# Exemplo de uso (usando jsonplaceholder como teste)
arquivos_csv = [
    "c:/Users/joaoj/OneDrive/Área de Trabalho/ler-nota-fiscal-python/notas_fiscais.csv",
    "c:/Users/joaoj/OneDrive/Área de Trabalho/ler-nota-fiscal-python/notas_fiscais1.csv"
]  # lista de caminhos completos para os arquivos CSV (aqui posso usar varios csv como teste/exemplo...)
notas_fiscais = ler_notas_fiscais(arquivos_csv)
url = 'https://jsonplaceholder.typicode.com/posts'  # endpoint de teste
enviar_notas_fiscais(notas_fiscais, url)