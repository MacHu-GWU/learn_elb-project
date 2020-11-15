# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint("index", __name__, template_folder="templates")


@bp.route("/", methods=["GET", ])
def index():
    return render_template("index/index.html")


if __name__ == "__main__":
    from flask import Flask
    from learn_elb.webapp.config import PORT

    app = Flask("index")
    app.register_blueprint(bp)
    app.run(port=PORT, debug=True)
