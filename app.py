from flask import Flask, render_template
from api import api_blueprint  # Import the API blueprint

app = Flask(__name__, static_folder='static', template_folder='templates')

# Register API blueprint
app.register_blueprint(api_blueprint)

@app.route('/')
def home():
    return render_template('index7.html')

if __name__ == '__main__':
    app.run(debug=True)
