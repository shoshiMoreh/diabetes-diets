import pymongo

# יצירת חיבור ל-MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# יצירת מסד נתונים
db = client["diabetesProject"]

# יצירת קולקציה
collection = db["details"]

# הגדרת הסכימה של הקולקציה
schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id", "name", "lastName", "mail", "password", "age", "gender", "kg", "high", "bloodGlucoseLevel", "hba1cLevel", "smokingHistory", "heartDisease", "hypertension"],
            "properties": {
                "id": {
                    "bsonType": "int",
                    "description": "must be a number and is required"
                },
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "lastName": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "mail": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "password": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "age": {
                    "bsonType": "int",
                    "description": "must be a number and is required"
                },
                "gender": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "kg": {
                    "bsonType": "number",
                    "description": "must be a number and is required"
                },
                "high": {
                    "bsonType": "int",
                    "description": "must be a number and is required"
                },
                "bloodGlucoseLevel": {
                    "bsonType": "int",
                    "description": "must be a number and is required"
                },
                "hba1cLevel": {
                     "bsonType": "number",
                     "description": "must be a number and is required"
                },
                "smokingHistory": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "heartDisease": {
                    "bsonType": "bool",
                    "description": "must be a boolean and is required"
                },
                "hypertension": {
                    "bsonType": "bool",
                    "description": "must be a boolean and is required"
                }
            }
        }
    }
}

# יצירת הקולקציה עם הסכימה
db.create_collection("details", validator=schema["validator"])
