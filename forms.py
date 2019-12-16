from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Required




class AddForm(FlaskForm):
    empid = StringField('Empid', validators=[DataRequired(), validators.length(max=10)])
    empname = StringField('Empname', validators=[DataRequired(), validators.length(max=25)])
    dateofbirth = DateField('DateofBirth', validators=[Required()])
    submit = SubmitField('Sign In')