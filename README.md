# Image-Classification-Football-Player-Similarity

### Overview
This data science and machine learning project aims to classify images and determine which player they resemble the most. The player list is limited to only 5 players:
* Lionel Messi.
*	Cristiano Ronaldo. 
*	Ryad Mahrez.
*	Erling Haaland.
*	Kylian Mbappe.

The project starts with data collection, where images of each player has been gathered from various sources. Next, the images will be cleaned and processed to prepare them for machine learning model training.
The machine learning model training use two different domains, the space domain (normal colorful image) and the wavelet domain to capture different aspects of the images. 

After that the hyperparameters are tested and different machine learning algorithms are tested in order to determine the best performing model. Once the best model is selected, it will be exported to be exploited by our server later on.
After that we build a Python Flask Server that provide an API that can be accessed by the website that we will build using HTML, CSS, and JavaScript.
Users will be able to upload an image and the server will classify the image and return the player it most closely resembles, along with the percentage of similarity.

### Folder Structure:
*	SERVER & UI: contains the Python Flask Server and the HTML, CSS and JavaScript code for the website
*	Artifacts: contain the machine learning model artifacts
*	model: Contains python notebook for model building
*	dataset: Dataset used for our model training

### Technologies used in this project:
*	Python
* Machine Learning
*	Numpy and OpenCV for data cleaning
*	Matplotlib for data visualization
*	Sklearn for model building
*	Jupyter notebook, visual studio code as IDE
*	Python flask for http server
*	HTML/CSS/Javascript for UI

![screenshot](/Snapshoot.PNG)


