# Multilingual Rasa Chatbot that works as a simple F.A.Q for CNSS (Moroccan National Social Security Fund) users in Arabic and French.


## Table of contents
* [General info](#general-info)

* [Technologies](#Technologies)

* [Setup](#setup)

* [Demo](#Demo)

## General info
The idea behind the project is to create a simple multilingual chatbot to answer some basic questions from the Moroccan National Social Security Fund users, the languages supported are : Arabic and French.

## Technologies

Project is created with:
* Rasa 3.0.5
* Visual Studio Code

## Setup 

To run this project locally follow the steps below : 

1- Clone the repo.

2- Detailed walkthrough on how to install the tools needed to run the project : https://www.youtube.com/watch?v=RVoFqxmG8p0

3- Once everything is installed enter the following commands on the anaconda prompt while being positioned in the project's folder: 

``` 
$ conda activate nameofvirtualenv
$ rasa data validate 
$ rasa train --fixed-model-name cnss_chatbot_ml"
$ rasa run -p 5007 -m models --enable-api --cors "*" --debug

```
4- On a different anaconda prompt terminal enter the following command to activate actions : $ rasa run actions

5- Open the index.html file in the "Rasa Webchat interface ML" folder, you should have a page with the chatbot widget on the bottom right corner.

## Demo 

![alt text](https://user-images.githubusercontent.com/16072777/185400182-01c5d275-ce80-4424-a6c4-9fdad6cfa8b7.PNG)


