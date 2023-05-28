# pepperGPT

## Table of contents
* [Description](#description)
* [Demostration](#demostration)
* [Technologies](#technologies)
* [Enabling Pepper](#enabling-pepper)
* [Setup](#setup)
* [Licence](#licence)

## Description
I made this project as my final project of junior II module in the RAS Javeriana student group, in this project you will find a node for ros 1 that allows pepper to communicate through ChatGPT api and python SpeechRecognition library.

## Demostration

https://github.com/miguelgonrod/pepperGPT/assets/49737722/b54c8ccd-6c8b-4726-853d-0ff8807e789b

## Technologies
This project is created with:
* python: 3.8.10
* ros: noetic

## Enabling Pepper
To enable pepper topics please refer to this other repo I uploaded in which you can download a fully functional docker with the naoqi packages, the necesary nodes you need to run are:
- bringup
- naoqi driver

Repository link:https://gitlab.com/IEEERASJaveriana/DockersforROS/docker_kinetic_pepper.git 

## Setup
To run this project you need to have enabled pepper topics and have ros installed, you need to install these dependencies:
```
$ sudo apt-get install python3-pip python-pip libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
$ sudo apt install ros-noetic-desktop-full
$ pip install SpeechRecognition
$ pip install pyaudio openai
```

Now you need to clone this repository in your workspace, add your openAI api key and launch it using rosrun:

To append your openAI api key in the scripts/Pepper_GPT.py file you need first to clone the repo with the command below, this api key have to be inside the the double quotation marks at line 8, if you dont know how to get your openAI api key check in this page: https://platform.openai.com/docs/quickstart/build-your-application

```
$ git clone https://github.com/miguelgonrod/pepperGPT.git
$ catkin_make # run this and the next command inside your workspace
$ source devel/setup.bash
$ rosrun pepperGPT Pepper_GPT.py
```
If you are getting a master node error is because you don't have activated the pepper topics with naoqi (this is explained int the [Enabling Pepper](#enabling-pepper) subtitle)

If you want to change the speech recognition language go to scripts, edit the Pepper_GPT.py file and change in the line 34 the language, if ypu want to change the training modify the list in the line 13 and if you want to change the node to publish the message change it in the line 12.

## Licence
pepperGPT is available under the BSD-3-Clause license. See the LICENSE file for more details.
