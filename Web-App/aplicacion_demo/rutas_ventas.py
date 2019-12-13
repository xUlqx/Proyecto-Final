from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Venta, Cliente, Tarjeta, TarjetaCliente
import jwt
import tkinter
from tkinter import messagebox    
from logging import FileHandler, WARNING
            
@app.route('/venta/')
def venta():  
    ventas= Venta.get_all()

    return render_template("venta/index.html",
                            ventas=ventas,
                           titulo='ventas')
@app.route('/venta/tarjeta')


@app.route("/venta/crear", methods=["GET"])
def venta_crear():
    clientes = Cliente.get_all()
    tarjetas = Tarjeta.get_all()
    return render_template("venta/crear.html",
                           clientes=clientes,
                           tarjetas=tarjetas,
                           titulo='Crear nuevo')

@app.route("/venta/crear", methods=["POST"])
def venta_agregar():
    if request.method == 'POST':
        
        id_cliente = request.form.get('id_cliente')
        token = request.form.get('token')
        monto = request.form.get('monto')
        token2 = request.form.get('token2')
    if id_cliente and token and monto:

        venta1 = Venta(monto=monto, token=token, id_cliente=id_cliente)
        tiempo = dt.now()
        db.session.add(venta1)
        db.session.commit()
        venta_id = venta1.id
        root = tkinter.Tk()
        root.withdraw()
        
        messagebox.showinfo("Estado","La Venta ha sido Exitosa\n\n      Code: 200")
        f = open("systemlog.txt", "a")
        f.write("\nLa Venta numero : " + str(venta_id) +  " ha sido Exitosa | Tiempo:" + str(tiempo) + "\n\n")
        f.close()
        root.destroy()
        

        
        return redirect(url_for('venta'))
        #return make_response('La Venta ha sido Exitosa!', 200)

    else:
        root2 = tkinter.Tk()
        root2.withdraw()
        messagebox.showerror("Estado","La Venta NO ha sido Exitosa\n\n      Code: 403")
        f = open("systemlog.txt", "a")
        f.write("\nLa Venta NO ha sido Exitosa | Tiempo:" + str(dt.now()) + "\n\n")
        f.close()
        root2.destroy()
        return redirect(url_for('venta'))
        #return make_response('La Venta NO ha sido Exitosa!', 403)"""
    
    




@app.route("/venta/delete", methods=['GET', 'POST'])
def venta_delete():
    venta_id = int(request.args['id'])
    venta = Venta.find_by_id(venta_id)
    db.session.delete(venta)
    db.session.commit()
    root = tkinter.Tk()
    root.withdraw()
        
    messagebox.showinfo("Estado","La Venta Numero: " + str(venta_id) + " ha sido eliminada. \n\n      Code: 200")
    f = open("systemlog.txt", "a")
    f.write("\nLa Venta numero : " + str(venta_id) +  " ha sido Eliminada | Tiempo:" + str(dt.now()) + "\n\n")
    f.close()
    root.destroy()
    return redirect(url_for('venta'))

@app.route("/venta/update", methods=['GET', 'POST'])
def venta_updated():
    venta_id = int(request.args['id'])
    venta = Venta.find_by_id(venta_id)
    if request.method == 'POST':
        id_cliente = str(request.form.getlist('id_cliente'))
        token = str(request.form.getlist('token'))
        monto = request.form.get('monto')
    if id_cliente and token and monto:
        venta.monto = monto 
        venta.token = token
        venta.id_cliente = id_cliente
        tarjeta.update()
    return redirect(url_for('venta'))
        

        