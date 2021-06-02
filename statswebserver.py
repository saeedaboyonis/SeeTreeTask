import requests
import time
from flask import Flask, render_template, request, g
import numpy as np
from PIL import Image
from statscalc import stats_calculator


# These are global variables
# DATA_BASE: saves the images names, requested functions and their results to use it for future identical requests
# NUMBER_OF_IMAGES: The number of all images stored in the Cloud Storage Bucket
DATA_BASE = {"image_name": {"min": "0", "max": "0", "mean": "0", "median": "0", "pXXX": "0"}}
NUMBER_OF_IMAGES = 10

app = Flask(__name__)


# The home page route that display all images from the Cloud Storage Bucket
@app.route('/')
def home():
    return render_template('HomePage.html', value=NUMBER_OF_IMAGES+1)


# The function page route that display all functions for the requested image
@app.route('/functions/<img_name>', methods=['GET'])
def functions(img_name):
    return render_template('Functions.html', img_name=img_name)


@app.route('/health')
def default():
    return render_template('Health.html')


# The Statistics page route that display the requested function result for an image
@app.route('/stats/<img_name>/<func>', methods=['GET'])
def stats(img_name, func):
    # this code checks if the requested function result already stored in DATA_BASE
    if img_name in DATA_BASE:
        if func in DATA_BASE[img_name]:
            res = 'The ' + func + ' value of the image ('+img_name+') is : ' + DATA_BASE[img_name][func]
            return render_template('Statistics.html', value=res, img_name=img_name)
    # this code pulls the requested image by its name from the url
    # if the image name is wrong or not exist in the Cloud Storage Bucket, return 404 error
    url = 'https://storage.googleapis.com/seetree-demo-open/' + img_name
    response = requests.get(url, stream=True).raw
    try:
        img = Image.open(response)
    except Exception as e:
        return render_template('Error.html', msg='Bad image file name!')
    # convert the image from RGB to grayscale mode
    img = img.convert('L')
    # convert the image to a numpy array
    arr = np.array(img)
    # call stats_calculator to calculate the requested function
    res = stats_calculator(func, img_name, arr)
    # if the function name is wrong or not exist, return 404 error
    if str(res[1]) == "none":
        return render_template('Error.html', msg='Bad function name!')
    # this code adds the new requested image or function to the DATA_BASE
    if img_name not in DATA_BASE:
        DATA_BASE.update({img_name: {func: str(res[1])}})
    elif func not in DATA_BASE[img_name]:
        DATA_BASE[img_name].update({func: str(res[1])})

    return render_template('Statistics.html', value=str(res[0]), img_name=img_name)


# This code measure the time that takes to render a template
@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


app.run(host='0.0.0.0', debug=True)
