import requests
from flask import Flask
import numpy as np
from PIL import Image


app = Flask(__name__)


@app.route('/health')
def default():
    return '<h1>OK!</h1>'


@app.route('/stats/<img_name>/<func>', methods=['GET'])
def statistics(img_name, func):

    url = 'https://storage.googleapis.com/seetree-demo-open/' + img_name
    response = requests.get(url, stream=True).raw
    try:
        img = Image.open(response)
    except Exception as e:
        return "<h1>404 Error</h1> The requested url was not found on this server : <B>Bad img_name file name!</B>"
    arr = np.array(img)
    percent = func[1:]
    if func == 'min':
        return '<h2>The minimum value of the img_name ('+img_name+') is : ' + str(np.min(arr)) + '</h2>'
    elif func == 'max':
        return '<h2>The maximum value of the img_name ('+img_name+') is : ' + str(np.max(arr)) + '</h2>'
    elif func == 'mean':
        return '<h2>The mean value of the img_name ('+img_name+') is : ' + str(np.mean(arr)) + '</h2>'
    elif func == 'median':
        return '<h2>The median value of the img_name ('+img_name+') is : ' + str(np.median(arr)) + '</h2>'
    elif func[0] == 'p' and percent.isnumeric() and int(percent) in range(0, 101):
        result = str(np.percentile(arr, int(percent)))
        return '<h2>The ' + str(percent) + '% percentile value of the img_name ('+img_name+') is : ' + result + '</h2>'
    else:
        return '<h1>404 Error</h1>  The requested url was not found on this server : <B>Bad function name!</B>'


app.run(host='0.0.0.0', debug=True)
