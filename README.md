<h2>How to run this web app in local machine.</h2>

- Step 1: Install virtualenv and create new virtual environtment for new project</br>
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/</br>
make sure that you use python with version > 3.6 in virtual environment by run this command <i>"virtualenv -p python3 \<project environment\>"</i></br>

- Step 2: Install packages using pip from requirements.txt</br>
run this command : <i>"pip install -r /path/to/requirements.txt"</i></br>

- Step 3: Access virtual environment and run the web app</br>
run following command : </br>
<i>"source \<project environment\>/bin/activate"</i> to access virtual environment</br>
<i>"cd django_project"</i></br>
<i>"python manage.py runserver"</i> to run our web app</br>

<h2>How to deploy this web app using Heroku service.</h2>

- Step 1: Follow this tutorial to register AWS S3 for File Uploads.</br>
Because Heroku do not have file system for us to store upload file from user. So that's why we have to store it in AWS S3</br>
https://www.youtube.com/watch?v=kt3ZtW9MXhw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17

- Step 2: Deploy this web app using Heroku service.</br>
https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17

<b>Note:</b>
- Setting environment variables: After modify <i>~/.bash_profile</i> you need to run <i>"source ~/.bash_profile"</i>
