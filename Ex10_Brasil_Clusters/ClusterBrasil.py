import pandas as pd
import folium
from folium.plugins import FastMarkerCluster

municipios = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex10_Brasil_Clusters\municipios.xlsx", engine='openpyxl')
estados = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex10_Brasil_Clusters\estados.xlsx", engine='openpyxl')

juncao = pd.merge(municipios, estados)
tabela = juncao.set_index("UF")

ufs = list(set(tabela.index.values))
# print(ufs)

mapas = {}
locais = {}

for uf in ufs:
    locais['local_{}'.format(uf)] = municipios[municipios.UF == uf][[
        "LATITUDE", "LONGITUDE"]].values.tolist()

mapa = folium.Map(location=[-14.441758, -48.9271955],
                  tiles='OpenStreetMap', zoom_start=4)

for estado in locais.keys():
    print(estado)
    FastMarkerCluster(data=locais['{}'.format(estado)]).add_to(mapa)

mapa.save('Ex10_Brasil_Clusters/mapas/Brasil.html')
