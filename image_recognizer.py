from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch
import os
import csv

IMAGE_PATH = './test.jpeg'
layer_index = 10


def get_tensor_by_path(path):
    # Load the image
    image = Image.open(path)

    # Resize the image to 224x224
    image = image.resize((224, 224))

    # Convert the grayscale image to RGB
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Load the feature extractor and ViT model
    feature_extractor = ViTFeatureExtractor.from_pretrained(
        "google/vit-base-patch16-224")
    model = ViTForImageClassification.from_pretrained(
        "google/vit-base-patch16-224")

    # Preprocess the image
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Get the output from the model
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)

    # Access the tensor from the specified hidden state layer
    hidden_state = outputs.hidden_states[layer_index]

    # Remove the class token feature vector (the first feature vector)
    hidden_state = hidden_state[:, 1:, :]

    flat_tensor = hidden_state.view(-1)

    normalized_tensor_1 = flat_tensor / torch.norm(flat_tensor, p=2)

    # Print the hidden state tensor
    return normalized_tensor_1


input_image_tensor = get_tensor_by_path(IMAGE_PATH)

image_dir = './pics'
all_files = os.listdir(image_dir)
image_files = [f for f in all_files if f.lower().endswith(
    ('.jpg', '.jpeg', '.png'))]

i = 0
scores_and_filenames = []

for image_file in image_files:
    test_image_path = os.path.join(image_dir, image_file)
    test_image_tensor = get_tensor_by_path(test_image_path)
    test_image_score = torch.dot(test_image_tensor, input_image_tensor)
    scores_and_filenames.append((1-test_image_score.item(), image_file))

# sort the list by score in descending order
scores_and_filenames.sort(key=lambda x: x[0], reverse=True)

# save the scores_and_filenames list as a CSV file
csv_filename = 'scores_and_filenames.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Score', 'Filename'])
    csv_writer.writerows(scores_and_filenames)

print(f'Saved scores and filenames to {csv_filename}')