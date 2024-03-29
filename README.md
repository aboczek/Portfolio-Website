# Portfolio Website for myself! 

Welcome to my Portfolio project, it is about my coding story with information about me, my projects and my story.

<img src="docs/amiresponsive.png" alt="am i responsive image" width="900">

## Table of content:

- [Motivation](#motivation)
- [User Experience](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Website Goals](#website-goals)
    - [Requirements](#requirements)
    - [Expectations](#expectations)
    - [Design](#design)
    - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Tablet](#tablet)
        - [Mobile](#mobile)
- [Authentication](#authentication)
- [Data Structure](#data-structure)
- [Website Structure](#website-structure)
- [Technology, Frameworks and Programs used](#technology-frameworks-and-programs-used)
    - [Languages](#languages)
    - [Frameworks and programs used](#frameworks-and-programs-used)
- [Features](#features)
    - [Navigation bar](#navigation)
- [Testing](#testing)
- [Testing user stories](#testing-user-stories)
- [Deployment](#deployment)
- [Credits](#credits)

# Motivation

My motivation for this website is to have my personal portfolio website to put myself out in the tech jobs market.

# User Experience (UX)

## User Stories
- User Story
    - As a user, I want to be able to land on main page.
    - As a user, I want to be able to navigate to About page.
    - As a user, I want to be able to navigate to Projects page.
    - As a user, I want to navigate through website easily.
    - As a user, I want to see projects done by the developer.
    - As a user, I want to be able to visit developer's GitHub.
    - As a user, I want to be able to download CV from Developer.
    - As a user, I want to see where Developer is located.
    - As a user, I want to contact the Developer if I want to message him/her.


## Website Goals

Websites goal is to promote myself as full stack developer and show off my projects and skills I have gained over last few months.

## Agile Methodology

- This project uses Agile methodology with kanban board, each user story is presented as **EPIC** and its smaller issues are **TASKS**

    <details><summary>Picture</summary>
    <img src="docs/agile-kanban.png" alt="kanban board"/>
    </details>
    <br>

## Requirements

- Landing Page.
- About Page.
- Projects showcase page.
- Download CV.

## Expectations

- I expect my website to be easily accessible.
- I expect my website to attract future employers.
- I expect to showcase my projects and skills.

## Design

- Colors
    - Colors used on website are:

        - White #fff:

        <img src="docs/white.png" alt="white" width="10%">

        - Blue #008cff:

        <img src="docs/blue.png" alt="blue" width="10%">

        - Grey #333

        <img src="docs/grey.png" alt="grey" width="10%">

    - Fonts:

    - PT-serif and backup San-serif

        - [PT-serif](https://fonts.google.com/specimen/PT+Serif)

    - Images:

        - Images used from [Pexel image](https://www.pexels.com/photo/hands-typing-on-a-laptop-keyboard-5483077/)


[Back to top](#)

## Wireframes

- Home page.
    <details><summary>Picture</summary>
    <img src="docs/home-page.png" alt="home page"/>
    </details>
    <br>

- About me page.
    <details><summary>Picture</summary>
    <img src="docs/about-me.png" alt="about me page"/>
    </details>
    <br>

- Projects page.
    <details><summary>Picture</summary>
    <img src="docs/projects.png" alt="projects page"/>
    </details>
    <br>

- Frontend admin panel page.
    <details><summary>Picture</summary>
    <img src="docs/front-panel-details.png" alt="front panel details section"/>
    </details>
    <br>
    <details><summary>Picture</summary>
    <img src="docs/front-panel-skills.png" alt="front panel skills section"/>
    </details>
    <br>
    <details><summary>Picture</summary>
    <img src="docs/front-panel-projects.png" alt="front panel projects section"/>
    </details>
    <br>

- Frontend admin panel editing pages.
    <details><summary>Picture</summary>
    <img src="docs/edit-pages.png" alt="front panel editiing pages"/>
    </details>
    <br>

- Hamburger menu.
    <details><summary>Picture</summary>
    <img src="docs/hamburger menu.png" alt="hamburger menu"/>
    </details>
    <br>

# Authentication and Security

- Project uses [Allauth](https://django-allauth.readthedocs.io/en/latest/) for login system, allauth base, login and logout was adjusted and styled.
  Random user wont be able to do anything even if they manage to register, front panel has code to check if user is staff and if not red button in the middle pops up to go back to home page.

- Users cannot register this is **personal** Portfolio Project to use in future.

- The register option exists but all admin functionality is protected by the *is_staff*.

    <details><summary>Login</summary>
    <img src="docs/login.png" alt="login"/>
    </details>
    <br>
    <details><summary>Logout</summary>
    <img src="docs/logout.png" alt="logout"/>
    </details>
    <br>
    <details><summary>if not staff</summary>
    <img src="docs/not-staff.png" alt="not staff"/>
    </details>
    <br>

- Security

    - All secret keys are stored safely in **env.py** for development stages and added to Heroku variables for production release.


# Data Structure

## Database 

- Details:

    | Object | Field |
    |---|---|
    | ID | is automatically generated |
    | full_name | CharField |
    | age | PositiveBigInteger |
    | nationality | Charfield |
    | languages | Charfield |
    | address | CharField |

- Skills:

    | Object | Field |
    |---|---|
    |  ID | is automatically generated |
    | skill | CharField |

- Projects:

    | Object | Field |
    |---|---|
    | ID | is automatically generated |
    | title | CharField |
    | project_link | URLField |
    | project_description | TextField |
    | project_image | CloudinaryField |

    <details><summary>Database structure image here </summary>
    <img src="docs/db-structure.png" alt="database structure" width="400"/>
    </details>
    <br>

- Logic

    <details><summary>Database structure image here</summary>
    <img src="docs/website-logic.png" alt="website logic" width="700"/>
    </details>
    <br>


# Website structure

- Breakpoints were mostly solved with [bootstrap 5](https://getbootstrap.com/docs/5.1/getting-started/introduction/).

- Breakpoints done by me:
    |  Screen size |  from |  | to breakpoint|
    |---|---|---|---|
    |small|>= 320px| medium | <= 768px |

[Back to top](#)

# Technology, Frameworks and Libraries used.

- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

## Frameworks and Libraries used.

- [Django](https://www.djangoproject.com/) Python-based web framework that follows the model–template–views architectural pattern.

- [Heroku](https://www.heroku.com) Deployment of website.

- [ElephantSQL](https://www.elephantsql.com/) Database storing all schemas and data.

- [Cloudinary](https://cloudinary.com/) Image storage.

- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) HTTP server interface.

- [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.

- [Pexels](https://www.pexels.com/) Free pictures, used on home page.

- [Bootstrap](https://getbootstrap.com/) Bootstrap 5 was used in this project.

- [Balsamiq](https://balsamiq.com/) Wireframes.

- [FontAwesome](https://fontawesome.com/) Icons used in this project.

- [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) used to generate new key.

- [Google fonts](https://fonts.google.com/) PT-serif was used.

- [Favicon](https://favicon.io/favicon-generator/) Favicon generator.

# Features

- Responsive on all devices.
- Interactive buttons.
- Custom frontend admin panel.
- Cloudinary picture storage.

## Navigation

- Hamburger menu and footer.
    - large and big tablets.

        <img src="docs/hamburger.png" alt="hamburger menu" width="1000">
        <img src="docs/footer.png" alt="footer" width="1000"> 

    - Small tablets and mobile.

        <img src="docs/hamburger-tablet.png" alt="hamburger menu small devices" width="1000">
        <img src="docs/footer-small.png" alt="footer small device" width="1000">


- Large devices.

    <img src="docs/1.jpg" alt="home page" width="1000">
    <img src="docs/2.png" alt="about me page" width="1000">
    <img src="docs/3.png" alt="projects page" width="1000">

- Tablets.

    <img src="docs/1-tablet.png" alt="home page tablet view" width="700">

    <img src="docs/2-tablet.png" alt="about me page tablet view" width="700">

    <img src="docs/3-tablet.png" alt="projects page tablet view" width="700">

- Small devices and mobile.

    <img src="docs/1-small.png" alt="home page small device view" width="500">
    <img src="docs/2-small.png" alt="about me page small device view" width="500">
    <img src="docs/3-small.png" alt="projects page small device view" width="500">

- Frontend admin panel which only I have access to.
    - large devices.

    <img src="docs/1-front-details.png" alt="front panel details" width="1000">
    <img src="docs/2-front-skills.png" alt="front panel skills" width="1000">
    <img src="docs/3-front-projects.png" alt="front panel projects" width="1000">

    - Tablet and medium devices.

    <img src="docs/4-front-details.png" alt="front panel details" width="700">

    <img src="docs/5-front-skills.png" alt="front panel details" width="700">

    <img src="docs/6-front-projects.png" alt="front panel details" width="700">

- Small devices dont scale nicely on frontend admin panel no pictures to be added.

# Testing

1. W3C HTML Validator, CSS Validator, CI Pylinter and jQuery JShint.

- HTML
    - All pages visible for user works.

    <img src="docs/index-validator.png" alt="html validator" width="700">

    - Error with width and height for index page image, and loading time is justified. Image is loaded from cloudinary and bootstrap is sizing it for me.

    <img src="docs/index-errors.png" alt="error index page" width="">

    - Frontend admin panel has warnings about exceeding columns, i have it justified content is rendered in it from database and django autofills them,
     and external user doesnt see it at all. Talked with tutor and he said he cant see any issue with it and that I could flag it as a bug that browser is filling missing or adding extra tags to it. 
<br>
    <img src="docs/warnings-table.png" alt="front panel validator warnings" width="700">

- CSS 

    <img src="docs/cssvalidator.png" alt="css validator" width="700">


- Python3

    forms:

    <img src="docs/forms-py-validator.png" alt="forms pylinter" width="900">

    models:

    <img src="docs/models-pylint.png" alt="models pylinter" width="900">

    views:

    <img src="docs/views-pylint.png" alt="views pylinter" width="900">

- JavaScript

    <img src="docs/js-linting.png" alt="javascript linting">

2. Testing on website.

- Lighthouse:

    - Desktop

        <img src="docs/desktop-lighthouse.png" alt="light house score on desktop">

    - Mobile

        <img src="docs/mobile-lighthouse.png" alt="light house score on desktop">

3. Testing on portable devices.


    I have tested it on my OnePlus phone and in Developer tools. Everything seemed nice.

    Tested more devices two as an example.

    <img src="docs/testing-mobile.png" alt="testing mobile">

    <img src="docs/testing-tablet.png" alt="testing tablet">

4. Automated testing done by me all passing except URLS showing that imports are not tested.

- To run testing you need to comment out postgres database and uncomment sqlite code in settings, like in the picture in spoiler below.
<details><summary>How settings should look</summary>
    <img src="docs/manual-testing/db-test.png" alt="views testing"/>
    </details>
    <br>

then run this command:

    ```
    python3 manage.py test
    ```

- Views automatic testing:

    <details><summary>views.py testing</summary>
    <img src="docs/views-py-image.png" alt="views testing"/>
    </details>
    <br>

- Forms automatic testing:

    <details><summary>forms.py testing</summary>
    <img src="docs/forms-py-image.png" alt="forms testing"/>
    </details>
    <br>

- Models automatic testing:

    <details><summary>models.py testing</summary>
    <img src="docs/models-py-image.png" alt="models testing"/>
    </details>
    <br>

- Coverage:

    <details><summary>coverage</summary>
    <img src="docs/coverage-html.png" alt="coverage"/>
    </details>
    <br>

- URLS not tested shows to test imports?:

    <details><summary>coverage urls</summary>
    <img src="docs/coverage-html-urls.png" alt="coverage urls"/>
    </details>
    <br>

5. Manual testing.

 - Manual testing was done only on data change notifications if Data was created, edited or deleted.


    <details><summary>Login Notification</summary>
    <img src="docs/manual-testing/login-notification.png" alt="login"/>
    </details>
    <br>
    <details><summary>Details created</summary>
    <img src="docs/manual-testing/create-detail.png" alt="create detail"/>
    </details>
    <br>
    <details><summary>Details edited</summary>
    <img src="docs/manual-testing/detail-edit.png" alt="edit detail"/>
    </details>
    <br>
    <details><summary>Project created</summary>
    <img src="docs/manual-testing/project-created.png" alt="create project"/>
    </details>
    <br>
    <details><summary>Project edited</summary>
    <img src="docs/manual-testing/project-created.png" alt="edited project"/>
    </details>
    <br>
    <details><summary>Project deleted</summary>
    <img src="docs/manual-testing/project-created.png" alt="deleted project"/>
    </details>
    <br>
    <details><summary>Skill created</summary>
    <img src="docs/manual-testing/Skills-created.png" alt="Create skill"/>
    </details>
    <br>
    <details><summary>Skill edited</summary>
    <img src="docs/manual-testing/skill-edited.png" alt="edited skill"/>
    </details>
    <br>
    <details><summary>Skill deleted</summary>
    <img src="docs/manual-testing/skills-deleted.png" alt="deleted skill"/>
    </details>
    <br>

    


6. Known bugs.
- ISSUE: [#75](https://github.com/aboczek/Portfolio-Website/issues/75)
Frontend admin panel, delete details doesnt work. Its a minor bug, details shouldnt be deleted just created and edited if necessary. Full CRUD works for rest of the functions. Code exists but says: 
```
Not Found The requested resource was not found on this server.
```
- ISSUE: [#74](https://github.com/aboczek/Portfolio-Website/issues/74)
Frontend admin panel, buttons in project preview grow with table depending of length of description.

7. Bugs Fixed.

- ISSUE: [#76](https://github.com/aboczek/Portfolio-Website/issues/76)
CV needed download as attribute in html files, that solved the issue.

- ISSUE: [#73](https://github.com/aboczek/Portfolio-Website/issues/73)
Frontend admin panel, unauthenticated return button was fixed by nesting **a** tag in a **div** and moving **id redirection** to **div**, then adding bootstrap class **btn** to it.

- ISSUE: [#42](https://github.com/aboczek/Portfolio-Website/issues/42)
Images wouldnt upload after adding more code to views.

- ISSUE: [#75](https://github.com/aboczek/Portfolio-Website/issues/75)
Frontend admin panel, delete details doesnt work. Fixed by changing url from *"edit-delete"* to *"delete-detail"* as it should be.
```
Not Found The requested resource was not found on this server.
```

<details><summary>Delete details</summary>
<img src="docs/delete-function-fix.png" alt="return button"/>
</details>
<br>

<details><summary>Button</summary>
<img src="docs/return-button.png" alt="return button"/>
</details>
<br>

- Images fix was adding "request.File" to edit and create functions and "enctype="multipart/form-data" to front-panel.html create form and edit-project.html.
<details><summary>Edit project view</summary>
<img src="docs/edit-project.png" alt="edit project view"/>
</details>
<br>
<details><summary>Create project view</summary>
<img src="docs/create-project.png" alt="create project view"/>
</details>
<br>
<details><summary>Create project form</summary>
<img src="docs/edit-project-form.png" alt="create project form"/>
</details>
<br>
<details><summary>Edit project form</summary>
<img src="docs/edit-project-form.png" alt="edit project form"/>
</details>
<br>

# Testing user stories

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to be able to land on main page | Type in websites address | Website will load and go to main page | PASS |
<details><summary>Picture</summary>
<img src="docs/1.jpg" alt="home page"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to be able to navigate to about page | While being on home page, click hamburger menu and press **about me** button | By pressing **about me** button, it will lead you to about me page with details and skills | PASS |
<details><summary>Picture</summary>
<img src="docs/2.png" alt="about me page"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to be able to navigate to projects pages | Click on hamburger menu and press **projects** | By pressing **projects** button it will lead you to projects preview page. | PASS |
<details><summary>Picture</summary>
<img src="docs/3.png" alt="projects preview page"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to navigate through website easily | Press hamburger menu and select any button | By selecting buttons it will lead you to pages accordingly to what you pressed | PASS |
<details><summary>Picture</summary>
<img src="docs/hamburger.png" alt="hamburger menu"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to see projects done by the developer | Press hamburger menu and click **projects** | By selecting **projects** buton it will lead you to projects preview, where you can preview them and open any you want that will lead you to GitHub repository | PASS |
<details><summary>Picture</summary>
<img src="docs/3.png" alt="projects preview page"/>
</details>
<br>
<details><summary>Picture of repo as example</summary>
<img src="docs/github-repo-example.png" alt="github repo"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to be able to visit developer's GitHub | Press GitHub icon in **footer** or open **projects** page and click on a link | By selecting any of those, it will lead you to GitHub profile or repository | PASS |
<details><summary>Picture</summary>
<img src="docs/github-1.png" alt="home page pointing at footer"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/github-2.png" alt="projects preview pointing at link"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to be able to download CV from developer | In footer or hamburger menu press **Download** Icon or **CV** button | By pressing those buttons it will download/open my CV for you| PASS |
<details><summary>Picture</summary>
<img src="docs/cv-download-1.png" alt="cv download"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/cv-download-2.png" alt="cv download"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to see where Developer is located | Press **about me** page on hamburger menu | About me page tells where developer is located | PASS |
<details><summary>Picture</summary>
<img src="docs/located.png" alt="about me location"/>
</details>
<br>

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| As a user, I want to contact the Developer if I want to message him/her | In **footer** or **CV** there is email provided or email function that will open email draf for you | User gets my email or email inbox opens up with window open to send an email | PASS |
<details><summary>Picture</summary>
<img src="docs/email-1.png" alt="email footer"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/email-2.png" alt="email cv"/>
</details>
<br>

# Deployment

## Programs needed:


### Cloudinary

- Create an account [here](https://cloudinary.com/).
- Login and let them chose for you in first window. Then go to dash board and kopy API Key.
<details><summary>Picture</summary>
<img src="docs/deployment/cloudianry-1.png" alt="cloudinary"/>
<img src="docs/deployment/cloudianry-2.png" alt="cloudinary"/>
</details>
<br>


### Heroku

- Create an account [here](https://www.heroku.com/) it will be used later.

### GitHub

- Login to your [GitHub](https://github.com/)

OR

- Create an account [GitHub](https://github.com/) it will be used later.


### ElephantSQL

- Create an account [here](https://www.elephantsql.com/).
- Login, create database and copy data base URL.
<details><summary>Picture</summary>
<img src="docs/deployment/7.png" alt="create database"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/8.png" alt="create database"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/9.png" alt="create database"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/10.png" alt="create database"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/11.png" alt="create database"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/12.png" alt="create database"/>
</details>
<br>

## Local Development

1. Go to Github repo [here](https://github.com/aboczek/Portfolio-Website) press **< CODE >** button, and press **COPY**.
<details><summary>Picture</summary>
<img src="docs/deployment/1.png" alt="deployment github"/>
</details>
<br>

OR **FORK** my repo [here](https://github.com/aboczek/Portfolio-Website) and **CLONE IT**
<details><summary>Picture</summary>
<img src="docs/fork.png" alt="deployment github"/>
<img src="docs/fork-2.png" alt="deployment github"/>
</details>
<br>

- If u copied the link to clone go to **step 3** and instead of link provided there use the link you have copied from your fork.

2. Go to your github repositories and create new repo, call it whatever you like. Press Create Repository it will lead you to another page, and press Gitpod it should open workspace for you. **If you use VSCODE on your PC just open new workspace**

<details><summary>Picture</summary>
<img src="docs/deployment/2.png" alt="deployment github"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/3.png" alt="deployment github"/>
</details>
<br>
<details><summary>Picture</summary>
<img src="docs/deployment/4.png" alt="deployment github"/>
</details>
<br>

3. When Gitpod or VSCODE is open, type in git bash following "git clone https://github.com/aboczek/Portfolio-Website.git" without quotation marks, and press enter. It will clone my repository, if you are looking for better explanation go to this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=desktop&platform=linux)
<details><summary>Picture</summary>
<img src="docs/deployment/5.png" alt="deployment github"/>
</details>
<br>

4. When everything is downloaded select all files and drag it outside of the folder in root directory(main folder), then delete **Portfolio website** folder. Should look like this.
<details><summary>Picture</summary>
<img src="docs/deployment/6.png" alt="deployment github"/>
</details>
<br>

5. Now you need to download all libraries and frameworks im using in this project.
```
pip3 install -r requirements.txt
```

6. Create **env.py** in main folder and add cloudinary api key, elephantSQL and your own secret key. Should look like below. (IF you name the **env.py** file wrong your password will be leaked to your repo.)
```
os.environ['DATABASE_URL'] = " url from elephantsql"
os.environ['SECRET_KEY'] = "secret_key"
os.environ['CLOUDINARY_URL'] = "api key from, remove 'CLOUDINARY_URL=' FROM BEGINING"
```
<details><summary>should look like this</summary>
<img src="docs/deployment/13.png" alt="deployment github"/>
</details>
<br>

7. After everything matches in previous step, we type in this command into terminal, this will migrate all models to database.
```
python3 manage.py migrate
```
<details><summary>should look like this</summary>
<img src="docs/deployment/14.png" alt="deployment github"/>
</details>
<br>

8. Now when its done we type in, this command to make superuser for admin panel. It will ask us for user name, email which is not required and password.
(i have error in red just because i made similar password to username, for your deployment dont do this)

```
python3 manage.py createsuperuser
```
<details><summary>should look like this</summary>
<img src="docs/deployment/15.png" alt="deployment github"/>
</details>
<br>

9. Go to adam_portfolio folder and open **settings.py** and add this code to **ALLOWED_HOST**
```
.herokuapp.com, localhost
```
<details><summary>should look like this</summary>
<img src="docs/deployment/host.png" alt="deployment github"/>
</details>
<br>


10. Now we push our code to GitHub, with:
```
git add .
git commit -m "your own commit"
git push
```

11. Now we go to [Heroku](https://www.heroku.com/) and login, then we create new app as follows on pictures. Pick your own name for it and server closer to you.
<details><summary>should look like this</summary>
<img src="docs/deployment/heroku-1.png" alt="deployment heroku"/>
<img src="docs/deployment/heroku-2.png" alt="deployment heroku"/>
</details>
<br>

12. Then we add our variables into Heroku as follows.
```
DATABASE_URL - url as in envy.py
SECRET_KEY - your secret key
CLOUDINARY_URL - API key as in eny.py
```
<details><summary>should look like this</summary>
<img src="docs/deployment/heroku-3.png" alt="deployment heroku"/>
</details>
<br>

13. Now we go to deploy tab, connect our Github repo to heroku and press Deploy button is going to be grey, we have it pressed already here.
<details><summary>should look like this</summary>
<img src="docs/deployment/heroku-4.png" alt="deployment heroku"/>
<img src="docs/deployment/heroku-5.png" alt="deployment heroku"/>
</details>
<br>

14. When everything is deployed, press **View** button and website will open.
<details><summary>should look like this</summary>
<img src="docs/deployment/heroku-6.png" alt="deployment heroku"/>
<img src="docs/deployment/heroku-7.jpg" alt="deployment heroku"/>
</details>
<br>

15. Now in address bar type in after our website url **/accounts/login** and input your superuser password. If everything works you should see frontend admin panel.
```
https://pp4-deployment.herokuapp.com/accounts/login/
```
<details><summary>should look like this</summary>
<img src="docs/deployment/live-1.png" alt="deployment heroku"/>
<img src="docs/deployment/live-2.png" alt="deployment heroku"/>
</details>
<br>

16. Now enjoy your new project, and fill it in with your data.

# Credits:

- Slack Community and my Mentor!
- Tutor Support.
- [Simen Daehlin](https://github.com/Eventyret) My Mentor very Helpfull!.
- [Pexels](https://www.pexels.com/) images.
- [The W3C Markup Validation Service](https://validator.w3.org/) Validation of HTML.
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Validation of CSS.
- [Autoprefixer](https://autoprefixer.github.io/) used to prefix CSS.
- [Colorhexa](https://www.colorhexa.com/) was used to take colors from for readme.
- [Sam Timmins](https://github.com/sam-timmins/swanbourne_village_stores) getting an idea from his deployment but done it my way.

