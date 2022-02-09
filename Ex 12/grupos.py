import pandas as pd
import branca
import folium
from folium.plugins import MarkerCluster

left_col_color = "#19a7bd"
right_col_color = "#ffccdd"

ler = pd.read_excel(
    r"D:\xampp\htdocs\Folium_Maps\Ex 12\municipiosreduzidos.xlsx", engine='openpyxl')

m = folium.Map(location=[-14.235004, -51.95528], zoom_start=4)


for grp_name, df_grp in ler.groupby('UF'):
    feature_group = MarkerCluster(name=grp_name)

    for row in df_grp.itertuples():
        institution_type = row.CATEGORIA
        if institution_type == 'Pública':
            color = 'darkblue'
        else:
            color = 'gray'

        html = """<!DOCTYPE html>
<html>

    <head>
        <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(row.NOME_MUNICIPIO) + """
    </head>
    <table style="height: 126px; width: 350px;">
        <tbody>
            <tr>
                <td style="width: 50px;padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">CATEGORIA</span></td>
                <td style="width: 150px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(institution_type) + """
            </tr>
            <tr>
                <td style="padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">CÓDIGO IBGE</span></td>
                <td style="width: 150px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(row.COD_IBGE) + """
            </tr>
            <tr>
                <td style="padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">ESTADO</span></td>
                <td style="width: 150px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(row.ESTADO) + """
            </tr>
            <tr>
                <td style="padding:3px;background-color: """ + left_col_color + """;"><span style="color: #ffffff;">REGIÃO</span></td>
                <td style="width: 150px;padding:3px;background-color: """ + right_col_color + """;">{}</td>""".format(row.REGIAO) + """
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

m.save('Teste6.html')
