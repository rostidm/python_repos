import folium
map = folium.Map(location=[53.7098,27.9534])
fg = folium.FeatureGroup(name="Map")

for coords in [[53.7098,27.9534],[60,10]]:
    fg.add_child(folium.Marker(location=coords, popup="Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("index.html")