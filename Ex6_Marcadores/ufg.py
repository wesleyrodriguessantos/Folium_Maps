import folium

m = folium.Map(location=[-16.6954999, -49.4443552], tiles='OpenStreetMap')

tooltip = "Clique aqui!"

folium.Marker(
    [-16.6765656, -49.2430639], popup="<i>UFG - Campus Colemar Natal e Silva</i>", tooltip=tooltip
).add_to(m)
folium.Marker(
    [-16.6062017, -49.2636511], popup="<b>UFG - Campus Samambaia</b>", tooltip=tooltip
).add_to(m)

m.save("Ex6_Marcadores/ufg_markers.html")
