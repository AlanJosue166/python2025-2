
from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def cliente_funcion():
    ci = request.json.get('ci')
    print("headers:", request.headers)
    print(f"CI recibido: {ci}")

    codRes, menRes, accion, salida = buscar_cliente(ci)

    respuesta = {
        "accion": accion,
        "codRes": codRes,
        "menRes": menRes,
        "ci": ci
    }

    if accion == "Success":
        respuesta.update(salida)

    return jsonify(respuesta)


def buscar_cliente(ci):
    ciLocal = "5748189"
    nombreLocal = "Alan"
    celLocal = "09111111"
    dirLocal = "xxxxxxxx"

    codRes = "SIN_ERROR"
    menRes = "OK"
    accion = ""
    salida = {}

    try:
        print("Verificando cliente...")

        if ci == ciLocal:
            print("Cliente encontrado")
            accion = "Success"
            salida = {
                "nombre": nombreLocal,
                "cel": celLocal,
                "dir": dirLocal
            }
        else:
            print("Cliente no está en el sistema")
            codRes = "ERROR"
            menRes = "Error cliente"
            accion = "Cliente no está en el sistema"

    except Exception as e:
        print("ERROR:", str(e))
        codRes = "ERROR"
        menRes = "Msg: " + str(e)
        accion = "Error interno"

    return codRes, menRes, accion, salida