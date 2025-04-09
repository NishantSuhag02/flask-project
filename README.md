# 📝 Flask Blogging Website 

A simple yet powerful blogging website built using **Flask** and **SQLite**, ideal for learning full-stack development with Python. This personal project lets you view, add, and read blog posts with clean UI using Bootstrap.

## 🔧 Features

- View all blog posts on the home page
- Read full blog content on individual detail pages
- Add new blog posts dynamically using a form
- SQLite database integration using `sqlite3`
- Efficient DB connection management using Flask's `g` object
- Clean, responsive frontend using **Bootstrap 5**
- REST API endpoint to fetch blog data as JSON

---

## 📸 Screenshot

![Homepage](static/screenshot-home.png)

---

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap 5
- **Database**: SQLite
- **Templating**: Jinja2
- **Deployment-ready**: Can be deployed on Replit, Heroku, or Render

---

## 📂 Project Structure

```
. ├── app.py # Main Flask app ├── blogs.db # SQLite database ├── database.py # Handles DB connection and utility functions ├── schema.sql # SQL script to initialize the database ├── templates/ │ ├── home.html # Homepage template │ ├── about-us.html # About Us page │ ├── nav.html # Navbar partial │ ├── blogitems.html # Blog list partial │ ├── blog_detail.html # Individual blog view │ └── add_blog.html # Blog creation form ├── static/ │ ├── screenshot-home.png # Screenshot for README │ └── image.jpg # Optional header image
```

---

## 🔗 API Usage

GET /api/blogs




