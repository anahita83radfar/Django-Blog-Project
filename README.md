# Developers Blog

Developers Blog is a website for people and developers who are interested in communicating with each other. The website's goal is to build a community of developers to ask questions, learn, and share technical knowledge. This weblog empowers people to find what they need to develop technology at work or home.

The user of this website will be able to read and write the post, update and delete the post, leave comments on the post, and like the post. Through online registration, users can access their profiles.

 ![Responsive page](/media/images/readme/responsive-ipad.jpg)
  ![Responsive page](/media/images/readme/responsive-mobile.jpg)

# Features

- ## The Home Page

  ![Responsive page](/media/images/readme/home.jpg)

- ### Navigation Bar
  - Featured at the top of the page on all pages. The navigation bar includes links to the Logo, Home page, About page, Register page, Login page, Profile page, and New post page.
  - The logo is the name of the website and by clicking on it the user redirect to the Home page.
  - The navigation makes the different pages of the website easy to find. It is fully responsive and identical on each page to allow for easy navigation without having to revert to the previous page.

  ![Navigation bar](/media/images/readme/nav.jpg)

- ### The Main Section
  - The main section on the Home page is divided into different sections or a list of posts so that each section represents a specific post that is published by the users of the website.
  - Each post section has an image with the post's author name, the title of the post,  excerpt, date of publication, and like's numbers underneath it. The user can access to the post's detail by clicking on the post's title or post excerpt.


  ![The Main section](/media/images/readme/main.jpg)

- ### The Footer
  - The footer section includes the contact links to the relevant social media sites. 
  - The social media links will open to a new tab to allow easy navigation for the user and the encourages user to keep connected via social media.

  ![The Footer](/media/images/readme/footer.jpg)

- ### The About Page
  - This page provides general information about this website to the user.

  ![The About page](/media/images/readme/about.jpg)

- ### The Sign-Up Page
  - This page will allow the user to get signed up to the website. The user will be asked to submit their full name, email address, and password.

  ![The Sign up page](/media/images/readme/signup.jpg)

- ### The login Page
  - This page will allow the user to get login to the website if already has been registerd.

  ![The login page](/media/images/readme/signin.jpg)

- ### The Profile Page
  - This page will demostrate the user's info such as name and email's adress.

  ![The profile page](/media/images/readme/profile.jpg)

- ### The New Post Page
  - This page allow the user to create a new post by compliting a form with different sections such as title, excerpt, content and status.
  - By creating a new post the user redirect to the post detail page.

  ![The New Post page](/media/images/readme/new.jpg)

- ### The Post Detail Page
  - The user can acsess to this page by clicking on the post's title or post's excerpt on the Home page. Also by creating a new post the user redirect to this page.
  - This page allows the user to read, update and delete the post, leave the comment and like the post.

  ![The Post Detail page](/media/images/readme/detail-content.jpg)
  ![The Post Detail page](/media/images/readme/detail-comment.jpg)

- ### The Post Update Page
  - The user can acsess to this page by clicking on the update's button on the Post Detail page. By clicking opens the post form with last context so as the user can update it and redirect to the updated post.

  ![The Post Detail page](/media/images/readme/update.jpg)

- ### The Post Delete Page
  - The user can acsess to this page by clicking on the delete's button on the Post Detail page. By clicking opens the confirm delete page which asks if the user is sure to delete the post permanently or wants to cancel it. By clicking cancel button the user redirect to the Post Detail page.

  ![The Post Detail page](/media/images/readme/delete.jpg)
  
# Data Model
   This diagram shows the different components of the website. The website is divided into different sections, authentication, creation post, access, and read created posts.

   ![Diagram](/media/images/readme/diagram.jpg)

# Design
- ### Sketch wireframes used in making the website mockup.
  - The Home page

    ![The Home page wireframe](/media/images/readme/home-page.jpg)

  - The Post Detail page

    ![The Post Detail page wireframe](/media/images/readme/post-detail.jpg)

  - The About page

    ![The About page wireframe](/media/images/readme/about-page.jpg)

  - The Sign Up page

    ![The Sign Up page wireframe](/media/images/readme/register-page.jpg)

  - The Sign In page

    ![The Sign In page wireframe](/media/images/readme/login-page.jpg)

  - The Sign Out page

    ![The Sign Out page wireframe](/media/images/readme/logout-page.jpg)

  - The Profile page

    ![The Profile page wireframe](/media/images/readme/profile-page.jpg)

  - The New Post page

    ![The New Post page wireframe](/media/images/readme/new-page.jpg)

  - The Post Update page

    ![The Post Update page wireframe](/media/images/readme/update-page.jpg)

  - The Post Delete page

    ![The Post Delete page wireframe](/media/images/readme/delete-page.jpg)

- ### Database Model

  ![Diagram](/media/images/readme/database.jpg)

# Testing

- This website is responsive for different devices such as desktop pc, tablets, and mobile. It functions on all standard screen sizes using the Chrome Dev Tools device toolbar.

- Different parts of the website such as header, footer, the main section, about page, sign up, login, profile, new post and post detail page all are easy to understand and readable.

- Manual test case template

  ![Manual test case template](/media/images/readme/Manual-Test-Case-Template.jpg)

### Validator Testing

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org) (check by text input)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator) (check by direct input)

- JavaScript
  - No errors were found when passing through the official  [Jshint validator](https://jshint.com/).
    - The following metrics were returned for the play.js file:
    - There is only one function in this file.
    - It takes no arguments.
    - This function contains 3 statements.
    - Cyclomatic complexity number for this function is 1.

- PEP8
   - No errors were returned from PEP8online.com

- Accessibility

![Accessibility](/media/images/readme/accessibility.jpg)

### Bugs
#### Solved bugs
- When I clicked on the like button on the post detail page a square box appeared around the heart icon. 
- I fixed the problem by adding this line of code `button:focus {outline: none;}` on the style.css file.


# Deployment
This project was deployed to Heroku.
- Steps for deployment:
  - Create a Virtual Environment
  - Install Project Dependencies
  - Update Local Database Schema
  - Run a Local Development Server
  - Fork or clone this repository
  - Create a new Heroku app
  - Update Remote Database Schema
  - Link the Heroku app to the repository
  - Click on **Deploy**

[Here is the live version of my project](https://developers-blog.onrender.com)

# Credits
### Content
- The icons in the footer, like and comment icon taken from [Font Awesome](https://fontawesome.com/)
- The commented code in the project is taken from CI [Codestar](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) project and [Specific YouTube Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)

### Media
- The photos used on the home page are from [Pexels](https://www.pexels.com)
- The posts content on the Home and the Post Detail page are from [Web.dev](https://web.dev/debug-web-vitals-in-the-field/)