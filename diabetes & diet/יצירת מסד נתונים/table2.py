import pymongo

# יצירת חיבור ל-MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# יצירת מסד נתונים
db = client["diabetesProject"]

# יצירת קולקציה
collection = db["diet"]

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
                    "bsonType": "number",
                    "description": "must be a string and is required"
                },
                "sunday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "monday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "tuesday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "wednesday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "thursday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "friday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
                "saturday": {
                    "bsonType": "object",
                    "properties": {
                        "data": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "must be a string"
                        }
                    },
                    "description": "must be an object"
                },
            }
        }
    }
}

# יצירת הקולקציה עם הסכימה
db.create_collection("diet", validator=schema["validator"])