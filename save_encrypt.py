from pymongo import MongoClient
from datetime import datetime
import json
from crypto_utils import encrypt_data

# Connect MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")
db = client["ocr_database"]
collection = db["ocr_results"]

# Example OCR + JSON data
pages_text = ["This is page 1", "This is page 2"]
json_output = {"lease_start": "01-01-2025", "tenant": "ABC Corp"}

# Convert to string before encryption
pages_text_str = json.dumps(pages_text)
json_output_str = json.dumps(json_output)

#  Encrypt BEFORE saving
encrypted_ocr = encrypt_data(pages_text_str)
encrypted_json = encrypt_data(json_output_str)

# Save ONLY encrypted data
document = {
    "companyId": "123",
    "dropboxid": "456",
    "encrypted_ocr_text": encrypted_ocr,
    "encrypted_json_output": encrypted_json,
    "created_at": datetime.utcnow()
}

collection.insert_one(document)

print(" Encrypted data saved to MongoDB")