import numpy as np
import tensorflow as tf
from flask import Flask,render_template,request,url_for
print(tf.__version__)
model=tf.keras.models.load_model("tmp.h5")


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        year=int(request.form['year'])
        t_1=[20.92,23.58,26.61,29.56,30.41,29.7,28.18,28.17,27.72,26.81,23.9,21.89]
        t_2=[20.59,23.08,25.58,29.17,30.47,29.44,28.31,28.12,28.11,27.24,23.92,21.47]
        for i in range(year-2017):
            t=[]
            test=[]
            x1=t_1
            t.append(x1)
            x2=t_2
            t.append(x2)
            test.append(t)
            test=np.array(test)
            y_hat=model.predict(test)
            t_1=x2
            t_2=list(y_hat[0])
        output=list(y_hat[0])
        month=['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT','NOV', 'DEC']
        return render_template('index.html',month=month,temp=output,y=year)
    return render_template('index.html',month=False,temp=False)
if __name__ == "__main__":
    app.run(debug=True)
    

    
