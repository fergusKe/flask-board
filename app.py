from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts/<id>')
def posts(id):
  return render_template('posts.html', id=id)

if __name__ == '__main__':
  app.run(debug=True)