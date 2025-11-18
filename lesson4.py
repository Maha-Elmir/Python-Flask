from flask import Flask

app = Flask(__name__)

### Home page
@app.route("/")
def home():

    html = """
    <h1>Welcome to my home page</h1>
    <p>Click the link below to navigate</p>
    <a href="/about">Go to about page</a>
    <a href="cat">Go to the kitty page page</a>
    <a href="/contact">Go to my contact page</a>
    """
    return html

### About page
@app.route("/about")
def about():
    html = """
    <h1>Welcome to my about page</h1>
    <p>I'm an epic coder</p>
    <a href="/">Go to home page</a>
    <a href="/cat">Go to the kitty page</a>
    <a href="/contact">Go to my contact page</a>
    """
    return html

### Third page
@app.route("/cat")
def cat():
    html = """
    <h1>This is the kitty page!</h1>
    <h3>This is for the lesson challenge</h3>
    <p>I learned how to add pictures (This cat is me right now)</p>
    <image src="https://i.pinimg.com/736x/14/20/fd/1420fdb2c1b84a55bc9a61e3050b0fa5.jpg" alt="Me right now">
    <a href="/">Go to home page</a>
    <a href="/about">Go to about page</a>
    <a href="/contact">Go to my contact page</a>
    """
    return html

### Contact page
@app.route("/contact")
def contact():
    html = """
    <h1>When to contact me</h1>
    <p>I dont know when</p>
    <a href="/">Go to home page</a>
    <a href="/about">Go to about page</a>
    <a href="/cat">Go to the kitty page page</a>
    """
    return html

app.run(debug=True, port=5000)