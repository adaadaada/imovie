from flask import Flask, render_template

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/imovie"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "5cc81d864066424680c2f91137b4678f"
app.debug = True
db = SQLAlchemy(app)

from app.admin import admin as admin_bp
from app.home import home as home_bp

app.register_blueprint(home_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")


# 404错误页面处理
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
