from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')