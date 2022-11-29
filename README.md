# Admin Features
Add details regarding venue, date, time, speakers, number of tickets. 
Change the status of a registration to Hold/Cancelled/Confirmed/Registered.

# User Features
User can register for the conference, and user will be notified via email regarding the registration and status of registration.
When a registration is cancelled, user under hold will be automatically given status as 'registered'.
Once a registration is cancelled, user with status 'hold' position will be automatically assigned status as 'registered'.

# Database Model
![Database Model](https://github.com/devbk007/conference_web_application/blob/master/Conference.png?raw=true)

# Steps to install application
1. Create a virtual enviroment
    If using conda , install using the command 
    
    ```
    conda create --prefix ./envs
    ```

2. Activate virtual environment
    ```
    conda activate ./envs
    ```

3. Install following packages
    ```
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    
    pip install -r requirements.txt
    ```

4. Create a project, in Google accounts, setup OAuth consent screen and create an OAuthID. 
    [![Watch the video for step by step setup]](https://youtu.be/6bzzpda63H0)   

5. Add a test user in the OAuth consent screen with the required email id.
6. Enable Gmail API.
7. Download the credentials as Json file and save as client_secret.json in conference/webpage/email_api/ directory.
8. Perform migrations.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
9. Create a superuser
     ```
    python manage.py createsuperuser
    ```
  
10. Run the command 
    ```
    python manage.py runserver
    ```
    A prompt screen will appear, if running for the first time. Configure by using the test user email id given in step 5.

11. If "No such table " error happens, run the following command
     ```
    python manage.py migrate --run-syncdb
    ```

#### Tip
If refresh error occur, then delete the token files and rerun.

# Demo Video
[![Video Thumbnail](https://github.com/devbk007/conference_web_application/blob/master/ytube_thumbnail.png)](https://youtu.be/d0Aof4ypAqI)
