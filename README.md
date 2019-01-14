Repository Details:
----------------------------------------------
Created by: Sonam Dargay
Collaborators: 
        1. Karma Samdrup
        2. Rinchen
        3. Suraj Mukhia
        4. Tawmo

Project Background:
----------------------------------------------
The security cameras installed in various places capture video footage. However the                 footage is automatically deleted after a certain period of time from the server due to limited storage capacity. Taking the scenario of College of Science and Technology (CST), with the current security system it is difficult to verify whether the person entering through the gate is an authorized individual or an intruder. It also requires human labor (security guards) to monitor and guard. It is also seen that guards tend to slack off on their duty usually falling asleep or not being diligently present on their post. This is one of the major setback in the current security system which can be easily taken advantage of by intruders.

Repo Info
---------------------------------------------
Git Branch for Graphical User Interface(GUI): feature-gui


Repo Structure
---------------------------------------------
1. +cascades: for storing haar cascades
2. +dataset: for storing dataset
3. +trainer: for storing trainer.yml
4. -dataset.py: for creating dataset
5. -trainer.py: trainer code
6. -recogniser.py: recognise code

Commands
----------------------------------------------
1. Create virtual environment by installing virtualenv
a. Instalation: 
        i. Linux: #python3 -m pip install --user virtualenv
        ii. windows: #py -m pip install --user virtualenv
b. Create virtual env:
        i. Linux: #python3 -m virtualenv env
        ii. windows: #py -m virtualenv env
2. Installing mysql:
        #python -m pip install mysql-connector
3. Installing tkinter
        #sudo apt-get install python3-tk
        or
        #sudo apt-get install python3-tkinter