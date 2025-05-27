from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("data.xlsx", engine="openpyxl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    number = request.form['number']
    result = df[df.iloc[:, 0].astype(str) == number]
    if not result.empty:
        querschnitt = result.iloc[0, 5]  # Column F
        return jsonify({"Querschnitt": querschnitt})
    else:
        return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
