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

        - [Google fonts](https://fonts.google.com/specimen/PT+Serif)

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

- Front panel page.
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

- Front panel editing pages.
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

- The register option exists but all admin functionality is protected by the **is_staff**.

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

    - All secret keys are stored safely in **envy.py** for development stages and added to Heroku variables for production release.


# Data Structure

## Database 

- Details:
    ```
    id - is automatically generated.

    full_name - CharField

    age - PositiveBigInteger

    nationality - Charfield

    languages - Charfield

    address - CharField
    ```       

- Skills:
    ```
    id - is automatically generated.

    skill - CharField
    ```

- Projects:
    ```
    id - is automatically generated.

    title - CharField

    project_link - URLField

    project_description - TextField

    project_image - CloudinaryField
    ```

    <details><summary>Database structure image</summary>
    <img src="docs/db-structure.png" alt="database structure" width="400"/>
    </details>
    <br>

- Logic

    <details><summary>Database structure image</summary>
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
- Custom front panel.
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

- Front panel which only I have access to.
    - large devices.

    <img src="docs/1-front-details.png" alt="front panel details" width="1000">
    <img src="docs/2-front-skills.png" alt="front panel skills" width="1000">
    <img src="docs/3-front-projects.png" alt="front panel projects" width="1000">

    - Tablet and medium devices.

    <img src="docs/4-front-details.png" alt="front panel details" width="700">

    <img src="docs/5-front-skills.png" alt="front panel details" width="700">

    <img src="docs/6-front-projects.png" alt="front panel details" width="700">

- Small devices dont scale nicely on front panel no pictures to be added.

# Testing

1. W3C HTML Validator, CSS Validator, CI Pylinter.

- HTML
    - All pages visible for user works.

    <img src="docs/index-validator.png" alt="html validator" width="700">

    - Error with width and height for index page image, and loading time is justified. Image is loaded from cloudinary and bootstrap is sizing it for me.

    <img src="docs/index-errors.png" alt="error index page" width="">

    - Front panel has warnings about exceeding columns, i have it justified content is rendered in it from database and django autofills them,
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

5. Known bugs.

- CV doesnt download. (Fixed)
- Images wouldnt upload after adding more code to views. (Fixed)
- Front panel, unauthenticated users return button.(fixed)
- Front panel, buttons in project preview grow after fixing html errors.

6. Bugs Fixed.

- CV needed download as attribute in html files, that solved the issue.

- Front panel, unauthenticated return button was fixed by nesting **a** tag in a **div** and moving **id redirection** to **div**, then adding bootstrap class **btn** to it.

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

**placeholder**

# Credits:

- Slack Community and my Mentor!
- Tutor Support.
- [Simen Daehlin](https://github.com/Eventyret) My Mentor very Helpfull!.
- [Pexels](https://www.pexels.com/) images.
- [The W3C Markup Validation Service](https://validator.w3.org/) Validation of HTML.
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Validation of CSS.
- [Autoprefixer](https://autoprefixer.github.io/) used to prefix CSS.
- [Colorhexa](https://www.colorhexa.com/) was used to take colors from for readme.

