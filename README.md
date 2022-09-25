# capstone

## authentication

using [all authentication](https://django-allauth.readthedocs.io/en/latest/installation.html) for the login and log out sysytem

### how to run the webapp

- Create a new folder
- Open terminal in new folder
- pip install virtualenv
- virtualenv venv
- venv\Scripts\activate
- git clone https://github.com/auscode/capstone
- cd capstone
- pip3 install -r requirements.txt
- python manage.py runserver

### layoutpage

this page contains the layout of the website it conatins the features of the navbar and the footer of the page itself.

The navabr contains the image(logo) of the website and it also contains the sign-in buttton if you are not logged in it changes as you sign-in to logout at the exact position of the sign-in button.

Footer contains only the required things like the rights reservation and from where it is inspired from and my name & github usernmae.

### index and create profile page

User interface of the netflix clone page to get idea of what you can do and what this website is providing to you.
for ex. you can create profiles for kids & Adults who can access diffrent videos(contents) according to the profile you have selected.

### movielist

In this page i've created a card it contains the image of the movie or series you want to feature and its description contains a little info about the movie or series.

Just below the card there is a video section there is a list of the movies you can watch it by clicking on the thumbnail of the movie.

# Distinctiveness and Complexity

...
Authentication Backend

in this webapp i've used the all-authenticcation system provided django-python where you zhave to install the library and set it up in the settings to use it.

I used it because i want to try other authentication system insted of writing their views again and again each time and suppose if i've to use googele, facebook, twitter etc. for login i've to learn and it and also learn how to make views for that which is more work by using all-auth i just have to add specify in the settings file to set it up, so i learn how to apply them in the last project.
....
....
Uploading

In all of our last project we basically provided link of the images or we use the image form the google service to show on our website.

But in this project i've provided the admin interface where a admin can add the movie(video) stored in their local device to the online sort of like YouTube and this video got stored in the media folder of the webpage and they can also provide Covers and the description of the movie(video).

So thats how it is different from the previous projects because in the previous projects i did not worked with videos and uploading them.

I did this because I wanted to create a webapp where admin can upload the vidoes directly from their device insted of going through various links and share it here so we can embed it and then stream it.

....
....
Profiles

In our proevius projects i did not create the profile section where i can segregate the profile based on their data like adult and kids.

I did this because thats how you would like to create the video platform where you can achieve variuos age group without having any conflict over any of that adult and kids stuff mixing altogether.
....
