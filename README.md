## Image Statistics Features Application 


In this web application we will handle calculation of image statistics, the images are stored in a Cloud Storage Bucket, in order to read files from the bucket we send a GET request to: https://storage.googleapis.com/seetree-demo-open/FILE_NAME.  

For example you can try opening https://storage.googleapis.com/seetree-demo-open/IMG_1.jpg in your browser.

Supported statistics functions are:
<br/><br/>
**i.** min
<br/>
**ii.** max
<br/>
**iii.** mean
<br/>
**iv.** median
<br/>
**v.** pXXX where XXX is a percentile between 0...100. For example p10 is the 10th percentile of the image, p99 is the 99th percentile
 ## Prerequisites

You should have the following items on your system:


**1)-** Docker.


**2)-** Command line tool.


**3)-** Flask.                           `apt install python3-flask`


## Starting services locally with flask
*  Git all the files to a directory in your system.

* Navigate to this directory with command line tool.

    `cd /the_directory_path/`

* Run the project in flask with these commands :


    `export FLASK_APP=main.py`
     </br>
     `flask run`
     
* Navigate to this url in your browser:
   </br>
http://localhost:5000/

 
## Starting services locally Docker

