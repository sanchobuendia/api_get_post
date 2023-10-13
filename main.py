from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Create a variable to store the posted dictionary
data_store = None

@app.route('/api/post_dict', methods=['POST'])
def post_data():
    try:
        global data_store  # Access the global data_store variable

        # Get the JSON data from the request
        request_data = request.get_json()

        if request_data:
            # Store the received data in data_store
            data_store = request_data
            return jsonify({"message": "Data received successfully."}), 201
        else:
            return jsonify({"error": "Invalid data format."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/get_dict', methods=['GET'])
def get_data():
    # Return the data stored in data_store
    if data_store:
        return jsonify({"data": data_store})
    else:
        return jsonify({"message": "No data available."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# gcloud run deploy