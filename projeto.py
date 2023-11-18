import pandas as pd
import requests
import json
from tqdm import tqdm

#Definindo as cidades
cidades = ['Salvador','London','São Paulo','Fortaleza','New York']

#Getando o JSON e direcionando para listas
planilha = {
    "cidade":[],
    "temperatura":[],
    "sensacao_termica":[],
    "minima":[],
    "maxima":[]
}

print('EXTRAINDO DADOS...')
for cidade in tqdm(cidades,colour='green'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    dados = requests.get(url).json()
    planilha['cidade'].append(dados['name'])
    planilha['temperatura'].append(dados['main']['temp'])
    planilha['sensacao_termica'].append(dados['main']['feels_like'])
    planilha['minima'].append(dados['main']['temp_min'])
    planilha['maxima'].append(dados['main']['temp_max'])
    
    
df = pd.DataFrame(planilha)
#Gerando planilha em excel
df.to_excel('planilha.xlsx')