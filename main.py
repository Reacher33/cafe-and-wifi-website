from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


class Property(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)
    location = db.Column(db.String(250), unique=True, nullable=False)
    has_sockets = db.Column(db.Integer, primary_key=True)
    has_toilet = db.Column(db.Integer, primary_key=True)
    has_wifi = db.Column(db.Integer, primary_key=True)
    can_take_calls = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.Integer, primary_key=True)
    coffee_price = db.Column(db.String, primary_key=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Property).order_by(Property.id))
    all_cafe = result.scalars().all()
    return render_template("index.html", cafes=all_cafe)


if __name__ == "__main__":
    app.run(debug=True)
