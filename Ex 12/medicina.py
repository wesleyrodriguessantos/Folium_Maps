import pandas as pd
import branca
import folium
from folium.plugins import MarkerCluster

left_col_color = "#6FB668"
right_col_color = "#ffccdd"

df = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex 12\medicina.xlsx", engine='openpyxl')

m = folium.Map(location=[-14.235004, -51.95528], zoom_start=4)


for grp_name, df_grp in df.groupby('UF'):
    feature_group = MarkerCluster(name=grp_name)

    for row in df_grp.itertuples():
        institution_type = row.CATEGORIA_ADMINISTRATIVA
        if institution_type.count("Pública") == 0:
            color = 'darkblue'
        elif institution_type.count("Privada") == 0:
            color = 'red'
        if institution_type.count("Especial") == 1:
            color = 'green'

        html = """<!DOCTYPE html>
<html>

    <head>
        <h5 style="margin-bottom:10"; width="200px">{}</h5>""".format(row.NOME_DA_IES) + """
    </head>
    <table style="height: 130px;">
        <tbody>
            <tr>
                <td style="width: 100px;padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Categoria Administrativa</span></td>
                <td style="width: 300px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(institution_type) + """
            </tr>
            <tr>
                <td style="padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Qt. Vagas Autorizadas</span></td>
                <td style="width: 300px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(row.QT_VAGAS_AUTORIZADAS) + """
            </tr>
            <tr>
                <td style="padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">Quantitativo de Vagas - Integral</span></td>
                <td style="width: 300px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(row.QT_VAGAS_INTEGRAL) + """
            </tr>
        </tbody>
    </table>
</html>
"""
        iframe = branca.element.IFrame(html=html, width=510, height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        folium.Marker(location=[row.LATITUDE, row.LONGITUDE], popup=popup, icon=folium.Icon(color=color, icon='university', prefix='fa')).add_to(
            feature_group)

    feature_group.add_to(m)

folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)

m.save('Ex 12/Medicina.html')
