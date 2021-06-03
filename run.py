from janes_voyages import app
import os

flask_host = os.environ.get("FLASK_IP", "127.0.0.1")
flask_port = os.environ.get("FLASK_PORT", 5000)
app.run(host=flask_host, port=flask_port)