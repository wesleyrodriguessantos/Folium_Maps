import pandas as pd
import folium

ler = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex8_Iterações\EXC\locais.xlsx", engine='openpyxl')

m = folium.Map(location=[-14.441758, -48.9271955],
               tiles='OpenStreetMap', zoom_start=8)


for index, linha in ler.iterrows():
    folium.RegularPolygonMarker([linha["LAT"], linha["LONG"]],
                                popup='<b>'+linha["LOCALIDADE/UF_2"] +
                                '</b>' + '<br>'+linha["DESCRICAO"],
                                radius=15,
                                number_of_sides=5,
                                tooltip=linha["LOCALIDADE"],
                                color=linha["COLOR"],
                                fill_color=linha["COLOR"]).add_to(m)


m.save("Ex8_Iterações/Polygon.html")
