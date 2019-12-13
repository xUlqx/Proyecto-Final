import jwt
from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Tarjeta, Cliente, Venta
import tkinter
from tkinter import messagebox    
from logging import FileHandler, WARNING

@app.route('/tarjeta/')
def tarjeta():
    tarjetas = Tarjeta.get_all()
    return render_template("tarjeta/index.html",
                           tarjetas=tarjetas,
                           titulo='tarjetas')


@app.route("/tarjeta/crear", methods=["GET"])
def tarjeta_crear():
    clientes = Cliente.get_all()
    return render_template("tarjeta/crear.html",
                           clientes=clientes,
                           titulo='Crear nuevo')

@app.route("/tarjeta/crear", methods=["POST"])
def tarjeta_agregar():
    import jwt
    import datetime
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        numero = request.form.get('numero')
        codigoSeguridad = request.form.get('codigoSeguridad')
        vencimientoMes = request.form.get('vencimientoMes')
        vencimientoAnio = request.form.get('vencimientoAnio')
        montoMax = request.form.get('montoMax')
        clientes = request.form.getlist('clientes')
        

    if tipo and numero and codigoSeguridad and vencimientoMes and vencimientoAnio and montoMax:
        token = jwt.encode({'numero' : numero, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], 'HS256')
        decoded_token = jwt.decode(token, 'altosecreto', algorithms=['HS256'])
        tarjeta1 = Tarjeta(tipo=tipo, numero=numero, codigoSeguridad=codigoSeguridad,
            vencimientoMes=vencimientoMes, vencimientoAnio=vencimientoAnio, montoMax=montoMax, token=token) 
        
        db.session.add(tarjeta1)
        db.session.commit()

        for cliente_id in clientes:
            cliente = Cliente.find_by_id(cliente_id)
            cliente.tarjetas.append(tarjeta1)
            cliente.update()
        
        tarjeta_id = tarjeta1.id
        root = tkinter.Tk()
        root.withdraw()
        
        messagebox.showinfo("Estado","La Tarjeta Ha sido Creada\n\n      Code: 200")
        f = open("systemlog.txt", "a")
        f.write("\nLa Tarjeta ID : " + str(tarjeta_id) +  " ha sido creado con Exit | Tiempo:" + str(dt.now()) + "\n\n")
        f.close()
        root.destroy()
        

       
        return redirect(url_for('tarjeta'))
    else:
        root2 = tkinter.Tk()
        root2.withdraw()
        messagebox.showerror("Estado","La Tarjeta NO fue Creada.\n\n      Code: 403")
        f = open("systemlog.txt", "a")
        f.write("\nTarjeta NO Creada Correctamente | Tiempo:" + str(dt.now()) + "\n\n")
        f.close()
        root2.destroy()
        return redirect(url_for('cliente'))

@app.route("/tarjeta/crear", methods=["POST"])
def tarjeta_agregar_post():
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        numero = request.form.get('numero')
        codigoSeguridad = request.form.get('codigoSeguridad')
        vencimientoMes = request.form.get('vencimientoMes')
        vencimientoAnio = request.form.get('vencimientoAnio')
        montoMax = request.form.get('montoMax')
    if tipo and numero:
        tarjeta1 = Tarjeta(tipo=tipo, numero=numero, codigoSeguridad=codigoSeguridad,
            vencimientoMes=vencimientoMes, vencimientoAnio=vencimientoAnio, montoMax=montoMax)
        db.session.add(tarjeta1)
        db.session.commit()
    return redirect(url_for('tarjeta'))

@app.route("/tarjeta/detalle", methods=['GET'])
def tarjeta_detalles():
    tarjeta_id = int(request.args['id'])
    tarjeta = Tarjeta.find_by_id(tarjeta_id)
    return render_template("tarjeta/detalle.html", tarjeta=tarjeta)

@app.route("/tarjeta/delete", methods=['GET', 'POST'])
def tarjeta_delete():
    tarjeta_id = int(request.args['id'])
    tarjeta = Tarjeta.find_by_id(tarjeta_id)
    db.session.delete(tarjeta)
    db.session.commit()
    return redirect("/tarjeta")

@app.route("/tarjeta/update", methods=['GET'])
def tarjeta_updating():
    print('request.args')
    print(request.args)
    print('request.base_url')
    print(request.base_url)
    print('request.data')
    print(request.data)
    print('request.form')
    print(request.form)
    print('request.get_json()')
    print(request.get_json())
    print('request.get_data()')
    print(request.get_data())
    print('request.full_path')
    print(request.full_path)
    print('request.headers')
    print(request.headers)
    print('request.method')
    print(request.method)
    print('request.query_string')
    print(request.query_string)
    print('request.referrer')
    print(request.referrer)
    print('request.user_agent')
    print(request.user_agent)
    tarjeta_id = int(request.args['id'])
    tarjeta = Tarjeta.find_by_id(tarjeta_id)
    return render_template("tarjeta/update.html", tarjeta=tarjeta)

@app.route("/tarjeta/update", methods=['GET', 'POST'])
def tarjeta_updated():
    if request.method == 'POST':
        id = request.form.get("id")
        tipo = request.form.get('tipo')
        numero = request.form.get('numero')
        codigoSeguridad = request.form.get('codigoSeguridad')
        vencimientoMes = request.form.get('vencimientoMes')
        vencimientoAnio = request.form.get('vencimientoAnio')
        montoMax = request.form.get('montoMax')
    if id and tipo and numero:
        tarjeta = Tarjeta.find_by_id(id)
        tarjeta.tipo = tipo
        tarjeta.numero = numero
        tarjeta.codigoSeguridad = codigoSeguridad
        tarjeta.vencimientoMes = vencimientoMes
        tarjeta.vencimientoAnio = vencimientoAnio
        tarjeta.montoMax = montoMax
        tarjeta.update()
    return redirect("/")
        

        