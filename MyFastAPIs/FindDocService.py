from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

mongo_user = os.getenv("MONGO_DB_USER")
mongo_password = os.getenv("MONGO_DB_PASSWORD")
mongo_database = os.getenv("MONGO_DATABASE")
mongo_collection = os.getenv("MONGO_COLLECTION")

# Use MongoDB Atlas URI instead of localhost
uri = f"mongodb+srv://{mongo_user}:{mongo_password}@cluster0.v5vloye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, 
                    tls=True,
                    tlsAllowInvalidCertificates=True,
                    tlsAllowInvalidHostnames=True,
                    serverSelectionTimeoutMS=5000)
db = client[mongo_database]
collection = db[mongo_collection]

@app.get("/health")
def health_check():
    try:
        # Test MongoDB connection
        client.admin.command('ping')
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

@app.get("/doctors")
def get_doctors():
    try:
        doctors = list(collection.find({}, {"_id": 0}))
        return {"doctors": doctors}
    except Exception as e:
        return {"error": f"Failed to fetch doctors: {str(e)}"}

@app.get("/doctors/{name}")
def get_doctor_by_name(name: str):
    try:
        # URL decode the name parameter and search case-insensitively
        doctor = collection.find_one({"name": {"$regex": f"^{name}$", "$options": "i"}}, {"_id": 0})
        if doctor:
            return {"doctor": doctor}
        return {"error": "Doctor not found"}
    except Exception as e:
        return {"error": f"Failed to fetch doctor: {str(e)}"}