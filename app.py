from flask import Flask, request, jsonify
import json
import os

# Load dataset once into memory
with open("units_2025_pretty.json", "r", encoding="utf-8") as f:
    units = json.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Monash Handbook Dataset API",
        "endpoints": {
            "/units": "Search or list all units (optional ?q= keyword to filter)",
            "/units/<code>": "Get details for a specific unit by code",
            "/health": "Health check"
        }
    })

@app.route("/units", methods=["GET"])
def search_units():
    q = request.args.get("q", "").lower()

    # Filter by query if provided
    results = []
    for u in units:
        common = u.get("common", {})
        code = common.get("code", "").lower()
        title = common.get("title", "").lower()
        if not q or q in code or q in title:
            results.append(u)

    return jsonify({
        "totalItems": len(results),
        "items": results
    })

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
    port = int(os.getenv("PORT", 8080))
    host = os.getenv("HOST", "0.0.0.0")
    app.run(host=host, port=port)
