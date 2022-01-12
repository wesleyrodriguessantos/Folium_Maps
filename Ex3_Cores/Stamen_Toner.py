import folium

# Adição de ZOOM
m = folium.Map(location=[-16.6719857, -49.3049661],
               tiles='Stamen Toner',
               zoom_start=12)

m.save("Ex3_Cores/mapa_Stamen.html")
