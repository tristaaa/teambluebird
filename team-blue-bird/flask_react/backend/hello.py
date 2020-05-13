from flask import Flask, request
#from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import heapq

app = Flask(__name__)

@app.route('/test', methods=["POST"])
def hi():

    result = request.get_data()
    print(result)

    return "hi"

if __name__ == "__main__":
    app.run(port="5001")