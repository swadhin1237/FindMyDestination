import folium

# Create a map centered at a specific coordinate
map_center = [20, 70]  # Replace with the central coordinate

# Create a map with the specified center and an initial zoom level
mymap = folium.Map(location=map_center, zoom_start=10)  # Adjust zoom level as needed

# Define a list of locations with their coordinates
locations = [
        {
            "Name": "Shree Somnath Jyotirling Temple",
            "Latitude": 20.88809185140322,
            "Longitude": 70.4011463005054
        },
        {
            "Name": "Badrinath Temple, Uttarakhand",
            "Latitude": 30.90775953658472,
            "Longitude": 79.4089680851403
        },
        {
            "Name": "Shree Jagannath Temple, Puri",
            "Latitude": 20.46870206438353,
            "Longitude": 86.24199153398787
        },
        {
            "Name": "Shri Kashi Vishwanath Temple, Varanasi",
            "Latitude": 25.31112474611372,
            "Longitude": 83.0108606869724
        },
        {
            "Name": "Meenakshi Amman Temple, Tamil Nadu",
            "Latitude": 9.919599606204573,
            "Longitude": 78.11928815236874
        },
        {
            "Name": "Kedarnath Temple, Uttarakhand",
            "Latitude": 30.640752874770957,
            "Longitude": 79.11084025891932
        },
        {
            "Name": "Ram Janmabhoomi Temple, Ayodhya",
            "Latitude": 26.794633391770766,
            "Longitude": 82.19704716873602
        },
        {
            "Name": "Tungnath Mahadev Temple, Uttarakhand",
            "Latitude": 30.48963321093567,
            "Longitude": 79.22205873011458
        },
        {
            "Name": "Akshardham Temple, Delhi",
            "Latitude": 28.612654638481608,
            "Longitude": 77.27750866007291
        },
        {
            "Name": "Palaruvi Waterfalls",
            "Latitude": 8.942205975474767,
            "Longitude": 77.16512659839518
        },
        {
            "Name": "Courtallam Falls",
            "Latitude": 8.931019567611102,
            "Longitude": 77.23789904072308
        },
        {
            "Name": "SATHODI FALLS",
            "Latitude": 14.950683948148148,
            "Longitude": 74.57941293554956
        },
        {
            "Name": "MAGOD FALLS",
            "Latitude": 14.851044357738484,
            "Longitude": 74.75127889161575
        },
        {
            "Name": "ATHIRAPPILLY FALLS",
            "Latitude": 10.285225543122365,
            "Longitude": 76.56987325257484
        },
        {
            "Name": "DUDHSAGAR FALLS",
            "Latitude": 15.316432647879767,
            "Longitude": 74.31391557720175
        },
        {
            "Name": "NOHKALIKAI FALLS",
            "Latitude": 25.275559193072418,
            "Longitude": 91.68608191607822
        },
        {
            "Name": "JOG FALLS",
            "Latitude": 14.2301951552093,
            "Longitude": 74.81245772758568
        },
        {
            "Name": "UNCHALLI FALLS",
            "Latitude": 14.409352882433602,
            "Longitude": 74.74772690558359
        },
        {
            "Name": "Barehipani Waterfall",
            "Latitude": 21.93298910296506,
            "Longitude": 86.38068082315479
        },
        {
            "Name": "Mullayanagiri Peak",
            "Latitude": 13.391803508821944,
            "Longitude": 75.72287439773328
        },
        {
            "Name": "Triund Hill",
            "Latitude": 32.260398603147316,
            "Longitude": 76.35653578274666
        },
        {
            "Name": "Kangchenjunga",
            "Latitude": 27.70279453746622,
            "Longitude": 88.14762077998685
        },
        {
            "Name": "Dainkund Peak",
            "Latitude": 32.520414614860705,
            "Longitude": 76.03574782016224
        },
        {
            "Name": "Apharwat Peak",
            "Latitude": 34.03969263045522,
            "Longitude": 74.3236247929554
        },
        {
            "Name": "Nandi Hills",
            "Latitude": 13.381807858895625,
            "Longitude": 77.67412535359709
        },
        {
            "Name": "Doddabetta Peak",
            "Latitude": 11.400831140583273,
            "Longitude": 76.7357735824683
        },
        {
            "Name": "Chembra Peak",
            "Latitude": 11.512174839250857,
            "Longitude": 76.08814354560745
        },
        {
            "Name": "Yume Samdong (Zero Point)",
            "Latitude": 27.935000127356783,
            "Longitude": 88.73635692091717
        },
        {
            "Name": "Chitkul",
            "Latitude": 31.353067503657343,
            "Longitude": 78.43612569971108
        }
    ]

# Add markers for each location to the map
for location in locations:
    folium.Marker(
        location=[location["Latitude"], location["Longitude"]],
        popup=location["Name"],
    ).add_to(mymap)

# Save the map as an HTML file
mymap.save("my_map.html")

# Display the map in a Jupyter Notebook
# mymap
