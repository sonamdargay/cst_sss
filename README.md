Repository Details:
----------------------------------------------
Created by: Sonam Dargay
<pre>
Collaborators: 
        1. Karma Samdrup
        2. Rinchen
        3. Suraj Mukhia
        4. Tawmo
</pre> 

Project Background:
----------------------------------------------
The security cameras installed in various places capture video footage. However the                 footage is automatically deleted after a certain period of time from the server due to limited storage capacity. Taking the scenario of College of Science and Technology (CST), with the current security system it is difficult to verify whether the person entering through the gate is an authorized individual or an intruder. It also requires human labor (security guards) to monitor and guard. It is also seen that guards tend to slack off on their duty usually falling asleep or not being diligently present on their post. This is one of the major setback in the current security system which can be easily taken advantage of by intruders.

Repo Info
---------------------------------------------
Git Branch for Graphical User Interface(GUI): <b>feature-gui</b>


Repo Structure
---------------------------------------------
<b>1. +cascades: for storing haar cascades
2. +dataset: for storing dataset
3. +trainer: for storing trainer.yml
4. +gui: for gui branch
5. --cst_ss_db: for database storage
6. -dataset.py: for creating dataset
7. -trainer.py: trainer code
8. -recogniser.py: recognise code</b>

Commands
----------------------------------------------
1. Create virtual environment by installing virtualenv
a. Instalation: 
<pre>       
        i. Linux: 
                #python3 -m pip install --user virtualenv
        ii. windows: 
                #py -m pip install --user virtualenv 
</pre> 
b. Create virtual env:
<pre> 
        i. Linux: 
                #python3 -m virtualenv env
        ii. windows: 
                #py -m virtualenv env
</pre> 
2. Installing mysql:
<pre>
        #python -m pip install mysql-connector
</pre> 
3. Installing tkinter
<pre> 
        #sudo apt-get install python3-tk
        or
        #sudo apt-get install python3-tkinter
</pre> 

Errors Solutions
-----------------------------------------------------
For Error
<pre>
Traceback (most recent call last):
File ".\trainer.py", line 7, in <module>
    recognizer = cv2.face.LBP
AttributeError: module 'cv2.cv2' has no attribute 'face'
</pre>

<b>You need to install opencv-contrib</b>
<pre> 
        #pip install opencv-contrib-python
<pre> 

It should work after that.