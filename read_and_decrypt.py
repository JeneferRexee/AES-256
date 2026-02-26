from pymongo import MongoClient
import json
from crypto_utils import decrypt_data

client = MongoClient("mongodb://localhost:27017/")
db = client["ocr_database"]
collection = db["ocr_results"]

# Fetch document
doc = collection.find_one({"companyId": "123"})

# Decrypt AFTER reading
decrypted_ocr = decrypt_data(doc["encrypted_ocr_text"])
decrypted_json = decrypt_data(doc["encrypted_json_output"])

# Convert back to original format
decrypted_ocr = json.loads(decrypted_ocr)
decrypted_json = json.loads(decrypted_json)

print("Decrypted OCR:", decrypted_ocr)
print("Decrypted JSON:", decrypted_json)