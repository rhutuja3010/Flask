


from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_name():
   return 'Hello %s!'
 
if __name__ == '__main__':
   app.run()



from flask import Flask
import pandas as pd

app = Flask(__name__)
information=pd.read_csv("cource.csv")

@app.route('/')
def title():
    for j in information["title"]:
        return j

if __name__ == '__main__':
    app.run(debug=True)