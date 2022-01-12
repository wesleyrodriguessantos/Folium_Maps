import folium

m = folium.Map(location=[-16.6954999, -49.4443552], tiles='OpenStreetMap')

tooltip = "Clique aqui!"

folium.Marker(
    [-16.6765656, -49.2430639], popup="<i>UFG - Campus Colemar Natal e Silva</i>", tooltip=tooltip,
    icon=folium.Icon(color='lightgray', icon='graduation-cap', prefix='fa')
).add_to(m)
folium.Marker(
    [-16.6062017, -49.2636511], popup="<b>UFG - Campus Samambaia</b>", tooltip=tooltip,
    icon=folium.Icon(color='green', icon='home', prefix='fa')
).add_to(m)
folium.Marker(
    [-16.708241, -49.2732332], popup="<b>Parque Vaca Brava</b>", tooltip=tooltip,
    icon=folium.Icon(icon="cloud")
).add_to(m)
folium.Marker(
    [-16.7091795, -49.2554342], popup="<b>Hospital de Urgências de Goiânia</b>", tooltip=tooltip,
    icon=folium.Icon(color="red", icon="heart")
).add_to(m)

m.save("Ex7_Icones/icons.html")
