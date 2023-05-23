<div align="center">
    <img src="asset/logo_flask.jpeg" alt="flask">
</div>

---

<h1 align="center"> Flask website </h1>

an example of how you can make a website for your resume using flask

---

<h1 align="center">Project structure</h1>

```
WebSite/
├── asset/
│   └── ...
├── src/
│   ├── routes/
│   │   └── ... 
│   ├── static/
│   │   │── image/
│   │   │   └── ...
│   │   └── css/
│   │        └── ...
│   └── templates/
│       └── ... 
└── main.py
```

## asset/
The directory where the resources (such as images) are located.

## src/
The directory that contains the project's source code. It includes several subdirectories:
1. **routes/** - The files responsible for determining routes and processing requests are stored here.
2. **static/** - This directory contains static files such as CSS styles, JavaScript scripts, or images used by web pages.
3. **templates/** - This is where the HTML page templates that are used to display the content of the web application are stored.

## main.py
This is the main Flask application file. It contains the main code that initializes the application and defines its configuration, routes, and other settings.
