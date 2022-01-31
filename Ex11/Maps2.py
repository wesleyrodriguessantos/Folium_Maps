import pandas as pd
import folium
from folium.plugins import MarkerCluster

ler = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex11\municipiosofc.xlsx", engine='openpyxl')

tabela = ler.set_index("UF")
ufs = list(set(tabela.index.values))

# print(ufs)

locais = {}
municipios = {}

for uf in ufs:
    locais['{}'.format(uf)] = ler[ler.UF == uf][[
        "LATITUDE", "LONGITUDE"]].values.tolist()

for mun in ufs:
    print(mun)
    municipios['{}'.format(mun)] = ler[ler.NOME_MUNICIPIO == mun][[
        "NOME_MUNICIPIO"]].values.tolist()

mapa = folium.Map(location=[-14.235004, -51.95528], zoom_start=4)

# for index, mun in ler.iterrows():
#     folium.Marker(popup='{}'.format(mun["NOME_MUNICIPIO"])).add_to(mapa)

for estado in locais.keys():
    MarkerCluster(locais['{}'.format(estado)],
                  name=estado, popups=locais['{}'.format(estado)]).add_to(mapa)

# for muni in municipios.keys():
#     folium.Popup(municipios['{}'.format(muni)]).add_to(mapa)

folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Stamen Toner').add_to(mapa)
folium.TileLayer('cartodbpositron').add_to(mapa)
folium.TileLayer('cartodbdark_matter').add_to(mapa)
folium.LayerControl().add_to(mapa)

mapa.save('Ex11/Brasil_3.html')
