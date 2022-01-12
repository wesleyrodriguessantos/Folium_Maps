import folium

# Adição de ZOOM
m = folium.Map(location=[-16.6815233, -49.2531244],
               tiles='Stamen Terrain',
               zoom_start=12)

m.save("Ex3_Cores/mapa_Stamen_Terrain.html")
