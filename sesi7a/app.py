from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():    
  return "Hello, world"

@app.route('/<name>')
def hello(name):  
  # return f"Hello, { name }"
  return f"Hello, { escape(name)}"

@app.route('/hello')
def helloHTML():
  name = "OCBC"
  return render_template('index.html', value=name)


# apakah dijalankan sebagai standalone script
if __name__ == '__main__':    
  app.run(debug=True)
  