import requests
from flask import Flask, render_template
import numpy as np
from PIL import Image

# These are global variables
# data_base: saves the images names, requested functions and their results to use it for future identical requests
# number_of_images: The number of all images stored in the Cloud Storage Bucket
data_base = {"image_name": {"min": "0", "max": "0", "mean": "0", "median": "0", "pXXX": "0"}}
number_of_images = 10

app = Flask(__name__)


# The home page route that display all images from the Cloud Storage Bucket
@app.route('/')
def home():
    return render_template('HomePage.html', value=number_of_images+1)


# The function page route that display all functions for the requested image
@app.route('/functions/<img_name>', methods=['GET'])
def functions(img_name):
    return render_template('Functions.html', img_name=img_name)


@app.route('/health')
def default():
    return 'OK'


# The Statistics page route that display the requested function result for an image
@app.route('/stats/<img_name>/<func>', methods=['GET'])
def stats(img_name, func):
    # this code checks if the requested function result already stored in data_base
    if img_name in data_base:
        if func in data_base[img_name]:
            res = 'The ' + func + ' value of the img_name ('+img_name+') is : ' + data_base[img_name][func]
            return render_template('Statistics.html', value=res)
    # this code pulls the requested image by its name from the url and transfer it to a numpy array
    # if the image name is wrong or not exist in the Cloud Storage Bucket, return 404 error
    url = 'https://storage.googleapis.com/seetree-demo-open/' + img_name
    response = requests.get(url, stream=True).raw
    try:
        img = Image.open(response)
    except Exception as e:
        return "<h1>404 Error</h1> The requested url was not found on this server : <B>Bad img_name file name!</B>"
    arr = np.array(img)
    # this code checks what is the requested function and calculate the result
    # if the function name is wrong or not exist, return 404 error
    percent = func[1:]
    if func == 'min':
        calc = str(np.min(arr))
        res = 'The minimum value of the img_name ('+img_name+') is : ' + calc
    elif func == 'max':
        calc = str(np.max(arr))
        res = 'The maximum value of the img_name ('+img_name+') is : ' + calc
    elif func == 'mean':
        calc = str(np.mean(arr))
        res = 'The mean value of the img_name ('+img_name+') is : ' + calc
    elif func == 'median':
        calc = str(np.median(arr))
        res = 'The median value of the img_name ('+img_name+') is : ' + calc
    elif func[0] == 'p' and percent.isnumeric() and int(percent) in range(0, 101):
        calc = str(np.percentile(arr, int(percent)))
        res = 'The ' + str(percent) + '% percentile value of the img_name ('+img_name+') is : ' + calc
    else:
        return '<h1>404 Error</h1>  The requested url was not found on this server : <B>Bad function name!</B>'
    # this code adds the new requested image or function to the data_base
    if img_name not in data_base:
        data_base.update({img_name: {func: calc}})
    elif func not in data_base[img_name]:
        data_base[img_name].update({func: calc})
    print(data_base)
    return render_template('Statistics.html', value=res)


app.run(host='0.0.0.0', debug=True)
