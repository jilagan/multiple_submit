from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/formsubmission', methods = ['POST'])
def form_submission():
    stype = request.form.get("stype")
    return render_template('formsubmission.html',stype=stype)
