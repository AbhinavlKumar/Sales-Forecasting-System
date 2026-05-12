from flask import Flask, render_template, send_file
import os

from sales_forecast import main, CHART_FILE

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run-analysis")
def run_analysis():
    main()
    return send_file(CHART_FILE, mimetype="image/png")

@app.route("/upload", methods=["POST"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
