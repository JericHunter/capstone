from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    """Return homepage."""
    return render_template('gallery.html')

@app.route('/about')
def about():
    """Return homepage."""
    return render_template('about.html')
