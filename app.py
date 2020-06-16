from flask import Flask, jsonify
from flask import render_template
from AzureCLI import *


azureAPI = Flask(__name__)

@azureAPI.route('/')
def home():
    try:
        return render_template("home.html")

    except SyntaxError:
        return 'A syntax error has occurred. Please run the code through a build process and try again...'

    except Exception as e:
        return e

@azureAPI.route('/listvms')
def listvms():
    return jsonify(AzureCLI.listVMs())

azureAPI.run(host='0.0.0.0', port=5000)
