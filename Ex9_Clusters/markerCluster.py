import pandas as pd
import folium
from folium.plugins import MarkerCluster

ler = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex9_Clusters\locais.xlsx", engine='openpyxl')

m = folium.Map(location=[-14.441758, -48.9271955],
               tiles='OpenStreetMap', zoom_start=5)

cluster = MarkerCluster().add_to(m)

for index, linha in ler.iterrows():
    folium.Marker([linha["LAT"], linha["LONG"]],
                  popup='<b>'+linha["LOCALIDADE/UF_2"]+'</b>' + '<br>'+linha["DESCRICAO"], tooltip=linha["LOCALIDADE"],
                  icon=folium.Icon(
                      color=linha["COLOR"], icon=linha["ICON"], prefix='fa')).add_to(cluster)


cluster.save("Ex9_Clusters/markerclusterMaior.html")
