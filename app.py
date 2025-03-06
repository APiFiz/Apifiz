import folium
from folium.plugins import Search

# Define the center of JNU Campus
jnu_center = [28.5406, 77.1662]

# Create a map centered around JNU
jnu_map = folium.Map(location=jnu_center, zoom_start=15)

# Feature group for markers
search_layer = folium.FeatureGroup(name="JNU Locations").add_to(jnu_map)

# Dictionary containing all locations (hostels, schools, dhabas, etc.)
locations = {
    "JNU Main Gate": [28.5424, 77.1630],
    "Central Library": [28.5400, 77.1690],
    "Sabarmati Dhaba": [28.5405, 77.1680],
    "Lohit Dhaba": [28.5410, 77.1675],
    "Ganga Dhaba": [28.5420, 77.1665],
    "Parthasarathy Rocks": [28.5375, 77.1625],
    # Schools
    "School of Computer & Systems Sciences": [28.5382, 77.1655],
    "School of Social Sciences": [28.5378, 77.1640],
    # Hostels
    "Damodar Hostel": [28.5435, 77.1685],
    "Koyna Hostel": [28.5450, 77.1690],
    "Shipra Hostel": [28.5440, 77.1675],
    "Mahi Hostel": [28.5430, 77.1660],
    "Chandrabhaga Hostel": [28.5420, 77.1650],
    "Sutlej Hostel": [28.5410, 77.1640],
    "Lohit Hostel": [28.5400, 77.1630],
    "Sabarmati Hostel": [28.5390, 77.1620],
    "Narmada Hostel": [28.5380, 77.1610],
    "Godavari Hostel": [28.5370, 77.1600],
    "Ganga Hostel": [28.5360, 77.1590],
    "Kaveri Hostel": [28.5350, 77.1580],
    "Periyar Hostel": [28.5340, 77.1570]
}

# Create a list of formatted data for search
search_data = []

# Add markers and prepare search data
for place, coords in locations.items():
    marker = folium.Marker(
        location=coords,
        popup=place,
        tooltip=place,
        icon=folium.Icon(color="blue" if "Dhaba" not in place else "green"),
    )
    marker.add_to(search_layer)

    # Append search data as GeoJSON
    search_data.append({"loc": coords, "name": place})

# Add Search plugin with proper indexing
search = Search(
    layer=search_layer,
    search_label="name",
    geom_type="Point",
    placeholder="Search JNU...",
    collapsed=False
).add_to(jnu_map)

# Save the map to an HTML file
jnu_map.save("jnu_fixed_search_map.html")

print("✅ JNU Fixed Searchable Map has been generated. Open 'jnu_fixed_search_map.html' in your browser to view it.")