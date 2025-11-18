from flask import Flask

# Create the web host app
app = Flask(__name__)

# This route is for our home page
@app.route("/")
def home():
    return "Hello, World"

# Start the web app
app.run(debug=True, port=5000)