from flask import Blueprint, request, jsonify
from pymongo import MongoClient

worker_routes = Blueprint('worker_routes', __name__)

client = MongoClient("mongodb://localhost:27017/")  # Conecta ao MongoDB
db = client["workers"]  # Nome do banco de dados
workers_collection = db["workers"]  # Nome da coleção

@worker_routes.route('/workers', methods=['POST'])
def add_worker():
    data = request.get_json()
    # Verifica se os campos obrigatórios estão presentes
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
