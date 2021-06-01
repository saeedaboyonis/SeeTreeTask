## Image Statistics Features Application 


In this web application we will handle calculation of image statistics, the images are stored in a Cloud Storage Bucket, in order to read files from the bucket we send a GET request to: https://storage.googleapis.com/seetree-demo-open/FILE_NAME.  

For example you can try opening https://storage.googleapis.com/seetree-demo-open/IMG_1.jpg in your browser.

Supported statistics functions are:
<br/><br/>
**i.** min: computes the minimum of image pixel values
<br/>
**ii.** max: computes the maximum of image pixel values
<br/>
**iii.** mean: computes the mean/average of image pixel values
<br/>
**iv.** median: computes the median/middle of image pixel values
<br/>
**v.** pXXX: where XXX is a percentile between 0...100. For example p10 is the 10th percentile of the image, p99 is the 99th percentile
 ## Prerequisites

You should have the following items on your system:


**1)-** Docker: The application tested with Docker Desktop for Windows 


**2)-** Command line tool: The application tested with Ubuntu 18.04 LTS


**3)-** Flask: You can download with `apt install python3-flask`


**4)-** Python: The application tested with Python3

## Setup the files 
*  Git all the files to a directory in your system.

   `git clone https://github.com/saeedaboyonis/SeeTreeTask.git`

* Navigate to this directory with command line tool.

    `cd /the_directory_path/`
* Start the application with one of the following ways.
## Starting application locally with flask

* Run the project in flask with these commands :


    `export FLASK_APP=main.py`
     </br>
     `flask run`
     
* Navigate to this url in your browser:
   </br>
http://localhost:5000/

 
## Starting application locally with Docker

* Run the project in docker with these commands :


    `docker build -t main .`
     </br>
     `docker run -id -p 5000:5000 -t main`
     
* Navigate to this url in your browser:
   </br>
http://localhost:5000/

## Starting application locally with Docker-Compose
* Run the project in docker-compose with this command :


    `docker-compose up`
     
* Navigate to this url in your browser:
   </br>
http://localhost:5000/
