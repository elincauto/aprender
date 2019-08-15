from app import app
from flask import render_template,request,redirect,url_for,flash
import csv

ficheromovimientos='data/movimientos.txt'

@app.route('/')
def index():
    #leer movimientos
    fMovimientos= open(ficheromovimientos,'r')
    csvreader=csv.reader(fMovimientos, delimiter=',' , quotechar='"')

    movimientos =[]
    for movimiento in csvreader:
        movimientos.append(movimiento) 

        
    #enviar movimientos
    return render_template('index.html',movimientos=movimientos)
   

@app.route('/nuevacompra', methods=['GET','POST'])
def compra():
    print(request.method)
    if request.method=='GET':       
        return render_template('nuevacompra.html')

    else:
        msg=validar(request.values)  != True
        if msg!=True
            flash(msg)
            return render_template('nuevacompra.html')
       
        fMovimientos=open(ficheromovimientos,'a+')
        precioUnitario=request.values['cantidadPagada']/request.values['cantidadComprada']  
        registro='{},'{}',{},{},{},{},{}\n'.format(request.values['fecha'],
        request.values['concepto'],request.values['monedaComprada'],
        request.values['cantidadComprada'],
        request.values['monedaPagada'],
        request.values['cantidadPagada'],precioUnitario)
        fMovimientos.write(registro)
        fMovimientos.close()
        return redirect(url_for('index'))
    
    def validar(values):
        if values['fecha']=='':
            return 'Debe informar la fecha'

        if values['concepto']=='':
            return 'Debe informar el concepto'

         if values['cantidadComprada']=='':
            return 'Debe informar una cantidad mayor que cero para cantidad comprada'

        if values['cantidadPagada']=='':
            return 'Debe informar un valor mayor que cero'

        return True




