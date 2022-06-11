
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
@app.route("/home")
def homee():
    return render_template(
        "index.html",
        name = "Home - The Bambank Color Palette"
    )
    
@app.route("/about")
def about():
    return render_template(
        "about.html",
        name = "About Us - The Bambank Color Palette"
    )

@app.route("/colorpalette")
def colorpalette():
    return render_template(
        "colorPalette.html",
        name = "Color Palette - The Bambank Color Palette"
    )

