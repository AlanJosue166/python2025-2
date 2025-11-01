from flask import Blueprint, request, jsonify

login =Blueprint('login', __name__)

@login.route('/login',methods=['POST'])
def login_user():
    ci = request.json.get('ci')
    #password = request.json.get('password')
    print("Headers:", request.headers)
    print(f"usuario: {user} ") #"ci": {ci}
    
    codRes,menRes,accion= inicializarVariables(user) #password llamada a la funmcion de login
    
    salida = {
        "codRes":codRes,
        "menRes": menRes,
        "user": user,
        "accion": accion,
        "ci": ci
    }
    return jsonify(salida)
def inicializarVariables(user, ci):
    userLocal = "Derlis"
   # passLocal = "5748189"
    codRes= "Sin_Error"
    menRes= "OK"
    
    
    try: 
        print("Verificar login")
        if ci == userLocal:
            print("Login exitoso")
            accion= "Succes"
        else:
            print("usuario incorrecto")
            codRes= "EEROR"
            menRes= "Error cliente"
            ci= "4133267"
            print("Login fallido")
            accion="No_succes"
    except Exception as e:
        print("Error",str(e))
        codRes= "Error"
        menRes= 'Msg: ' + str(e)
        accion= "Error interno"
    return codRes,menRes, accion
    