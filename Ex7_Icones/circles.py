import folium


m = folium.Map(location=[-16.6689782, -49.3082348],
               tiles="OpenStreetMap", zoom_start=12)

folium.Circle(
    radius=25,
    location=[-16.6765656, -49.2430639],
    popup="UFG - Campus Colemar Natal e Silva",
    color="crimson",
    fill=False,
).add_to(m)

folium.CircleMarker(
    location=[-16.6062017, -49.2636511],
    radius=100,
    popup="UFG - Campus Samambaia",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

m.save("Ex7_Icones/circles.html")
