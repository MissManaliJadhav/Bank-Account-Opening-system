from flask import Flask, request, jsonify
from services.ocr_service import extract_text
from services.kyc_service import verify_kyc
from services.aml_service import aml_check
from services.risk_engine import calculate_risk
from models import save_transaction
from utils.logger import log

app = Flask(__name__)

@app.route("/api/process-account", methods=["POST"])
def process_account():
    try:
        data = request.json

        log("Received request")

        # OCR
        extracted = extract_text(data.get("documents", []))

        # KYC
        if not verify_kyc(extracted):
            return jsonify({"status": "FAIL", "reason": "KYC Failed"}), 400

        # AML
        if not aml_check(data.get("name")):
            return jsonify({"status": "FAIL", "reason": "Blacklisted"}), 403

        # Risk
        score, level = calculate_risk(data)

        # Save
        save_transaction(data, score, level)

        log("Processed successfully")

        return jsonify({
            "status": "SUCCESS",
            "risk_score": score,
            "risk_level": level
        })

    except Exception as e:
        log(str(e))
        return jsonify({"status": "ERROR", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
