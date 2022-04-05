from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [
    {
        "id":1,
        "title":u"Go to grocery shop",
        "description":u"Buy tomatoes, apples, banana, biscuits",
        "done":False,
    },

    {
        "id":2,
        "title":u"Finish English Homework",
        "description":u"Write 500 word essay on the importance of dysopian texts in society",
        "done":False,
    },
]

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/add-data",methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":u"404 Error: Please provide data"
        }, 400)
    
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False,
        
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":u"Your request has been successfully submitted",
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks,
    
    })
if (__name__ == "__main__"):
    app.run(debug=True)

