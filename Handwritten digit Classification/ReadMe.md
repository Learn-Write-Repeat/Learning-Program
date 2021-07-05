# Handwritten Digit Classification

## Dataset Used: MNIST handwritten digits <br>
The dataset consists of 60,000 examples, where 10,000 have been taken as a test set. The images are grayscale, 28x28 pixels, and centered to reduce preprocessing and the overall time to predict a number.
An example of the dataset can be seen in the image:
![image](https://user-images.githubusercontent.com/60402341/124498244-a4f39280-ddd9-11eb-8253-d7040e9a2fb0.png)


## Tech Stack
1. Python 3+
2. Tensorflow
3. Numpy
4. Keras <br>
The code was written and executed using Google collab. <br>
[Notebook](https://colab.research.google.com/drive/1sI_SnHEjKYihQ3ilU9_o3viRQjUnz_I7?usp=sharing#scrollTo=04WZoANV80iX)

## Introduction
Keras is a high-level neural network API focused on user friendliness, fast prototyping, modularity and extensibility. It works with deep learning frameworks like Tensorflow, 
Theano and CNTK, allowing building and training a neural network without much problem. Using Convolutional Neural Networks (CNN) and a Tensorflow backend, 
handwritten digits were classified. CNN uses multilayer perceptrons to do computational work and relatively little pre-processing compared to 
other image classification algorithms.That is, the network learns through filters that in traditional algorithms were hand-engineered. Hence, for the task of image processing, 
CNNs are the best-suited option.

## Accuracy 
The digits were classified with an accuracy of 92.6% using the CNN, trained using Google Collab.

### Team Members
1. Anushka Dixit
2. Tisha Jhabak
3. Anit Rosalin Paul

### Mentor
Akash Patel
