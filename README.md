# Travel Destination Recommendation

## Project Overview

Travel Destination Recommendation is a project that helps users find travel destinations in India that have a similar feel to their desired international destinations. This recommendation system leverages a PyTorch model to analyze and compare images to provide users with visually similar travel options.

# Demo Video

[![Demo Video](https://www.bing.com/ck/a?!&&p=099dd85d24279965JmltdHM9MTY5OTA1NjAwMCZpZ3VpZD0wODZlZjM4OS01Zjg0LTYyN2EtMzg1OS1lMzQyNWUzNjYzZGQmaW5zaWQ9NTU4Mw&ptn=3&hsh=3&fclid=086ef389-5f84-627a-3859-e3425e3663dd&u=a1L2ltYWdlcy9zZWFyY2g_cT1pbWFnZSBvZiBhIGRlbW8gdmlkZW8gZm9yIHRyYXZlbGxpbmcgJkZPUk09SVFGUkJBJmlkPUQ5NzhCMDIwMDY4QTJCREIzODk5RDJCRDg2MERCRjI3MEEzMkU5NDc&ntb=1)](https://drive.google.com/drive/folders/1-q78whNGHJhqd6bzKq9JxE08flJnpKG4?usp=sharing)

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Uniqueness](#unique)

## Getting Started
<a name="getting-started"></a>
To get started with this project, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/travel-destination-recommendation.git
  
2. Install the required packages:
    ```bash
    pip install -r requirements.txt

3. Run the application:
   ```bash
   python app.py

## Project Structure
<a name="project-structure"></a>
The project structure is organized as follows:

FindMyDestination/
-    ├── app.py            # Flask web application
-    ├── static/
-    │   ├── images/       # Static images
-    │   ├── css/          # Cascading Style Sheets
-    │   ├── js/           # JavaScript files
-    ├── templates/        # HTML templates
-    ├── datafile and model           # Data files
-    ├── requirements.txt  # Python dependencies
-    ├── README.md         # Project documentation

## Usage
<a name="usage"></a>
1. Visit the web application (usually at http://localhost:5000).

2. Upload an detail of your desired international destination.

3. The PyTorch model will analyze the image and find visually similar places in India.

4. The application will display a list of recommended travel destinations in India based on image similarity and along with places nearby them.

## How It Works
<a name="how-it-works"></a>
The application works by using a PyTorch model to extract features from images of travel destinations. These features are then used to find visually similar destinations in India. The recommendation system is based on the similarity between the feature representations of images.

## Contributing
<a name="contributing"></a>
Contributions to this project are welcome. Feel free to open issues, suggest improvements, or submit pull requests to help make this project even better.

## Uniqueness
<a name="unique"></a>
In our project, we've developed the majority of the code from scratch, especially the backend logic and functionality. However, due to time constraints, we've integrated some frontend components from external sources available on the internet. While we've customized and integrated these components to suit our project's needs, the core logic and backend development were created entirely from the ground up.

