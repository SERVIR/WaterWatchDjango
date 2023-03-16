# Ferlo Ephemeral Water Body Monitoring Dashboard

This tool lets you select a water body and see the data processed by the Earth Engine collection.


# Required 

* Python 3.9

* Google Service Account and secret key JSON

* Access to the Earth Engine Asset projects/servir-wa/services/ephemeral_water_ferlo/processed_ponds/

# Installation

1. Open a terminal or command prompt on your computer.

2.  Navigate to the directory where you want to clone the repository.

3.  Run the command git clone https://github.com/SERVIR/WaterWatchDjango.git

4.  Press Enter. This will start the cloning process and create a copy of the repository on your computer in the current directory.

5.  After the cloning process is finished, you will find a new directory named WaterWatchDjango. This directory contains the full copy of the repository including all the files and the full git history.

6.  You will need an EE account, if you do not currently have one you can sign up https://earthengine.google.com/signup

7.  Next you will need to create a google cloud project where you will enable EE and Google Authentication for your project. Navigate to https://console.cloud.google.com/projectcreate

8.  Follow the prompts to create the project, you may want to name it Your_Project_Name so you can skip this part when you set up your application.

9.  After you create the project you must select it from the dropdown in the top

10. In the left panel under APIs & Services click the "OAuth consent screen" link, then fill out the form with the information for your application. There are a few pages with choices, proceed when finished.

11. In the left panel click "Credentials" link

12. At the top left click + Create Credentials and select "OAuth 2.0 Client ID"

13. In the dropdown select "Web Application" and give a name.

14. In the App Domain fields use the the dev domains for example:

        http://127.0.0.1:8000/
        http://127.0.0.1:8000/terms-privacy
        http://127.0.0.1:8000/terms-privacy

15. Add Authorized JavaScript origins (you may enable multiple)

        http://localhost:8000
        http://127.0.0.1:8000

16. Add Authorized redirect URIs (you may enable multiple)

        http://localhost:8000/accounts/google/login/callback/
        http://127.0.0.1:8000/accounts/google/login/callback/

17. Copy and save the Client ID and Client secret to your local machine (you will need these later)

18. Click DOWNLOAD JSON and save

19. Click save

20. Click Enabled APIs & Services then click the + Enable APIS AND SERVICES link at the top

21. Search for Earth Engine, click it, then click enable.

22. Click Create Credentials again and select service account

23. Fill out information and click CREATE AND CONTINUE.

24. Click Select a role and scroll to Earth Engine, then select Earth Engine Resource Viewer

25. Register the service account https://signup.earthengine.google.com/#!/service\_accounts

26. Before you can run the application you will need to create a data.json file in the root directory. In this file you will need the following:

        {
          "SECRET\_KEY": "your\_secret\_key",
          "ALLOWED\_HOSTS": \["localhost", "127.0.0.1"\],
          "CSRF\_TRUSTED\_ORIGINS": \["http://localhost:8000","http://127.0.0.1:8000"\],
          "EE_SECRET_KEY" : "your\_json\_key",
          "EE_SERVICE_ACCOUNT" : "your\_service\_acccount",
        }
SECRET_KEY is any random string of characters

ALLOWED_HOSTS is the domain you will be accessing the site from, in development it will be left as is, in production you will remove those and add your actual domain

CSRF_TRUSTED_ORIGINS: similar to above except this needs the http or https protocol added

EE_SECRET_KEY: is the json file you downloaded from the google console

EE_SERVICE_ACCOUNT is the service account you created above

27. Run the command python manage.py runserver

28. Now you can open a browser and navigate to port http://127.0.0.1:8000/ unless you specified a different port in your configuration.

# Contact
Please feel free to contact us if you have any questions.

# Authors
Githika Tondapu (NASA/USRA)
Francisco Delgado (NASA/USRA)
Lance Gilliland (NASA/JACOBS)
Billy Ashmall (NASA/USRA)
Emil Cherrington (NASA/UAH)
Sarva Pulla (former NASA/USRA)
Rebekke Muench (former NASA/UAH)
Kel Markert (former NASA/UAH)
Belal Ba (CSE)
Adama Mamadou (CSE)

# License and Distribution
This application is built and maintained by SERVIR under the terms of the MIT License.

# Privacy & Terms of Use
This applications abides to all of SERVIR's privacy and terms of use as described at https://servirglobal.net/Privacy-Terms-of-Use.

# Disclaimer
The SERVIR Program, NASA and USAID make no express or implied warranty of this application as to the merchantability or fitness for a particular purpose. Neither the US Government nor its contractors shall be liable for special, consequential or incidental damages attributed to this application.