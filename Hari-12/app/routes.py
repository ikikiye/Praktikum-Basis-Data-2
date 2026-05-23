from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():

   posts = [
        {
            'npm': '2406404876',
            'nama': 'Muhammad Risqi'
        },
    ]
   return render_template('index.html', dataMahasiswa=posts)
