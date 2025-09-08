from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Optional, Email


class ProductForm(FlaskForm):
    name = StringField('Nome do Produto', validators=[DataRequired()])
    description = TextAreaField('Descricao')
    price = DecimalField('Preco',
                         validators=[DataRequired(), NumberRange(min=0.01, message='Preco deve ser maior que zero!')])
    submit = SubmitField('Salvar Produto')


class CustomerForm(FlaskForm):
    name = StringField('Nome do Cliente', validators=[DataRequired()])
    phone = StringField('Telefone/WhatsApp') #TODO adicionar validacao e formatacao
    email = StringField('Email', validators=[Optional(), Email()])
    customer_type = StringField('Tipo de Cliente')
    submit = SubmitField('Salvar Cliente')
