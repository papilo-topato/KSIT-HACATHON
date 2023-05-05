import datetime
import configparser
from base64 import b64decode
import webbrowser
import openai
from openai.error import InvalidRequestError
adobe=str(input("enter the text :- "))
num_image=int(input("enter the no. of image to be generated :-"))
#choose resolution 
print("1. resolution 1024x1024 ")
print("2. resolution 512x512 ")
print("3. resolution 256x256 ")
x=int(input(" enter the resolution value"))
def generate_image(prompt, num_image=1, size='512x512', output_format='url'):
    try:
        images = []
        response = openai.Image.create(
            prompt=prompt,
            n=num_image,
            size=size,
            response_format=output_format
        )
        if output_format == 'url':
            for image in response['data']:
                images.append(image.url)
        elif output_format == 'b64_json':
            for image in response['data']:
                images.append(image.b64_json)
        return {'created': datetime.datetime.fromtimestamp(response['created']), 'images': images}
    except InvalidRequestError as e:
        print(e)

config = configparser.ConfigParser() 
config.read('credential.ini')

openai.api_key ='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'

SIZES = ('1024x1024', '512x512', '256x256')

# generate images (url outputs)
if x==1 :
    response = generate_image(adobe, num_image, size=SIZES[0])
    response['created']
    images = response['images']
    for image in images:
        webbrowser.open(image)

elif x==2:
    response = generate_image(adobe, num_image, size=SIZES[1])
    response['created']
    images = response['images']
    for image in images:
        webbrowser.open(image)
elif x==3:
    response = generate_image(adobe, num_image, size=SIZES[2])
    response['created']
    images = response['images']
    for image in images:
        webbrowser.open(image)
else:
    print("invalid input")


