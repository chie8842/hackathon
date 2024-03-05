import argparse
from flask import Flask
from flask import request
from flask import jsonify
from logger import logger_config
import boto3

from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
import params

# logger
# logger = logger_config('test', loglevel='WARN', log_file='log/log.txt')
# logger.warning('This is the test logging')

apikey = params.apikey

# TODO: add integration to get openAI api key from AWS Secret manager
def get_api_key():
    return apikey


app = Flask(__name__)

@app.route('/vectorize_all', methods=['POST'])
def vectorize_all():
    # Your logic for vectorize_all endpoint here
    # Example: vectorize all data sent in the request
    connection_string = request.json['connection_string']
    db = request.json['']
    # Perform vectorization
    # vectorized_data = vectorize(data)
    #return jsonify({"message": "Vectorization of all data performed successfully"})
    return data

@app.route('/vectorize_auto', methods=['POST'])
def vectorize_auto():
    # Your logic for vectorize_auto endpoint here
    # Example: automatically detect data type and vectorize
    data = request.json
    # Perform auto vectorization
    # vectorized_data = auto_vectorize(data)
    return jsonify({"message": "Automatic vectorization performed successfully"})

@app.route('/vectorize_manual', methods=['POST'])
def vectorize_manual():
    # Your logic for vectorize_manual endpoint here
    # Example: manually specify parameters for vectorization
    data = request.json
    # Perform manual vectorization
    # vectorized_data = manual_vectorize(data)
    return jsonify({"message": "Manual vectorization performed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
