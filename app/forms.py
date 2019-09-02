from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField,SelectField,SubmitField
from wtforms.validators import Datarequired,ValidationError


class CompraForm(FlaskForm):
    fecha = DateField('Fecha', validators=[Datarequired()])
    concepto = StringField('Concepto', validators=[Datarequired()])
    cantidadComprada=FloatField('Cantidad Comprada', validators=[Datarequired()])
    monedaComprada=SelectField('Moneda pagada',choices=[('EUR','Euros'),('BTC','Bitecoins'),('LTC','Litecoins'),('ETH','Ethereum')])
    cantidadPagada=FloatField('Cantidad Pagada',validators=Datarequired)
    monedaPagada=SelectField('Moneda pagada',choices=[('EUR','Euros'),('BTC','Bitecoins'),('LTC','Litecoins'),('ETH','Ethereum')] )
    submit= SubmitField('Comprar')

    def validate_cantidadComprada(self,field):
        if field.data < 0:
            raise ValidationError('Debe ser un numero positivo')
 