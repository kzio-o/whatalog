from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ProductForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[DataRequired()])
    description = TextAreaField('Descricao')
    price = DecimalField('Preco',
                         validators=[DataRequired(), NumberRange(min=0.01, message='Preco deve ser maior que zero!')])
    submit = SubmitField('Salvar Produto')

