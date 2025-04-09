import sqlite3
from flask import Flask, render_template, g, jsonify, request, redirect, url_for


app = Flask(__name__)

DATABASE = 'blogs.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row 
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    db = get_db()
    blogs = db.execute('SELECT * FROM blogs').fetchall()
    return render_template('home.html', blogs=blogs)

@app.route('/api/blogs')
def blogs_api():
    db = get_db()
    blogs = db.execute('SELECT * FROM blogs').fetchall()
    blogs_list = [{'title': b['title'], 'published': b['published']} for b in blogs]
    return jsonify(blogs_list)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    db = get_db()
    blog = db.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,)).fetchone()
    if blog is None:
        return "Blog not found", 404
    return render_template('blog_detail.html', blog=blog)

@app.route('/add-blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['title']
        published = request.form['published']
        content = request.form['content']  

        conn = sqlite3.connect('blogs.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO blogs (title, published, content, image) VALUES (?, ?, ?, ?)",
                    (title, published, content,))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('add_blog.html')


@app.route('/about-us')
def about_us():
  return render_template('about-us.html')
  
if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)