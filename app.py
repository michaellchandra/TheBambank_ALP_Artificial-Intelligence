
#Flask Import

from flask import Flask
app = Flask("ALP_AI")

from flask import render_template

@app.route("/")
def home():
    return render_template(
        "index.html",
        name = "Home - The Bambank Color Palette"
    )

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "welcome.html",
        name=name,
    )

cmap = ListedColormap(palettable.colorbrewer.qualitative.Dark2_7.mpl_colors)
