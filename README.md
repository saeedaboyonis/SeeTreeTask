## Image Statistics Features Application 


In this web application we will handle calculation of image statistics, the images are stored in a Cloud Storage Bucket, in order to read files from the bucket we send a GET request to: https://storage.googleapis.com/seetree-demo-open/FILE_NAME.  

For example you can try opening https://storage.googleapis.com/seetree-demo-open/IMG_1.jpg in your browser.

Supported statistics functions are:


i. min


ii. max


iii. mean


iv. median


v. pXXX where XXX is a percentile between 0...100. For example p10 is the 10th percentile of the image, p99 is the 99th percentile

## Starting services locally with flask
* Build a Docker image for Spring Pet Clinic:


 `./mvnw compile -Dimage=spetclinic com.google.cloud.tools:jib-maven-plugin:1.0.0:dockerBuild`
* Run Pet Clinic in Kubernetes:


`kubectl apply -f petclinic-deployment`
* Run the folowing command and navigate to localhost:8080 in your browser:


`    kubectl port-forward deployment/petclinic 8080:8080` 
## Starting services locally without Docker

