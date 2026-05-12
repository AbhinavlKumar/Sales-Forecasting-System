import os
from flask import Flask

# Import main function from your analysis file
from sales_forecast import main

app = Flask(__name__)

@app.route("/")
def home():
    # Run analysis
    main()

    return "Sales Data Analysis Completed Successfully"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)