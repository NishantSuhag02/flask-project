from flask import Flask, render_template, jsonify

app = Flask(__name__)

BLOGS = [
  {
    'title': 'Power of Yoga',
    'Published': 'April 12, 2023'
  },
  {
    'title': 'Unlocking the World of NFTs',
    'Published': 'Jan 07, 2024'
  },
  {
    'title': 'Exploring the Features of ChatGPT',
    'Published': 'May 25, 2023'
  },
  {
    'title': 'Sources of Fats That Are Harmful for Your Health',
    'Published': 'March 18, 2024'
  },
  {
    'title': 'Building Muscle',
    'Published': 'July 29, 2024'
  }
]

@app.route('/')
def home():
  return render_template('home.html', blogs=BLOGS)

@app.route('/about-us')
def about_us():
  return render_template('about-us.html')

@app.route('/api/blogs')
def blogs_api():
  return jsonify(BLOGS)
  
if __name__ == '__main__':
 app.run(host='0.0.0.0', debug=True)