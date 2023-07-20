import subprocess
from flask import Flask, request, send_from_directory, jsonify
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__)
app.config['FLASK_HTPASSWD_PATH'] = 'C:\\Users\\Pasharet\\Documents\\GitHub\\usbsrvcmd-web\\.htpasswd'
htpasswd = HtPasswdAuth(app)

valid_commands = [
'usbsrvcmd disconnect 0',
'usbsrvcmd disconnect 1',
'usbsrvcmd disconnect 2',
'usbsrvcmd disconnect 3',
'usbsrvcmd disconnect 4',
'usbsrvcmd disconnect 5',
'usbsrvcmd disconnect 6',
'usbsrvcmd disconnect 7',
'usbsrvcmd disconnect 8',
'usbsrvcmd disconnect 9',
'usbsrvcmd list -o',
'shutdown /r'
]

@app.route('/')
@htpasswd.required
def index(user):
    return send_from_directory('.', 'index.htm')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/main.css')
def css():
    return send_from_directory('.', 'main.css')

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

@app.route('/estgenpas.htm')
def estgenpas():
    return send_from_directory('.', 'estgenpas.htm')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
