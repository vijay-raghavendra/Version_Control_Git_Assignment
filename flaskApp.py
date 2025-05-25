from urllib.parse import quote_plus
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

#  Safely encode the username and password
username = quote_plus("vijayaraghavendra424")
password = quote_plus("Vijay@250999")
#  Construct the URI
MONGO_URI = f"mongodb+srv://{username}:{password}@vijaycluster.pvsu0g3.mongodb.net/vijayDB?retryWrites=true&w=majority&appName=vijayCluster"
# MongoDB Connection
client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["submissions"]

@app.route("/submittodoitem", methods=["POST"])
def submit_item():
    data = request.get_json()
    item_name = data.get("itemName")
    item_desc = data.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"message": "Invalid input"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return jsonify({"message": "Item saved successfully"})

if __name__ == "__main__":
    app.run(debug=True)
