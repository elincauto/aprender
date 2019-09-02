from app import app
from flask import render_template,request,redirect,url_for,flash
import csv
from os import remove, rename

ficheromovimientos='data/movimientos.txt'
ficheronuevo='data/nuevomovimientos.txt'

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
    form= CompraForm(request.form)

    if request.method=='GET':       
        return render_template('nuevacompra.html', form=form)

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

@app.route('/modificar',method=['GET','POST'])
def update():
   
    if request.method=='GET':
        if request.values.get('ix'):
            movimiento ,ix=recuperarregistro(request.values.get('ix'))
            return render_template('update.html', registro_seleccionado=movimiento, ix=ix)
    else:   
        if request.values.get('ix'):
            msg=validar(request.values)
            if msg != True:
                registro_seleccionado=[

                [request.values['fecha'],
                 request.values['concepto'],
                 request.values['monedaComprada'],  
                 request.values['cantidadComprada'],
                 request.values['cantidadPagada'] 
                 ]
                return render_template('update.html', registro_seleccionado=registro_seleccionado, ix=request.values['ix'], errores=msg)

            modificarregistro(request.values)

            return redirect(url_for('index'))




@app.route('/procesarregistro',methods=['POST'])
def procesar():
    if request.values.get('ix'):            
        if request.values['btnselected'] == 'Borrar': 
            borrar(request.values['ix'])  
    else: 
         #modificar(int(request.values['ix']))
         return redirect(url_for('update'))
        
    return redirect(url_for('index'))

def recuperarregistro(ix):
    fe=open(ficheromovimientos,'r')
    csvreader=csv.reader(fe, delimiter=',' , quotechar='"')
    contador=1
    for linea in csvreader:
        if contador==ix:
            fe.close()
            return linea
        contador+=1

    fe.close()    

def modificarregistro(values):
    fe=open(ficheromovimientos,'r')
    fs=open(ficheronuevo,'w')
    ix= int(values.get('ix'))
    precioUnitario=request.values['cantidadPagada']/request.values['cantidadComprada']  
    registro='{},"{}",{},{},{},{},{}\n'.format(request.values['fecha'],
                request.values['concepto'],request.values['monedaComprada'],
                request.values['cantidadComprada'],
                request.values['monedaPagada'],
                request.values['cantidadPagada'],precioUnitario)
    contador=1
    for linea in fe:
        if contador == ix:
            linea=registro
        fs.write(linea)

        contador+=1
    
    fe.close()
    fs.close()

    remove(ficheromovimientos)
    remove(ficheronuevo,ficheromovimientos)
          
def borrar(ix):
    
    fe=open(ficheromovimientos,'r')
    fs = open(ficheronuevo,'w')

    if request.values.get('ix'):

        ix=int(request.values['ix'])
        contador = 1
        for linea in fe:
            if contador !=ix:
                fs.write(linea)
        contador+=1
    fe.close()
    fs.close()
    remove(ficheromovimientos)
    rename(ficheronuevo, ficheromovimientos)



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




