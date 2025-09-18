from flask import Flask, request, jsonify
import json

# Load dataset once
with open("units_2025_pretty.json", "r", encoding="utf-8") as f:
    units = json.load(f)

app = Flask(__name__)

@app.route("/units", methods=["GET"])
def search_units():
    q = request.args.get("q", "").lower()
    if not q:
        return jsonify({"totalItems": len(units), "items": units})

    results = []
    for u in units:
        common = u.get("common", {})
        code = common.get("code", "").lower()
        title = common.get("title", "").lower()
        if q in code or q in title:
            results.append(u)

    return jsonify({"totalItems": len(results), "items": results})

@app.route("/units/<code>", methods=["GET"])
def get_unit(code):
    code = code.upper()
    for u in units:
        if u.get("common", {}).get("code") == code:
            return jsonify(u)
    return jsonify({"error": "Unit not found"}), 404

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
