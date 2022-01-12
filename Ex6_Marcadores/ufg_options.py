import folium


m = folium.Map(location=[-16.6954999, -49.4443552])

folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('Stamen Water Color').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)

tooltip = "Clique aqui!"

folium.Marker(
    [-16.6765656, -49.2430639], popup="<i>UFG - Campus Colemar Natal e Silva</i>", tooltip=tooltip
).add_to(m)
folium.Marker(
    [-16.6062017, -49.2636511], popup="<b>UFG - Campus Samambaia</b>", tooltip=tooltip
).add_to(m)

m.save("Ex6_Marcadores/ufg_markers_options.html")
