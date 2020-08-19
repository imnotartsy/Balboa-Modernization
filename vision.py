from google.cloud import vision
import io

# enter in cmdline:
#export GOOGLE_APPLICATION_CREDENTIALS="Balboa-Modernization-760f368bcd91.json"

# https://cloud.google.com/vision/docs/ocr?apix_params=%7B%22resource%22%3A%7B%
#  7D%7D#vision_text_detection-python
def detect_text(path, verbose):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if verbose:
        print('Texts:')

        for text in texts:
            print('\n"{}"'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])

            print('bounds: {}'.format(','.join(vertices)))

    return texts

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


data = detect_text("image.jpg", False)

# Convert to strings
textStrings = []
for text in data:
    textStrings.append(str(text.description))

print(len(textStrings)) # 520

print(type(textStrings))
print(type(textStrings[0]))



names = []
# print(textStrings[1])

# Assumes the first text recovnized is not a last name lmao
for i in range(2, len(textStrings)):
    # ## print (i)
    # if i == 1:
    #     print (textStrings[i-1])
    if "Owner:" in textStrings[i-1]:
        name = ""
        while ":" not in textStrings[i]:
            name += textStrings[i] + " "
            i = i+1
        names.append(name)

for name in names:
    print(name)



print("done")