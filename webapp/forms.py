from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired


class BasicParametersForm(FlaskForm):
    cruising_speed = FloatField('Крейсерская скорость км/с', validators=[DataRequired()])
    submit = SubmitField('Отправить')
