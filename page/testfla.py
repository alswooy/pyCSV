from flask import Flask, render_template,request
from django.shortcuts import render
from werkzeug.utils import secure_filename
import csv
# import pandas as pd
app = Flask(__name__)


@app.route("/")
def start():
    return render_template('upload.html')

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/Total_Benign_Malicious_Error_Chart',methods =['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f=request.files['file'] #받아오는
        
        return render_template('Total_Benign_Malicious_Error_Chart.html',file=f.filename) #보내주는
    
if __name__ == "__main__":
    app.run() 