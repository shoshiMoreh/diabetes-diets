import pymongo as pm
from pymongo import DESCENDING, ReturnDocument
from flask import Flask, jsonify, request, flash, send_file, Response
from flask_cors import CORS, cross_origin
from bson import json_util
from utils import all, bmi
from diet import totalModel, numCalories
from bll import sendModel
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app, supports_credentials=True)
client = pm.MongoClient("mongodb://localhost:27017/")
db = client["diabetesProject"]
collection = db["details"]
collection2 = db["diet2"]


@app.route('/users/GetUserByMailAndPassword', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_user_by_email_and_pass():
    request_data = request.get_json()
    mail = request_data['mail']
    print("כעי")
    password = request_data['password']
    userData = collection.find_one({"mail": mail})
    if userData and userData.get('password') == password:
        print("מצאתי!!")
        return json_util.dumps(userData), 200
    return jsonify(False), 400


@app.route('/users/addUser', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_user():
    user = request.json
    # הוספת המשתמש למסד הנתונים
    latest_user = collection.find_one(sort=[("id", DESCENDING)])
    if latest_user is not None:
        next_id = latest_user['id'] + 1
    else:
        next_id = 1
    print(next_id)
    user['id'] = next_id
    print(user)
    result = collection.insert_one(user)
    userData = collection.find_one({"_id": result.inserted_id})
    print("cvb")
    print(result)
    print("True")
    if not result:
        return jsonify('error'), 500
    # return jsonify({'message': f'User added successfully, user id: {str(result.inserted_id)}',
    #                 'user_id': str(result.inserted_id)}), 200
    return jsonify(str(userData['id']))

    # return jsonify({'message': f'User added successfully, user id: {result.inserted_id}', 'user_id': result.inserted_id}), 200
    # return jsonify(result)


@app.route('/users/addDiet', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_diet():
    requestData = request.json
    user = requestData['user']
    diet = requestData['diet']
    print("קריאת הנתונים")
    diet = sendModel(user, diet)
    # הוספת הדיאטה למסד הנתונים
    diet['id'] = int(user.get("id"))
    print(diet)
    result = collection2.insert_one(diet)
    if not result:
        return jsonify('error')
    return json_util.dumps(diet), 200

@app.route('/users/updateDiet', methods=['POST'])
@cross_origin(supports_credentials=True)
def update_diet():
    print("גכעיחיעכג")
    requestData = request.json
    user = requestData['user']
    diet = requestData['diet']
    print("שלום!!")
    if not user:
        return jsonify({"message": "No data provided for update"}), 400
    if "id" not in user:
        return jsonify({"message": "No ID provided for update"}), 400
    existing_user = collection2.find_one({"id": int(user["id"])})
    if not existing_user:
        return jsonify({"message": "User not found"}), 404
    query = {"id": existing_user.get("id")}
    diet = sendModel(user, diet)
    print(query)
    update_data = {"$set": existing_user}
    result = collection2.update_one(query, {"$set":
                                               {"chanceDiabetes": diet.get("chanceDiabetes"),
                                                "sunday": diet.get("sunday"),
                                                "monday": diet.get("monday"),
                                                "tuesday": diet.get("tuesday"),
                                                "wednesday": diet.get("wednesday"),
                                                "thursday": diet.get("thursday"),
                                                "friday": diet.get("friday"),
                                                "saturday": diet.get("saturday"),
                                                }})
    print(result)
    if not result:
        return jsonify({"message": "error"}), 404
    userData = collection2.find_one({"id": diet.get("id")})
    return json_util.dumps(diet), 200

@app.route('/users/updateUser', methods=['POST'])
@cross_origin(supports_credentials=True)
def update_user():
    print("אני רוצה לעדכן!!")
    # # מידע חדש לעדכון
    new_data = request.json
    # # בדיקה אם ישנם נתונים לעדכון
    # if not new_data:
    if not new_data:
        return jsonify({"message": "No data provided for update"}), 400
    # בדיקה האם המשתמש קיים במסד הנתונים
    if "id" not in new_data:
        return jsonify({"message": "No ID provided for update"}), 400
    existing_user = collection.find_one({"id": int(new_data["id"])})
    if not existing_user:
        return jsonify({"message": "User not found"}), 404
    query = {"id": existing_user.get("id")}
    print(query)
    update_data = {"$set": existing_user}
    # עדכון המשתמש במסד הנתונים
    # result = collection.find_one_and_update(query, update_data, return_document=ReturnDocument.AFTER)
    result = collection.update_one(query, {"$set":
                                              {"name": new_data.get("name"),
                                                "lastName": new_data.get("lastName"),
                                                "mail": new_data.get("mail"),
                                                "password": new_data.get("password"),
                                                "a": new_data.get("a"),
                                                "age": new_data.get("age"),
                                                "gender": new_data.get("gender"),
                                                "kg": new_data.get("kg"),
                                                "high": new_data.get("high"),
                                                "bloodGlucoseLevel": new_data.get("bloodGlucoseLevel"),
                                                "hba1cLevel": new_data.get("hba1cLevel"),
                                                "smokingHistory": new_data.get("smokingHistory"),
                                                "heartDisease": new_data.get("heartDisease"),
                                                "hypertension": new_data.get("hypertension")}})
    if not result:
        return jsonify({"message": "error"}), 404
    return jsonify("True")



@app.route('/users/GetDietById', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_diet_by_id():
    id = request.get_json()
    print("כעי")
    diet = collection2.find_one({"id": id})
    if diet:
        # return jsonify(userData), 200
        return json_util.dumps(diet), 200
    return jsonify(False)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
