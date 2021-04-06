<h2>How to run this web app in local machine.</h2>

- Step 1: Install virtualenv and create new virtual environtment for new project</br>
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/</br>
make sure that you use python with version > 3.6 in virtual environment by run this command <i>"virtualenv -p python3 \<project environment\>"</i></br>

- Step 2: Install packages using pip from requirements.txt</br>
run this command : <i>"pip install -r /path/to/requirements.txt"</i></br>

- Step 3: Access virtual environment</br>
run this command : <i>"source \<project environment\>/bin/activate"</i></br>

- Step 4: Define environment variables</br>
run this command : <i>"nano ~/.bash_profile"</i> to open file bash that contain environment variables</br>
add necessary evironment variables:</br>
export SECRET_KEY="47e2415487126kgnau995ef54290669a4241aa"</br>
export DEBUG_VALUE="True"</br>
export EMAIL_HOST_USER='youremail@gmail.com'</br>
export EMAIL_HOST_PASSWORD='your app password'</br>

<b>Note:</b></br>
Generate secret key by python secrets module.</br>
Follow this link to register email app password: https://support.google.com/mail/answer/185833?hl=en-GB</br>

- Step 5: Apply environment variables to our virtual environment</br>
run this command : <i>"source ~/.bash_profile"</i></br>

- Step 6: Migrate our database change</br>
run those command :</br>
<i>"cd django_project"</i></br>
<i>"python manage.py migrate"</i></br>

- Step 7: Run our web app</br>
<i>"python manage.py runserver"</i></br>

<h2>How to deploy this web app using Heroku service.</h2>

- Step 1: Follow this tutorial to register AWS S3 for File Uploads.</br>
Because Heroku do not have file system for us to store upload file from user. So that's why we have to store it in AWS S3</br>
https://www.youtube.com/watch?v=kt3ZtW9MXhw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17

- Step 2: Deploy this web app using Heroku service.</br>
https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17

<b>Note:</b>
- Setting environment variables: After modify <i>~/.bash_profile</i> you need to run <i>"source ~/.bash_profile"</i>
