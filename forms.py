from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed

class CustomizationForm(FlaskForm):
    recipient_email = StringField("Recipient's Email", validators=[DataRequired(), Email()])
    message = StringField("Message", validators=[Length(min=0,max=50)])
    photos = MultipleFileField(validators=[FileAllowed(["png","jpg","jpeg","gif"])])
    submit = SubmitField('Add To Cart')
