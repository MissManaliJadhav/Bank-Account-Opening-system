from database import get_connection

def save_transaction(data, risk_score, risk_level):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            name TEXT,
            amount FLOAT,
            source TEXT,
            risk_score INT,
            risk_level TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO transactions (name, amount, source, risk_score, risk_level)
        VALUES (%s, %s, %s, %s, %s)
    """, (data["name"], data["amount"], data["source"], risk_score, risk_level))

    conn.commit()
    cursor.close()
    conn.close()
