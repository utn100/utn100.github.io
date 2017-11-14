from ast import literal_eval as make_tuple
import folium
with open('geocode_combined.csv','r') as f:
	code = [line.rstrip() for line in f]
    code =[item for item in code if item != ""]

#Convert each location point to tuple
code_tuple = []
for item in code:
	code_tuple.append(make_tuple(item[1:(len(item)-1)]))

#Map the points
latlon = code_tuple
mapit = folium.Map( location=[40, -1.464582], zoom_start=2 )
for coord in latlon:
	folium.CircleMarker(location=[coord[0],coord[1]],
                        radius=1,fill=True,
                        fill_color='#FF0000',
                        fill_opacity=0.4,
                        weight=1,
                        color='#FF0000').add_to(mapit)
mapit.save( 'map.html')