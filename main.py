from flask import Flask, request, jsonify
from google.appengine.api import wrap_wsgi_app
from google.appengine.api.mail import send_mail
import os

app = Flask(__name__)
app.wsgi_app = wrap_wsgi_app(app.wsgi_app)

# https://emailtest-2yhs5ice4q-tl.a.run.app/sendemail
data_store = None

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sendemail")
def sendMail():
    send_mail(sender= "aureliano.paiva@grupofleury.com.br",
                  to= "sanchobuendia@gmail.com",
                  subject="Testing Python3 sending mails",
                    body="""Dear Albert:
    
                        Your example.com account has been approved.  You can now visit
                        http://www.example.com/ and sign in using your Google Account to
                        access new features.
    
                        Please let us know if you have any questions.
    
                        The example.com Team
                        """)

    return "Mail was sent"

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