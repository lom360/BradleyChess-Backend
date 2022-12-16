***************************************************
************ Flask Backend Application ************
***************************************************

Description: This application will work as a backend
that will run the Machine Learning Model. The model
was built using the SARSA algorithm. The training of
the system will be done outside of the application,
but a Q Table will be produced and the application
will use those tables to control the movement of the
agent on the frontend application. The server will
handle API requests and send it to the frontend to
update the Agent's move. The frontend application
can be found at this link: https://www.bradleychess.com.
An API test of this server can be found at this link: 
https://flask-bradley-chess.azurewebsites.net



****************************************************
************ Setting Up The Environment ************
****************************************************

1) Python 3 installation is required for this project.
Please download and install from the link below:
https://www.python.org/downloads/

2) Create a virtual environment so global environment
does not run into stability issue. Run the command below
inside the root directory of the project:

python -m venv virtualfolder

NOTE: virtualfolder could be any name. It is up to you, and
a new folder will be created with that same name after
running the above command.

3) Now it is time to enter the virtual environment.
Inside the same folder where the virtualfolder was
"created", but not inside the actual virtualfolder.
Run the the commands that fits your system:

Windows: virtualfolder\Scripts\activate
Linux/Mac: virtualfolder/bin/activate

4) We should be working in the virtual environment now.
This will prevent any issues to the global environment
when installing packages. Now it's time to install the
required packages. The requirement.txt will help us
with that. Run this command:

pip install -r requirements.txt

5) All required packages should be installed now.



*****************************************************
************** Running The Application **************
*****************************************************

1) To run the application locally on your system.
Run this command:

python server.py

2) Normally the localhost would be running on http://127.0.0.1:5000,
but the console will always list where it is located at. So pay
attention to the messages the console gives after running the
application in case that it is different.

3) This Flask Application acts as a server for the https://www.bradleychess.com/
website. So users will not be concerned with direct interaction 
with this backend application. They will be more concerned with the
frontend application.



******************************************************
****************** Folder Structure ******************
******************************************************

1) The root folder consists of:
	- server.py: runs the application 
	- requirements.txt: installs required packages 
	- Procfile: tells the deployment host which file to run
	- components: contains QTables, routes.py and the ml folder

2) Inside the components folder:
	- QTables: Controls the move of the agent
	- routes.py: contains the routes for API calls
	- ml: folder that contains the classes to train a model