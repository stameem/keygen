from fastapi import FastAPI, Response
import mysql.connector, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "btcuser")
DB_PASS = os.getenv("DB_PASS", "btcpass")
DB_NAME = os.getenv("DB_NAME", "btcdb")

def get_db():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME
    )

@app.get("/history")
def history():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT public_key, generated_at FROM keys ORDER BY generated_at DESC LIMIT 100")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/pdf")
def pdf():
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    c.drawString(100, 750, "Bitcoin Keypair")
    c.drawString(100, 700, "Demo PDF from BTC_Keygen Microservice")
    c.showPage()
    c.save()
    buf.seek(0)
    return Response(content=buf.read(), media_type="application/pdf")
