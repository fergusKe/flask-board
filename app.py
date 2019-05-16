from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/posts/<id>')
def posts(id):
  return '文章編號是: %s' % id

if __name__ == '__main__':
  app.run(debug=True)