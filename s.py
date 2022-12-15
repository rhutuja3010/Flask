import json
from flask import Flask
import pandas as pd
# with open ('source.json',encoding='utf-8') as file:
#     dic=json.load(file)
# information=dic['data']
information=pd.read_csv("source.csv",encoding='utf-8')
app = Flask(__name__)
@app.route('/')
def searchStringInTitle():
    l=[]
    Title=str(information["title"])
    # l.append(Title)

    # Title.encode('title').decode('utf8')
    return Title
if __name__ == '__main__':
    app.run(debug=True)