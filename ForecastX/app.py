import os
from flask import Flask, send_file, jsonify

from sales_forecast import main, CHART_FILE

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Sales Forecast Analysis API Running"
    })


@app.route("/run-analysis")
def run_analysis():
    try:
        chart_path = main()

        return jsonify({
            "message": "Analysis completed successfully",
            "chart": str(chart_path.name)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/chart")
def get_chart():
    if CHART_FILE.exists():
        return send_file(CHART_FILE, mimetype="image/png")

    return jsonify({
        "error": "Chart not found. Run analysis first."
    }), 404


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
