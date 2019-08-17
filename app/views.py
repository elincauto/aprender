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
        msg=validar(request.values)
        if msg!=True:
            
            return render_template('nuevacompra.html',errores=msg)
       
        fMovimientos=open(ficheromovimientos,'a+')
        precioUnitario=request.values['cantidadPagada']/request.values['cantidadComprada']  
        registro='{},"{}",{},{},{},{},{}\n'.format(request.values['fecha'],
        request.values['concepto'],request.values['monedaComprada'],
        request.values['cantidadComprada'],
        request.values['monedaPagada'],
        request.values['cantidadPagada'],precioUnitario)
        fMovimientos.write(registro)
        fMovimientos.close()
        return redirect(url_for('index'))
    
    def validar(values):

        errores=[]

        if values['fecha']=='':
            errores.append( 'Debe informar la fecha')

        if values['concepto']=='':
            errores.append('Debe informar el concepto')

        if values['cantidadComprada']=='':
            errores.append( 'Debe informar una cantidad mayor que cero para cantidad comprada')

        if values['cantidadPagada']=='':
            errores.append( 'Debe informar un valor mayor que cero')
        
        if len(errores)==0:
            return True
        else:
            return errores

@app.route('/skeleton.css')
def skeleton():
    return 'Hola,skeleton'




