from flask import Flask
from flask import Flask, render_template
import requests
import pandas as pd
import random
# app = Flask(__name__)
app=Flask(__name__,template_folder='templates')




@app.route('/')
def hello_world():
    with open("person.csv") as file:
        return render_template("index.html", csv=file)
    
    # file_name=requests.args.get("age","sample_data")

    # sample_data=pd.read_csv("person" +".csv")
    # json_data=sample_data.to_dict()
    # print(sample_data)
    # return render_template("index.html", len=len(sample_data),columns=list(sample_data), content=json_data)
    # return sample_data
    

if __name__ == "__main__":
    port = 5000 + random.randint(0, 999)
    app.run(debug=True, port=port)
    # app.run()


