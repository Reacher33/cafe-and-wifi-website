from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


# WTForm for creating a new cafe data
class CafeForm(FlaskForm):
    name = StringField("Blog Post Title", validators=[DataRequired()])
    map_url = StringField("Blog Post Title", validators=[DataRequired(), URL()])
    img_url = StringField("Blog Post Title", validators=[DataRequired(), URL()])
    location = StringField("Blog Post Title", validators=[DataRequired()])
    has_sockets = BooleanField("Blog Post Title", validators=[DataRequired()])
    has_toilet = BooleanField("Blog Post Title", validators=[DataRequired()])
    has_wifi = BooleanField("Blog Post Title", validators=[DataRequired()])
    can_take_calls = BooleanField("Blog Post Title", validators=[DataRequired()])
    seats = StringField("Blog Post Title", validators=[DataRequired()])
    coffee_price = IntegerField("Blog Post Title", validators=[DataRequired()])
    submit = SubmitField("Add Cafe")
