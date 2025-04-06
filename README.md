step 1: Install all required dependencies and packages
pip insatll django
pip install djangorestframework

pip install pipenv 
pipenv insatll
pipenve shell (these 3 are optional but recommended)

pip install customtkinter
pip insatll requests (these 2 are used for gui)

pip insatll pillow (used for the bg image to appear in gui)

step 2: python manage.py createsuperuser (create a super user to login on the django_admin board)

step 3: Once superuser created run 
python manage.py runserver (this will start the backend)
visit http://127.0.0.1:8000/admin/ and login with your username and password

step 4: Back to terminal run
python frontend.py (this should run the gui)

step 5: If you wish to add your own img as background image just save your image name as "bg_image.jpg"

"I hope you like this and and make changes as you wish, my future idea is to make the gui more better 
and hopefully deploy this so do visit for any updates... See you all Sayonara" -Arnold/KuroiAkuma 
