import matplotlib.pyplot as plt
import csv
import matplotlib
from flask import Flask, send_file, make_response ,render_template, request, redirect
from io import BytesIO
import os
from werkzeug.utils import secure_filename
import numpy as np

## remove cache 
from functools import wraps, update_wrapper
from datetime import datetime
matplotlib.use('Agg') 

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response      
  return update_wrapper(no_cache, view)
app = Flask(__name__)


def file():
    filename = f"/Users/alswooy/Downloads/test.csv"

    with open(filename, encoding='utf-8') as f:
        data = csv.reader(f)
        # Initialize result containers
        counts = {hour: {'BENIGN': 0, 'MALICIOUS': 0, 'SUSPICIOUS': 0, 'ERROR': 0} for hour in range(24)}

        for row in data:
            if row[0] != '':
                my_str = row[0]
                result2 = row[2]

                # Check if the string is long enough and extract the hour
                if len(my_str) >= 13:  # Ensure my_str has enough characters
                    hour = int(my_str[11:13])  # Extract the hour as an integer
                    result_count = result2[0]  # Get the first character of result2

                    # Count the results if they are valid
                    if result_count in ['B', 'M', 'S', 'E']:
                        if result_count == 'B':
                            counts[hour]['BENIGN'] += 1
                        elif result_count == 'M':
                            counts[hour]['MALICIOUS'] += 1
                        elif result_count == 'S':
                            counts[hour]['SUSPICIOUS'] += 1
                        elif result_count == 'E':
                            counts[hour]['ERROR'] += 1

        # Calculate total counts for each hour
        total_counts = {hour: sum(counts[hour].values()) for hour in range(24)}
        
        # Prepare data for return
        benign = [counts[hour]['BENIGN'] for hour in range(24)]
        malicious = [counts[hour]['MALICIOUS'] for hour in range(24)]
        suspicious = [counts[hour]['SUSPICIOUS'] for hour in range(24)]
        error = [counts[hour]['ERROR'] for hour in range(24)]
        total = [total_counts[hour] for hour in range(24)]
    print(benign, malicious, suspicious, error, total)
    return benign, malicious, suspicious, error, total


@app.route("/", methods=["GET"])
@nocache
def index():
    benign, malicious, suspicious, error, total = file()
    
    benignx = list(range(1, 25))
    maliciousx = list(range(1, 25))
    suspiciousx = list(range(1, 25))
    errorx = list(range(1, 25))
    totalx = list(range(1, 25))

    fig = plt.figure(figsize=(10,10)) ## 캔버스 생성
    fig.set_facecolor('white') ## 배경색 설정
    ticklabel=['00','01','02','03','04','05','06','07','08','09',
                '10','11','12','13','14','15','16','17','18','19',
                '20','21','22','23']
    x = np.arange(24)  # 0부터 23까지의 값을 생성
    width = 0.15  # 막대 폭 설정

    # 그래프 그리기
    plt.bar(x - 2*width, benign, color='skyblue', width=width, label="BENIGN")
    plt.bar(x - width, malicious, color='g', width=width, label="MALICIOUS")
    plt.bar(x, suspicious, color='y', width=width, label="SUSPICIOUS")
    plt.bar(x + width, error, color='red', width=width, label="ERROR")
    plt.bar(x + 2*width, total, color='black', width=width, label="TOTAL")

    plt.title("Total_Benign_Malicious_Error_Chart")
    plt.xlabel('Time')
    plt.ylabel('Data')
    plt.legend(loc=0)
    plt.xticks(benignx,ticklabel,fontsize=10,rotation=0)
    
    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png', dpi=200)
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(port=5001) 