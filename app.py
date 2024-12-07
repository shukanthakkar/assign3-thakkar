from flask import Flask
import socket
import requests

app = Flask(__name__)

# Get hostname and IP address
hostname = socket.gethostname()

def get_external_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except Exception as e:
        return f"Error retrieving IP: {e}"

ip_address = get_external_ip()

@app.route("/")
def hello_cloud():
    return "Hello from thakkar ECS Container"

@app.route("/host")
def host_name():
    return f"Hostname: {hostname}"

@app.route("/ip")
def host_ip():
    return f"IP Address: {ip_address}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
