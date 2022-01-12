import folium

m2 = folium.Map(width=800, height=600,
                location=[-16.6815233, -49.2531244], zoom_start=11, min_zoom=8, max_zoom=14)

m2.save("Ex5_Zoom/Limitar_Zoom.html")
