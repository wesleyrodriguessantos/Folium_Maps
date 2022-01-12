import folium


m2 = folium.Map(width=600, height=600, location=[-16.6815233, -49.2531244])

folium.TileLayer('Stamen Terrain').add_to(m2)
folium.TileLayer('Stamen Toner').add_to(m2)
folium.TileLayer('Stamen Water Color').add_to(m2)
folium.TileLayer('cartodbpositron').add_to(m2)
folium.TileLayer('cartodbdark_matter').add_to(m2)
folium.LayerControl().add_to(m2)

m2.save("Ex4_Tamanhos/Mapa_Figura.html")
