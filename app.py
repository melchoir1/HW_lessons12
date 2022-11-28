from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.main_blueprint import main_blueprint
from loader.loader_blueprint import loader_blueprint
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)


app.run(host='127.0.0.1', port=8000, debug=True)