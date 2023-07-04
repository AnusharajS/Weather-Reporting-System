import flask
import os
import csv
# import requests as re
import pandas as pd
import numpy as np
from flask import Flask, render_template, jsonify, request, session, redirect, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# timestamp = request.args.get("timestamp")
# temp = request.args.get("temp")
# hum = request.args.get("hum")
# pres = request.args.get("pressure")


datafile = "C:/Users/Anusha/OneDrive/Documents/VI SEM/IoT lab/IoT Mini project/sensor_sample.csv"
df = pd.read_csv(datafile)


# def add_to_file(datafile):
#     # checks if file exists. if yes, appends values for dictionary keys under corresponding header in a new line
#     if os.path.isfile(datafile):
#         with open(datafile, 'a', newline='') as csvfile:
#             # ,'Pressure','Dripping Staus']
#             fieldnames = ['Time', 'Temperature-C',
#                           'Temperature-F', 'Humidity', 'Pressure']
#             data_writer = csv.DictWriter(
#                 csvfile, fieldnames=fieldnames, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

#             # , 'Pressure':data2['pressure'], 'Dripping status':data3['status']})
#             data_writer.writerow({'Time': timestamp, 'Temperature-C': temp,
#                                  'Temperature-F': ((9/5)*temp)+32, 'Humidity': hum, 'Pressure': pres})

#     else:  # creates file (that has been checked and does not yet exist) and adds headers and values for all 3 keys in dict
#         with open(datafile, 'w', newline='') as csvfile:
#             fieldnames = ['Time', 'Temperature-C', 'Temperature-F',
#                           'Humidity', 'Pressure']
#             data_writer = csv.DictWriter(
#                 csvfile, fieldnames=fieldnames, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

#             data_writer.writeheader()
#             # 'Pressure':data2['pressure'], 'Dripping status':data3['status']})
#             data_writer.writerow({'Time': timestamp, 'Temperature-C': temp,
#                                  'Temperature-F': ((9/5)*temp)+32, 'Humidity': hum, 'Pressure': pres})


@app.route('/report')
def report():
    return render_template('report.html')


@app.route('/dashboard')
def db():
    add_to_file(datafile)
    return render_template('plots.html')


@app.route('/chartdata', methods=['GET', 'POST'])
def chart_data():
    data = pd.read_csv(datafile)
    print(data)
    return data.to_json()

# def pred():


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
