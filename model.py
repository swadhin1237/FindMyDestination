import json
import requests
from PIL import Image
from io import BytesIO
from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch
import math 
# import clip
# from transformers import CLIPProcessor, CLIPModel
UNSPLASH_ACCESS_KEY='-t_MrYB3fgtLStQQikmfYFqXr2sJTrTBO5bPikYu7Tw'
from pyunsplash import PyUnsplash

with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

WaterFalls = data_dict['WaterFalls']
Temples = data_dict['Temples']
Mountains = data_dict['Mountains']

def extract_image(image_url):
    # Send an HTTP GET request to the image URL
    response = requests.get(image_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the content of the response, which is the image data
        image_data = response.content

        # Create a Pillow (PIL) image object from the image data
        img = Image.open(BytesIO(image_data))

        # You can now work with the 'img' object, such as displaying it or processing it.
        # For example, to display the image:
        img.show()
        return img
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        return None

def get_tensor_by_path(image):
    # Resize the image to 224x224
    image = image.resize((224, 224))
    # Convert the grayscale image to RGB
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Load the feature extractor and ViT model
    feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
    model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")
    # Preprocess the image
    inputs = feature_extractor(images=image, return_tensors="pt")
    # Get the output from the model
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    # Access the tensor from the specified hidden state layer
    hidden_state = outputs.hidden_states[10]
    # Remove the class token feature vector (the first feature vector)
    hidden_state = hidden_state[:, 1:, :]
    flat_tensor = hidden_state.view(-1)
    normalized_tensor = flat_tensor / torch.norm(flat_tensor, p=2)
    # Return the normalized tensor
    return normalized_tensor

def get_similarity_score(image_path1, tensor2):
    # Get tensors for both images
    tensor1 = get_tensor_by_path(image_path1)
    # Calculate the cosine similarity between the two tensors
    similarity_score = torch.dot(tensor1, tensor2).item()

    return similarity_score



def get_similar_Waterfalls(test_link):
    test_img = extract_image(test_link)
    if test_img is None:
        return None
    tensor2=get_tensor_by_path(test_img)
    # tensor2=test_img
    score_index=[]
    for i in WaterFalls:
        score=0
        for j in i['Images']:
            img = extract_image(j)
            if img is None:
                continue
            score=max(get_similarity_score(img, tensor2),score)
        print(score," ",i['Name'])
        score_index.append((score,i))
    score_index.sort(reverse=True)
    return score_index

def get_similar_Temples(test_link):
    test_img = extract_image(test_link)
    if test_img is None:
        return None
    tensor2=get_tensor_by_path(test_img)
    # tensor2=test_img
    score_index=[]
    for i in Temples:
        score=0
        for j in i['Images']:
            img = extract_image(j)
            if img is None:
                continue
            score=max(get_similarity_score(img, tensor2),score)
        print(score," ",i['Name'])
        score_index.append((score,i))
    score_index.sort(reverse=True)
    return score_index

def get_similar_Mountains(test_link):
    test_img = extract_image(test_link)
    if test_img is None:
        return None
    tensor2=get_tensor_by_path(test_img)
    # tensor2=test_img
    score_index=[]
    for i in Mountains:
        score=0
        for j in i['Images']:
            img = extract_image(j)
            if img is None:
                continue
            score=max(get_similarity_score(img, tensor2),score)
        print(score," ",i['Name'])
        score_index.append((score,i))
    score_index.sort(reverse=True)
    return score_index
    
# for i in WaterFalls[0]['Images']:
#     extract_image(i)




def result(name,tag):
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)

    photos = pu.photos(type_='random', count=1, featured=True, query=name)
    [photo] = photos.entries
    print(photo.id, photo.link_download)
    if tag=="waterfall":
        arr=get_similar_Waterfalls(photo.link_download)
    elif tag=="temple":
        arr=get_similar_Temples(photo.link_download)
    elif tag=="mountain":
        arr=get_similar_Mountains(photo.link_download)
    print(arr)
    fin=[]
    for i in range(0,5):
        fin.append(arr[i][1])
    return fin


result("niagara falls")