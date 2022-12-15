from flask import Flask

import pandas as pd

df = pd.read_csv("source.csv")

app =  Flask(__name__)
@app.route('/')
def prod():

    x=list(df['title'])
    # result = '/n'.join(str(item) for item in x)
    # return result
    # return x
    return ('\n'.join(map(str, x)))
if __name__ == "__main__":

    app.run(debug=True)