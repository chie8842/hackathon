from flask import Flask, request, jsonify
from logger import logger_config


# logger
# logger = logger_config('test', loglevel='WARN', log_file='log/log.txt')
# logger.warning('This is the test logging')


app = Flask(__name__)

@app.route('/vectorize_all', methods=['POST'])
def vectorize_all():
    # Your logic for vectorize_all endpoint here
    # Example: vectorize all data sent in the request
    data = request.json
    # Perform vectorization
    # vectorized_data = vectorize(data)
    return jsonify({"message": "Vectorization of all data performed successfully"})

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
