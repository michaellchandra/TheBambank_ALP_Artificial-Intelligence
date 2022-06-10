
#Flask Import

from flask import Flask
app = Flask("ALP_AI")

from flask import render_template

#App Route
@app.route("/")
def home():
    return render_template(
        "index.html",
        name = "Home - The Bambank Color Palette"
    )


