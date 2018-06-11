import os

import cv2
import jinja2
from flask import Flask, render_template, request, jsonify, send_from_directory
from imagesearch.colordescriptor import ColorDescriptor
from imagesearch.searcher import Searcher

# create flask instance
app = Flask(__name__)

INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# main route
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload", methods=['POST'])
def upload():
    filename = ''
    target = os.path.join(APP_ROOT, 'static')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        # filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    print(filename)
    return render_template("complete.html", dest=filename)


@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":

        RESULTS_ARRAY = []

        # get url
        image_url = request.form.get('img')
        # image_url = os.path.join('static', image_url)
        print(image_url)
        try:

            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))

            # load the query image and describe it
            from skimage import io
            image_url = "static/" + image_url
            image_url = os.path.join(os.path.dirname(__file__), image_url)
            # query = io.imread(image_url)
            # query = cv2.cvtColor(query, cv2.COLOR_RGB2BGR)
            query = cv2.imread(image_url, 1)
            features = cd.describe(query)
            # perform the search
            searcher = Searcher(INDEX)
            results = []
            results = searcher.search(features)

            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append(
                    {"image": str(resultID), "score": str(score)})
            # return success
            return jsonify(results=(RESULTS_ARRAY[:]))

        except:

            # return error
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500


# run!
if __name__ == '__main__':
    app.run('127.0.0.1', debug=True)
