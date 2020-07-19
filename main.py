from search import search_ai
from flask import Flask, jsonify, request
import json
from recommend import Filtering

app = Flask(__name__)

@app.route('/')
def Home():  
   resp = {
       "status":200,
       "message":"OK",
   }
   return jsonify(resp)

@app.route('/Search')
def predict():
    Position = request.args.get('text')
    JobPosition, JobID, Percentage = search_ai(Position)
    JobID = json.dumps(int(JobID))
    Percentage = Percentage * 100
    Percentage = json.dumps(float(Percentage))
    resp = {
        "status" : 200,
        "message": "OK",
        "data":{
            "Input" : Position,
            "Position": JobPosition,
            "ID": JobID,
            "Percentage" : Percentage,
        }
    }
    return jsonify(resp),200

@app.route('/recommend')
def recommendation() :
    UserID = request.args.get('ID') # ตอนนำไปใช้งานจะใช้ ID ที่ USER ได้รับจริงตอนลงทะเบียน#
    resp = {
        "status" : 200,
        "message" : "OK",
        "data" : {
            "recommend1" : Filtering(UserID, 0),
            "recommend2" : Filtering(UserID, 1),
            "recommend3" : Filtering(UserID, 2)
        }
    }
    return jsonify(resp), 200
if __name__ == '__main__':
   app.run(host="0.0.0.0",port = 8080, debug=True)