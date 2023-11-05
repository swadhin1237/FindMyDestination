import math

# Function to calculate the Haversine distance between two sets of coordinates
def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(coord1['Latitude'])
    lon1 = math.radians(coord1['Longitude'])
    lat2 = math.radians(coord2['Latitude'])
    lon2 = math.radians(coord2['Longitude'])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

# Example data with temples, waterfalls, and mountains
data = {
    "Temples": [
      {
        "Name": "Shree Somnath Jyotirling Temple",
        "Images": [
          "https://lh5.googleusercontent.com/p/AF1QipOJnhL_lUo0enwUr9iMcY0Cu5Zfqe8STRC2QeW-=w408-h293-k-no",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVtUzJdUG74dpVwbqljLPuhyav46Jlvh59CA&usqp=CAU",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpfaw_ZLD57zFQP6JNKEmgretLoeSce9SwdQ&usqp=CAU"
        ],
        "Location": "Somnath Mandir Rd, Somnath, Prabhas Patan, Gujarat 362268",
        "Coordinates": {
          "Latitude": 20.88809185140322,
          "Longitude": 70.4011463005054
        }
      },
      {
        "Name": "Badrinath Temple, Uttarakhand",
        "Images": [
          "https://lh3.googleusercontent.com/gps-proxy/AFm_dcQBYH63ilyv9pVttODW5-7q5NdcmJzIrz1gopclp-CE7zyA1-1pIoAISeFbTqwH0rkX5a39qCLsTYgtItRW9ZJlE0C_fjc98tjj6XleJIhG3SgfHGPPardX-QEJ_Q2uwU3Y4mawG1ydbFrjACZwJ_FmVjQSPuky0hdIibs5JtwCIS0LOHuGi73elg=w408-h272-k-no",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWYE-PRCUMfBg7mMSZkN_9fqVCCazk0KfMkg&usqp=CAU",
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2018/07/Badrinath-Temple-Uttarakhand.jpg"
        ],
        "Location": "Badri to Mata Murti road, Badrinath, Uttarakhand 246422",
        "Coordinates": {
          "Latitude": 30.90775953658472,
          "Longitude": 79.4089680851403
        }
      },
      {
        "Name": "Shree Jagannath Temple, Puri",
        "Images": [
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2019/04/Jagannath-Temple-Puri.jpg",
          "https://media.gettyimages.com/id/1484152228/photo/puri-jagannath-temple-from-front-with-clear-blue-sky-as-backdrop.jpg?s=612x612&w=0&k=20&c=YpPw0u-ge8rww3VrLJCK5Y7haH-VmNHgWbXzqz4J3QA=",
          "https://lh5.googleusercontent.com/p/AF1QipONEb0ArZ-Um3qquh-XnwWGlZwbJ7ibiTYjNZKe=w408-h305-k-no"
        ],
        "Location": "Bali Sahi, Puri, Odisha 752001",
        "Coordinates": {
          "Latitude": 20.46870206438353,
          "Longitude": 86.24199153398787
        }
      },
      {
        "Name": "Shri Kashi Vishwanath Temple, Varanasi",
        "Images": [
          "https://lh5.googleusercontent.com/p/AF1QipP4c8ozxzWqS-vOxBigD-68SggxhdibPOVHg--w=w408-h309-k-no"
        ],
        "Location": "Lahori Tola, Varanasi, Domari, Uttar Pradesh 221001",
        "Coordinates": {
          "Latitude": 25.31112474611372,
          "Longitude": 83.0108606869724
        }
      },
      {
        "Name": "Meenakshi Amman Temple, Tamil Nadu",
        "Images": [
          "https://lh5.googleusercontent.com/p/AF1QipO8_VJ4ErgBiV2EhJoUPUb6OdmUj22qtuPGY3KL=w408-h609-k-no",
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2022/07/Meenakshi-Amman-Temple.jpg"
        ],
        "Location": "Madurai Main, Madurai, Tamil Nadu 625001",
        "Coordinates": {
          "Latitude": 9.919599606204573,
          "Longitude": 78.11928815236874
        }
      },
      {
        "Name": "Kedarnath Temple, Uttarakhand",
        "Images": [
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2022/03/Kedarnath-Temple.jpg",
          "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia.org%2Fcommons%2F3%2F30%2FKedarnath_Temple.jpg&tbnid=gU-9T97LDK_vZM&vet=12ahUKEwjxv8m8lqqCAxXUoOkKHRTsALUQMygAegQIARAt..i&imgrefurl=https%3A%2F%2Fhi.wikipedia.org%2Fwiki%2F%25E0%25A4%2595%25E0%25A5%2587%25E0%25A4%25A6%25E0%25A4%25BE%25E0%25A4%25B0%25E0%25A4%25A5%25E0%25A4%25AE%25E0%25A4%25A8%25E0%25A5%258D%25E0%25A4%25A6%25E0%25A4%25BF%25E0%25A4%25B0&docid=d6dzuJLNaPX_JM&w=3072&h=2048&q=Kedarnath%20Temple%20(%E0%A4%95%E0%A5%87%E0%A4%A6%E0%A4%BE%E0%A4%B0%E0%A4%A5%20%E0%A4%AE%E0%A4%82%E0%A4%A6%E0%A4%BF%E0%A4%B0)%2C%20Uttarakhand&ved=2ahUKEwjxv8m8lqqCAxXUoOkKHRTsALUQMygAegQIARAt"
        ],
        "Location": "Kedarnath, Uttarakhand 246445",
        "Coordinates": {
          "Latitude": 30.640752874770957,
          "Longitude": 79.11084025891932
        }
      },
      {
        "Name": "Ram Janmabhoomi Temple, Ayodhya",
        "Images": [
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2018/07/Ram-Janmabhoomi-Temple-Ayodhya.jpg",
          "https://lh5.googleusercontent.com/p/AF1QipMt_BX5gDxrzMs4OWQKaFDX3ngvK0le3SwMhY89=w408-h292-k-no"
        ],
        "Location": "Sai Nagar, Ayodhya, Uttar Pradesh 224123",
        "Coordinates": {
          "Latitude": 26.794633391770766,
          "Longitude": 82.19704716873602
        }
      },
      {
        "Name": "Tungnath Mahadev Temple, Uttarakhand",
        "Images": [
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2019/04/Tungnath-Temple.jpg",
          "https://lh5.googleusercontent.com/p/AF1QipPxNNkpp9BW9udjHXaaZkZsuKJG5cg9o4chrpij=w408-h306-k-no"
        ],
        "Location": "Rudraprayag, Uttarakhand 246419",
        "Coordinates": {
          "Latitude": 30.48963321093567,
          "Longitude": 79.22205873011458
        }
      },
      {
        "Name": "Akshardham Temple, Delhi",
        "Images": [
          "https://www.namasteindiatrip.com/blog/wp-content/uploads/2019/04/Akshardham-Temple-Delhi.jpg",
          "https://lh5.googleusercontent.com/p/AF1QipMHxLSqI6J0sQQp60YmEiUT7K1w_CiehPDO7kGM=w408-h541-k-no"
        ],
        "Location": "Noida Mor, Pandav Nagar, New Delhi, Delhi, 110092",
        "Coordinates": {
          "Latitude": 28.612654638481608,
          "Longitude": 77.27750866007291
        }
      }
    ],
    "WaterFalls": [
        {
          "Name": "Palaruvi Waterfalls",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipMrArSachBh4I67BgFM3WGsrubUJxLWLrKQRUIM=w426-h240-k-no",
            "https://images.world-of-waterfalls.com/Palaruvi_Falls_044_11192009.jpg"
          ],
          "Location": "Palaruvi, Kerala",
          "Coordinates": {
            "Latitude": 8.942205975474767,
            "Longitude": 77.16512659839518
          }
        },
        {
          "Name": "Courtallam Falls",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipN3wxN1c_Q66g37nLpt3D9xhl7T0YnJwkkLtTP4=w408-h725-k-no",
            "https://images.world-of-waterfalls.com/Five_Falls_020_11192009.jpg"
          ],
          "Location": "Courtallam, Tamil Nadu",
          "Coordinates": {
            "Latitude": 8.931019567611102,
            "Longitude": 77.23789904072308
          }
        },
        {
          "Name": "SATHODI FALLS",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipNtsYGQ6yqAMNgneJuFdVjUxT3ju_xfn9MYwBb1=w408-h272-k-no",
            "https://images.world-of-waterfalls.com/Sathodi_Falls_014_11142009.jpg"
          ],
          "Location": "Balagar, Karnataka",
          "Coordinates": {
            "Latitude": 14.950683948148148,
            "Longitude": 74.57941293554956
          }
        },
        {
          "Name": "MAGOD FALLS",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipPBM-ChyPuBo68Ds5bBzo46AO4xnhYKahTopltp=w408-h271-k-no",
            "https://images.world-of-waterfalls.com/Magod_Falls_008_11132009.jpg"
          ],
          "Location": "Magod, Karnataka",
          "Coordinates": {
            "Latitude": 14.851044357738484,
            "Longitude": 74.75127889161575
          }
        },
        {
          "Name": "ATHIRAPPILLY FALLS",
          "Images": [
            "https://images.world-of-waterfalls.com/Athirappilly_Falls_014_11162009.jpg",
            "https://lh5.googleusercontent.com/p/AF1QipOBCdltGZdWS9RRhwjugFXgqThjXt3PFjMk_LPa=w408-h544-k-no"
          ],
          "Location": "Pariyaram, Kerala",
          "Coordinates": {
            "Latitude": 10.285225543122365,
            "Longitude": 76.56987325257484
          }
        },
        {
          "Name": "DUDHSAGAR FALLS",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipPI-KJH8jWecrgce0ItKscubeoCH7Lghtl5yPLG=w408-h270-k-no",
            "https://images.world-of-waterfalls.com/Dudhsagar_012_11122009.jpg"
          ],
          "Location": "Sonaulim, Goa",
          "Coordinates": {
            "Latitude": 15.316432647879767,
            "Longitude": 74.31391557720175
          }
        },
        {
          "Name": "NOHKALIKAI FALLS",
          "Images": [
            "https://images.world-of-waterfalls.com/Nohkalikai_Falls_013_11092009.jpg",
            "https://lh5.googleusercontent.com/p/AF1QipNCH8_i4xY0ea5n97DRhI0_qWk0MeIsJM-TRTcp=w408-h306-k-no"
          ],
          "Location": "Meghalaya",
          "Coordinates": {
            "Latitude": 25.275559193072418,
            "Longitude": 91.68608191607822
          }
        },
        {
          "Name": "JOG FALLS",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipORqL5O11k-8baMb_AIwdNZkAWiZEv8N22Kftzt=w408-h306-k-no",
            "https://images.world-of-waterfalls.com/Jog_Falls_016_11142009.jpg"
          ],
          "Location": "Jog Falls, Karnataka",
          "Coordinates": {
            "Latitude": 14.2301951552093,
            "Longitude": 74.81245772758568
          }
        },
        {
          "Name": "UNCHALLI FALLS",
          "Images": [
            "https://images.world-of-waterfalls.com/Unchalli_Falls_077_11142009.jpg",
            "https://lh5.googleusercontent.com/p/AF1QipOPIii22tbq_rCRfkCbBccrRV2X7YSwxHKeu0Kx=w408-h306-k-no"
          ],
          "Location": "Unchalli, Karnataka",
          "Coordinates": {
            "Latitude": 14.409352882433602,
            "Longitude": 74.74772690558359
          }
        },
        {
          "Name": "Barehipani Waterfall",
          "Images": [
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCadpp3WePVfVLE65pp8X0gRWy714UMq9ttQ&usqp=CAU",
            "https://lh5.googleusercontent.com/p/AF1QipPXANXmR-CvC9V4TRtYulXvWljW4imKlF5rDpGF=w408-h271-k-no"
          ],
          "Location": "Odisha",
          "Coordinates": {
            "Latitude": 21.93298910296506,
            "Longitude": 86.38068082315479
          }
        }
      ],
      "Mountains": [
        {
          "Name": "Mullayanagiri Peak",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipPL3SwsM097Um8CSFgvCdfjJWBVjAqXTlZ8gn_n=w408-h306-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/6e/54/05/img-20180922-090745-hdr.jpg?w=500&h=400&s=1"
          ],
          "Location": "Mullayanagiri Peak, Karnataka",
          "Coordinates": {
            "Latitude": 13.391803508821944,
            "Longitude": 75.72287439773328
          }
        },
        {
          "Name": "Triund Hill",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipO279E9I-ddu6Q9Dth_jZUSz3a4IFGgbwvmdpsZ=w445-h240-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/42/10/8e/triund-hill.jpg?w=500&h=400&s=1"
          ],
          "Location": "Triund Hill, Himachal Pradesh",
          "Coordinates": {
            "Latitude": 32.260398603147316,
            "Longitude": 76.35653578274666
          }
        },
        {
          "Name": "Kangchenjunga",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipMSRdAoVUK9yQIerF8pR0lYft0cFChxR-hJc4g=w408-h266-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/f6/77/2b/queen-of-hills.jpg?w=500&h=400&s=1"
          ],
          "Location": "Kangchenjunga, Lelep, Nepal",
          "Coordinates": {
            "Latitude": 27.70279453746622,
            "Longitude": 88.14762077998685
          }
        },
        {
          "Name": "Dainkund Peak",
          "Images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/ed/3a/e3/img-20160415-220504-largejpg.jpg?w=500&h=400&s=1",
            "https://lh5.googleusercontent.com/p/AF1QipN9Itt1a0HZi1nWFqf8PXzIXpIKHj2lOR3814G-=w408-h306-k-no"
          ],
          "Location": "Dainkund Peak, Rakhed, Himachal Pradesh",
          "Coordinates": {
            "Latitude": 32.520414614860705,
            "Longitude": 76.03574782016224
          }
        },
        {
          "Name": "Apharwat Peak",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipP4tGBiAa0lOwQHxxER4Bpkhk-11UvV8cXClHQY=w408-h272-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/ec/b0/41/img-20180131-wa0006-largejpg.jpg?w=500&h=400&s=1"
          ],
          "Location": "Apharwat Peak, Kashmir",
          "Coordinates": {
            "Latitude": 34.03969263045522,
            "Longitude": 74.3236247929554
          }
        },
        {
          "Name": "Nandi Hills",
          "Images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/9b/9a/3e/20160612-141224-largejpg.jpg?w=500&h=400&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/1f/a0/63/nandi-hills.jpg?w=500&h=-1&s=1"
          ],
          "Location": "Nandi Hills, Karnataka",
          "Coordinates": {
            "Latitude": 13.381807858895625,
            "Longitude": 77.67412535359709
          }
        },
        {
          "Name": "Doddabetta Peak",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipNyeIW07_wBaRrMmtK6J-Sy1DfwICW8QMi5BCn8=w426-h240-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/06/1e/34/photo1jpg.jpg?w=500&h=-1&s=1"
          ],
          "Location": "Doddabetta Peak, Tamil Nadu",
          "Coordinates": {
            "Latitude": 11.400831140583273,
            "Longitude": 76.7357735824683
          }
        },
        {
          "Name": "Chembra Peak",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipNYfAc1u8HkMmnorve9HDL3IM9X-2yNOn28PMVm=w408-h255-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/13/14/e9/do-not-miss-this-view.jpg?w=500&h=400&s=1"
          ],
          "Location": "Chembra Peak, Kerala",
          "Coordinates": {
            "Latitude": 11.512174839250857,
            "Longitude": 76.08814354560745
          }
        },
        {
          "Name": "Yume Samdong (Zero Point)",
          "Images": [
            "https://lh5.googleusercontent.com/p/AF1QipP5Mt-gRHWz0iy5IdPF7QOfmrxfe-Gr0QYVyJyk=w408-h272-k-no",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/e9/70/a3/yumesamdong-zero-point.jpg?w=500&h=-1&s=1"
          ],
          "Location": "Yume Samdong (Zero Point), Sikkim",
          "Coordinates": {
            "Latitude": 27.935000127356783,
            "Longitude": 88.73635692091717
          }
        },
        {
          "Name": "Chitkul",
          "Images": [
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/15/10/81/18/chitkul.jpg?w=500&h=-1&s=1",
            "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/a3/b4/d2/caption.jpg?w=500&h=400&s=1"
          ],
          "Location": "Chitkul, Himachal Pradesh",
          "Coordinates": {
            "Latitude": 31.353067503657343,
            "Longitude": 78.43612569971108
          }
        }
      ]
}

# Define the maximum distance a person can travel in one day (in kilometers)
max_distance_per_day = 30  # Adjust this value as needed

# Initialize empty clusters
clusters = []

# Iterate through each category (Temples, Waterfalls, Mountains)
for category, locations in data.items():
    for location in locations:
        # Create a new cluster for the location
        new_cluster = [(location, category)]

        # Iterate through the remaining locations to form clusters
        for other_location in locations:
            if location != other_location:
                distance = haversine_distance(location['Coordinates'], other_location['Coordinates'])
                if distance <= max_distance_per_day:
                    new_cluster.append((other_location, category))

        # Check if the new cluster already exists in the clusters list
        is_duplicate = False
        for cluster in clusters:
            if set(new_cluster) == set(cluster):
                is_duplicate = True
                break
        # If the new cluster is not a duplicate, add it to the clusters list
        if not is_duplicate:
            clusters.append(new_cluster)

# Print the clusters
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}:")
    for location, category in cluster:
        print(f"{location['Name']} - {category}")
    print("\n")