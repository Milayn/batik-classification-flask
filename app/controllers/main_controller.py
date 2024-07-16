from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app.services.prediction_service import predict_batik
from app.models.batik_model import get_class_description
from datetime import datetime
import re

main = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        format_name = datetime.now().strftime("%Y%m%d%H%M%S") + filename
        file_path = os.path.join("app/static/uploads", format_name)
        file.save(file_path)
        prediction = predict_batik(file_path)

        deskripsi = get_class_description(index=prediction)

        return render_template(
            "index.html", prediction=prediction, filename=format_name, deskripsi=deskripsi
        )
    else:
        return redirect(request.url)
