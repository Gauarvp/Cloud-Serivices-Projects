from google.cloud import vision_v1p3beta1 as vision
from google.cloud import language_v1

def analyze_image(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)

    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

def analyze_sentiment(text):
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})

    sentiment = response.document_sentiment
    score = sentiment.score
    magnitude = sentiment.magnitude

    print('Sentiment:')
    print(f'Score: {score}')
    print(f'Magnitude: {magnitude}')

# Usage
image_path = 'path/to/image.jpg'
text = 'I am feeling great today!'

analyze_image(image_path)
analyze_sentiment(text)
