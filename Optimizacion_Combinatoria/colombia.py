import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from shapely.geometry import Point
df = pd.DataFrame({
    'City': ['Palmira', 'Pasto', 'Tuluá', 'Bogota', 'Pereira','Armenia','Manizales','Valledupar','Montería','Soledad','Cartagena','Barranquilla','Medellín','Bucaramanga','Cúcuta'],
    'Country': ['Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia', 'Colombia'],
    'Latitude': [3.53944, 1.21361, 4.08466, 4.60971, 4.81333,4.53389,5.06889,10.46314,8.74798 ,10.91843,10.39972,10.96854,6.25184,7.12539,7.89391],
    'Longitude': [-76.30361, -77.28111, -76.19536, -74.08175, -75.69611,-75.68111,-75.51738,-73.25322,-75.88143,-74.76459,-75.51444,-74.78132,-75.56359,-73.1198,-72.50782]
})
df["Coordinates"] = list(zip(df.Longitude, df.Latitude))
df["Coordinates"] = df["Coordinates"].apply(Point)
gdf = gpd.GeoDataFrame(df, geometry="Coordinates")
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
world = world.set_index("iso_a3")
fig, gax = plt.subplots(figsize=(10,10))

# By only plotting rows in which the continent is 'South America' we only plot SA.
world.query("name == 'Colombia'").plot(ax=gax, edgecolor='black',color='white')

# By the way, if you haven't read the book 'longitude' by Dava Sobel, you should...
gax.set_xlabel('longitude')
gax.set_ylabel('latitude')
gdf.plot(ax=gax, color='red', alpha = 1)
gax.spines['top'].set_visible(False)
gax.spines['right'].set_visible(False)
for x, y, label in zip(gdf['Coordinates'].x, gdf['Coordinates'].y, gdf['City']):
    gax.annotate(label, xy=(x,y), xytext=(4,4), textcoords='offset points')

plt.show()
