import subprocess
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

valid_commands = ['usbsrvcmd disconnect 0', 'usbsrvcmd disconnect 1', 'usbsrvcmd disconnect 2', 'usbsrvcmd disconnect 3']

@app.route('/execute', methods=['POST'])
def execute_command():
    command = request.form.get('command')
    if command in valid_commands:
        try:
            result = subprocess.check_output(command, shell=True)
            return result
        except subprocess.CalledProcessError as e:
            return f"Command execution error: {str(e)}"
    else:
        return jsonify(error="Invalid command!")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return send_from_directory('.', 'index.htm')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
