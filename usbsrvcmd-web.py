import subprocess
from flask import Flask, request, jsonify
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__, static_url_path='')
app.config['FLASK_HTPASSWD_PATH'] = 'C:\\Users\\Pasharet\\Documents\\GitHub\\usbsrvcmd-web\\static\\.htpasswd'
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
def root(user):
    return app.send_static_file('usbsrvcmd-web.htm')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
