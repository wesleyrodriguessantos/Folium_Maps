import pandas as pd
import folium

ler = pd.read_excel(
    r"C:\Users\Wesley\OneDrive\Documents\Folium\municipios.xlsx", engine='openpyxl')

tabela = ler.set_index("UF")
ufs = list(set(tabela.index.values))

tabelas = {}
mapas = {}

for uf in ufs:
    tabelas['base_{}'.format(uf)] = ler[ler.UF == uf]


for estado in tabela.keys():
    mapas['mapa_{}'.format(estado)] = folium.Map(
        location=[-14.235004, -51.95528], zoom_start=5)

    for item in tabelas[estado].iterrows():
        lat = item[1]["LATITUDE"]
        longi = item[1]["LONGITUDE"]
        descricao = item[1]["NOME_MUNICIPIO"]
        folium.Marker((lat, longi), popup=descricao).add_to(
            mapas['mapa_{}'.format(estado)])

    mapas['mapa_{}'.format(estado)].save(
        'Ex8_Iterações/Estados/{}.html'.format(estado))
