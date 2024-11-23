# app.py
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/run', methods=['POST'])
def run():
    mode = request.form.get('mode')
    count = request.form.get('count')
    delay = request.form.get('delay')
    # Call the TBomb script with the selected mode
    result = subprocess.run(['python3', 'tbomb/bomber.py', f'--{mode}', '--count', count, '--delay', delay], capture_output=True, text=True)
    socketio.emit('update', {'output': result.stdout})
    return jsonify({"output": result.stdout})

if __name__ == '__main__':
    socketio.run(app, debug=True)