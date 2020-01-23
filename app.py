 #from the flask library, import the class datatype Flask and the method render_template
from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html') #pass the html file 'home.html' to the method render template

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)