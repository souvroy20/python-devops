import psutil
import subprocess
import sys
import os
from flask import Flask, render_template

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")

install_requirements()

# app = Flask(__name__)

# @app.route("/")
# def index():
#     cpu_percent = psutil.cpu_percent()
#     mem_percent = psutil.virtual_memory().percent
#     message = None
#     if cpu_percent > 80 or mem_percent > 80:
#         message = "SOUVICK!! High CPU or memory utilization detected!"
#     return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0',port=5001)

app = Flask(__name__)

# Configuration from environment variables with defaults
CPU_THRESHOLD = int(os.environ.get('CPU_THRESHOLD', 80))
MEM_THRESHOLD = int(os.environ.get('MEM_THRESHOLD', 80))

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > CPU_THRESHOLD or mem_percent > MEM_THRESHOLD:
        message = f"High CPU ({cpu_percent}%) or memory ({mem_percent}%) utilization detected!"
    return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)

@app.route("/data")
def data():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return jsonify({"cpu_percent": cpu_percent, "mem_percent": mem_percent})

if __name__ == '__main__':
    # For production, it's better to use a production-ready WSGI server like Gunicorn or Waitress.
    # The debug flag should be turned off in production.
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
