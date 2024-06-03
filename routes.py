import os
from flask import Blueprint, request, jsonify
from database import Database

worker_routes = Blueprint('worker_routes', __name__)

# Conecta ao MongoDB
mongo_password = os.environ.get('MONGO_PASSWORD')
uri = f"mongodb+srv://carlavprudencio:{mongo_password}@studies.h33rdll.mongodb.net/"
db = Database(uri)
workers_collection = db.get_collection("workers")

@worker_routes.route('/workers', methods=['POST'])
def add_worker():
    data = request.get_json()
    required_fields = ['name', 'phone', 'neighborhood', 'city', 'state', 'category']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo obrigatório '{field}' ausente"}), 400
    workers_collection.insert_one(data)
    return jsonify({"message": "Worker added successfully"}), 200

@worker_routes.route('/workers', methods=['GET'])
def get_workers():
    workers = list(workers_collection.find())
    return jsonify({"workers": workers}), 200

@worker_routes.route('/workers/<category>', methods=['GET'])
def get_workers_by_category(category):
    workers = list(workers_collection.find({"category": category}))
    return jsonify({"workers": workers}), 200
