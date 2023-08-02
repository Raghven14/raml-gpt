from flask import Flask, render_template, request, send_file, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_raml', methods=['POST'])
def generate_raml():
    sample_data = request.form['sample_data']
    http_method = request.form['http_method']

    try:
        # Validate JSON structure
        parsed_data = json.loads(sample_data)
    except json.JSONDecodeError:
        # If the JSON is invalid, return an error message
        error_msg = "Invalid JSON structure. Please provide a valid JSON object."
        return render_template('result.html', error_msg=error_msg)

    # Your logic to generate RAML specifications goes here
    # For demonstration purposes, let's just convert the data to upper case
    converted_data = sample_data.upper()

    # Save the converted data to a text file
    filename = save_to_file(converted_data)

    return render_template('result.html', converted_data=converted_data, filename=filename)

def save_to_file(data):
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
    with open('static/' + filename, 'w') as file:
        file.write(data)
    return filename

if __name__ == '__main__':
    app.run(debug=True)