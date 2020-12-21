from wsilabeador import app
from pipapilapibra.pilengua import pilengua, inversa
from flask import jsonify, request


@app.route('/<frase>')
def index(frase):
    diccionario = {}
    diccionario["Response"] = True
    diccionario["result"] = {"original": frase, "traducido": pilengua(frase)}

    '''
    También podemos hacerlo a capón
    diccionario = {"Response": True,
                   "result":{"original": frase, "traducido": pilengua(frase)}
    }
    '''

    return jsonify(diccionario)

@app.route('/decodifica/<frase>')
def decodifica(frase):
    diccionario = {}
    diccionario["Response"] = True
    diccionario["result"] = {"original": frase, "traducido": inversa(frase+" ")}

    return jsonify(diccionario)
