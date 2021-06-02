from flask import Flask, render_template, request, g
import numpy as np


# this code checks what is the requested function and calculate the result

def stats_calculator(func, img_name, arr):
    percent = func[1:]
    if func == 'min':
        calc = str(np.min(arr))
        return 'The minimum value of the image (' + img_name + ') is : ' + calc, calc
    elif func == 'max':
        calc = str(np.max(arr))
        return 'The maximum value of the image (' + img_name + ') is : ' + calc, calc
    elif func == 'mean':
        calc = str(np.mean(arr))
        return 'The mean value of the image (' + img_name + ') is : ' + calc, calc
    elif func == 'median':
        calc = str(np.median(arr))
        return 'The median value of the image (' + img_name + ') is : ' + calc, calc
    elif func[0] == 'p' and percent.isnumeric() and int(percent) in range(0, 101):
        calc = str(np.percentile(arr, int(percent)))
        return 'The ' + str(percent) + '% percentile value of the image (' + img_name + ') is : ' + calc, calc
    else:
        return "none", "none"
