print("Starting script...")  # Debug print

from flask import Flask
print("Flask imported successfully")  # Debug print

app = Flask(__name__)
print("Flask app created")  # Debug print

@app.route('/')
def home():
    return "<h1>Hello, Flask is working!</h1>"

print("Route defined")  # Debug print

# Remove the if __name__ == '__main__' check and directly run the app
print("About to start Flask server...")  # Debug print
app.run(debug=True, port=5000, host='127.0.0.1')
print("After Flask run call")  # Debug print