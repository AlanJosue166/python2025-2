#

from flask import Flask
from login import login #importamos el bleprint desde login.py
from logout import logout

app=Flask(__name__)
app.register_blueprint(logout)
app.register_blueprint(login) #registramos el blueprint
@app.route('/')
def homo():
    return "Hola Alan"
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')