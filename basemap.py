import folium
import pandas
#dir(folium) #to see what folium functionality is implemented
#help(folium.map)
#how to win friends and influence people
#within 10 seconds, explain and answer "do you see what I see, this is what your facing, this is what you need"
## succession of no answers is powerful
# Ronald Regan, are you better off?
# simultaneous empathy and epiphany response from other person
# should leave every negotiation with the other party leaving with full respect for you

data = pandas.read_csv("Volcanoes.txt")
print("Volcanoes.txt contains the following data:")
print(data)

print("The data type of Volcanoes.txt is:")
type(data)

print("The columns of Volcanoes.txt is:")
print(data.columns)

print("The number of rows in the lat columns is:")
len(data["LAT"])

print("The functionality provided by folium map module is:")
dir(folium)

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer():
	if elevation < 1000:
		return 'green'
	elif 1000 <= elecation < 3000:
		return 'orange'
	else:
		return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")

#Adding coordinates with a loop
#for coordinates in [[38.2, -99.1], [39.2, -97.1]]
#	fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

for lt, ln, el in zip(lat, lon, elev):
	fg.add_child(folium.Marker(location=[lt, ln], popup=f"{str(el)}+ m", icon=folium.Icon(color=color_producer())))

# Adding HTML to popup windows
html="""<h4>Volcano information:</h4>
Height: %s m
"""
'''
for lt, ln, el in zip(lat, lon, elev):
	iframe = folium.IFrame(html=html % str(el), width=200, height=100)
	fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))
'''

# Adding HTML with links to popups
html2="""
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height %s m
"""
'''
for lt, ln, el, name in zip(lat, lon, elev, name):
	iframe = folium.IFrame(html=html % (name, name, el), width = 200, height=100)
	fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

'''

#Example lambda function
# >>> l = lambda x: x**2
# >>> l(5)
#output: 25

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


