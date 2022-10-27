from flask import Flask, render_template, request, session, redirect
import requests
import os
import time

app = Flask(__name__)
last_push = 0

# Significantly smaller than beepboop actual time
# but high enough to smooth out network latency, etc.
# when using polling mode
CUTOFF_TIME = 8

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

# Allows for polling access
@app.route("/api/state", methods=["GET"])
def state():
    return str(int((time.time() - last_push) < CUTOFF_TIME))

@app.route("/api/push", methods=["POST"])
def push():
    global last_push
    tmp = last_push
    last_push = time.time()

    print("Beeping the boop")
    if (time.time() - tmp) > CUTOFF_TIME:
        try:
            requests.get(os.environ["BEEPBOOP_URL"], timeout=3)
        except:
            print("Beepboop is offline.")

    return "OK"

# for debug only; prod should run on gunicorn
def main():
    app.run("0.0.0.0", port=6331)

if __name__ == "__main__":
    main()
