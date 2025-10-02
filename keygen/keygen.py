from fastapi import FastAPI
import bitcoin
import qrcode
import io
import base64

app = FastAPI()

@app.get("/generate")
def generate_key():
    private_key = bitcoin.random_key()
    public_key = bitcoin.privtopub(private_key)

    # Generate QR
    qr = qrcode.make(public_key)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    qr_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")

    return {
        "private_key": private_key,
        "public_key": public_key,
        "qr": f"data:image/png;base64,{qr_base64}"
    }
