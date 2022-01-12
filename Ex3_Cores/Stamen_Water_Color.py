import folium

# Adição de ZOOM
m = folium.Map(location=[-16.6815233, -49.2531244],
               tiles='Stamen Water Color',
               zoom_start=12)

m.save("Ex3_Cores/Stamen_Water_Color.html")
