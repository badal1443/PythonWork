import json
import ssl
from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv()

mongo_user = os.getenv("MONGO_DB_USER")
mongo_password = os.getenv("MONGO_DB_PASSWORD")
mongo_database = os.getenv("MONGO_DATABASE")
mongo_collection = os.getenv("MONGO_COLLECTION")

uri = f"mongodb+srv://{mongo_user}:{mongo_password}@cluster0.v5vloye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server with proper SSL configuration
client = MongoClient(uri, 
                    tls=True,
                    tlsAllowInvalidCertificates=True,
                    tlsAllowInvalidHostnames=True,
                    serverSelectionTimeoutMS=5000,
                    connectTimeoutMS=10000,
                    socketTimeoutMS=10000)
# Send a ping to confirm a successful connection
try:
    print("Testing MongoDB connection...")
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")

    curr_dir = os.getcwd()
    print(f"📁 Current working directory: {curr_dir}")

    file_path = os.path.join(curr_dir, 'MyFastAPIs/doctors.json')
    print(f"🔍 Looking for doctors.json file at: {file_path}")

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        print("📋 Files in current directory:")
        for file in os.listdir(curr_dir):
            print(f"   - {file}")
        exit(1)

    print("📖 Reading doctors.json file...")
    with open(file_path) as doctors_file:
        doctors_data = json.load(doctors_file)
        
    print(f"📊 Loaded {len(doctors_data)} records from JSON file")
    
    # Validate data structure
    if not isinstance(doctors_data, list):
        print("❌ Error: doctors_data should be a list of documents")
        print(f"   Actual type: {type(doctors_data)}")
        exit(1)
        
    # Select database and collection from environment variables
    db = client[mongo_database]
    collection = db[mongo_collection]
    
    print(f"📄 Using database: {mongo_database}")
    print(f"📄 Using collection: {mongo_collection}")
    
    print("🧹 Clearing existing data from collection...")
    delete_result = collection.delete_many({})
    print(f"   Deleted {delete_result.deleted_count} existing documents")
    
    print("📝 Inserting new documents...")
    result = collection.insert_many(doctors_data)
    print(f"✅ Successfully inserted {len(result.inserted_ids)} doctors into the collection.")
    
except Exception as e:
    print(f"❌ Error occurred: {type(e).__name__}: {e}")
    import traceback
    print("📋 Full error details:")
    traceback.print_exc()
