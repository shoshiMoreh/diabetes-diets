import pymongo

# יצירת חיבור ל-MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# יצירת מסד נתונים
db = client["diabetesProject"]

# הגדרת הסכימה של הקולקציה
schema = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["id", "chanceDiabetes"],
            "properties": {
                "id": {
                    "bsonType": "int",
                    "description": "must be a number and is required"
                },
                "chanceDiabetes": {
                    "bsonType": "double",
                    "description": "must be a number and is required"
                },
                "sunday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "monday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "tuesday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "wednesday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "thursday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "friday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                },
                "saturday": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "string"
                        }
                    },
                    "description": "must be an array of arrays of strings"
                }
            }
        }
    }
}

# יצירת הקולקציה עם הסכימה
db.create_collection("diet2", validator=schema["validator"])