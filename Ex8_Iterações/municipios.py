import pandas as pd
import folium

ler = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex8_Iterações\EXC\municipios.xlsx", engine='openpyxl')

m = folium.Map(location=[-14.356625, -50.343006],
               tiles='OpenStreetMap', zoom_start=5)


for index, linha in ler.iterrows():
    folium.Marker([linha["LATITUDE"], linha["LONGITUDE"]]).add_to(m)


m.save("Ex8_Iterações/municipios2.html")
