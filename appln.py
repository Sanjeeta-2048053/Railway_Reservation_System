from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pyodbc
#connection to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-LVQTHM2D\SQLEXPRESS;'
                      'Database=trains;'
                      'Trusted_Connection=yes;');

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("script2.html")


@app.route("/mime", methods = ["GET", "POST"])

def data():
    option = request.form['BB']
    if option == 'option1':
        data2=pd.read_sql("select * from Route", conn)
        result=data2.to_html()
        sns.barplot(x='Route_id',y='No_of_Stoppages',data=data2)
        plt.xlabel('Route')
        plt.ylabel('Number of stoppages')
        plt.title('Route wise stoppages')
        plt.savefig('static/train1.jpg')
        result=append_html(result,['train1.jpg'])
    elif option == 'option2':
        data2=pd.read_sql("select * from Station", conn)
        result=data2.to_html()
        sns.barplot(x='Station_Name',y='No_of_platforms',data=data2)
        plt.xlabel('Station name')
        plt.ylabel('Number of platforms')
        plt.title('Station wise platforms')
        plt.savefig('static/train2.jpg')
        result=append_html(result,['train2.jpg'])
    elif option == 'option3':
        data2=pd.read_sql("select * from Ticket", conn)
        result=data2.to_html()
    elif option == 'option4':
        data2=pd.read_sql("select * from Train", conn)
        result=data2.to_html()
    elif option == 'option5':
        data2=pd.read_sql("select * from User_details", conn)
        result=data2.to_html()
    return result

def append_html(result,image_names):
    for i in image_names:
        result=result+" <img src=\"static/"+i+"\" width=\"600\" height=\"500\">"
    return result

if __name__ == "__main__":
    app.run(debug=True)



        