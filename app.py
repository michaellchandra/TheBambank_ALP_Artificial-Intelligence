#Flask Import

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from PIL import Image

from sklearn.cluster import KMeans

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
# buat upload imagenya di image_path
image_path = Path("images/test_image.jpeg")
image = Image.open(image_path.open("rb"))

arr = np.array(image)
arr.shape

pixels = arr.reshape((-1,3))
pixels.shape

pixels.min(), pixels.mean(), pixels.max()

pixels = pixels.astype("float32") / 255
pixels.min(), pixels.mean(), pixels.max()

pixels.mean(0)

np.median(pixels,0)

plt.hist(
    pixels.mean(1),
    color="grey"
);

plt.figure(figsize=(16,4))
plt.subplot(1,3,1)
plt.hist(
    pixels[:,0],
    color="r"
)
plt.subplot(1,3,2)
plt.hist(
    pixels[:,1],
    color="g"
)
plt.subplot(1,3,3)
plt.hist(
    pixels[:,2],
    color="b"
);

plt.figure(figsize=(14,6))
sns.kdeplot(
    pixels[:,0],
    color="r"
)
sns.kdeplot(
    pixels[:,1],
    color="g"
)
sns.kdeplot(
    pixels[:,2],
    color="b"
)
plt.xlabel("Brightness")
plt.ylabel("Density")
plt.title(
    "Test Image RGB Color Channel Density",
    fontsize=20
);

kmeans = KMeans(n_clusters=8)
predictions = kmeans.fit_predict(pixels)
centers = kmeans.cluster_centers_

def read_image(path):
    with open(path,"rb") as f:
        return np.array(Image.open(f))

def preprocess_image(img):
    return img.reshape((-1,3)).astype("float32") / 255

def get_kmeans_centers(img,nclusters):
    return KMeans(n_clusters=nclusters).fit(img).cluster_centers_

def make_kmeans_palette(path,nclusters=8):
    # Load the image
    img = read_image(path)
    # Reshape and set range
    pixels = preprocess_image(img)
    # Cluster the pixels
    centers = get_kmeans_centers(pixels,nclusters)
    # Plot the image
    plt.figure(figsize=(14,8))
    plt.imshow(img)
    plt.grid()
    plt.axis('off')
    plt.show()
    # Plot the palette
    plt.figure(figsize=(14,6))
    plt.imshow(centers[
        np.concatenate([[i] * 100 for i in range(len(centers))]).reshape((-1,10)).T
    ])
    plt.grid()
    plt.axis('off')
    plt.show()
    # yg di return print("Image:",img_path),make_kmeans_palette(img_path)
    return render_template(print("Image:",img_path),make_kmeans_palette(img_path),
        "colorPalette.html",
        name = "Color Palette - The Bambank Color Palette"
    )

