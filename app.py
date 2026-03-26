from flask import Flask, request, jsonify
from services.ocr_service import extract_text
from services.kyc_service import verify_kyc
from services.aml_service import aml_check
from services.risk_engine import calculate_risk
from utils.validator import validate_input
from utils.logger import log
from models import save_transaction, init_db
from auth import generate_token
from services.pdf_service import generate_welcome_kit

app = Flask(__name__)

# INIT DB
init_db()

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == "1234":
        token = generate_token(data["username"])
        return jsonify({"token": token})
    return jsonify({"error": "Invalid login"}), 401


# MAIN API
@app.route("/api/process-account", methods=["POST"])
def process_account():
    data = request.json

    valid, msg = validate_input(data)
    if not valid:
        return jsonify({"error": msg}), 400

    log("Processing started")

    extracted = extract_text(data.get("documents", []))

    if not verify_kyc(extracted):
        return jsonify({"error": "KYC Failed"}), 400

    if not aml_check(data.get("name")):
        return jsonify({"error": "Blacklisted"}), 403

    score, level = calculate_risk(data)

# ✅ Generate PDF
    pdf_file = generate_welcome_kit(data)
    
    # Save in DB
    save_transaction(data, score, level)
    
    log("Processing completed")
    
    return jsonify({
        "status": "SUCCESS",
        "risk_score": score,
        "risk_level": level,
        "welcome_kit": pdf_file   # ✅ Added this
    })


# VIEW TRANSACTIONS
@app.route("/transactions", methods=["GET"])
def transactions():
    from database import get_connection
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    data = cur.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
