from nicegui import ui
import requests
import os

KEYGEN_URL = os.getenv("KEYGEN_URL", "http://keygen:5001")
PDF_URL = os.getenv("PDF_URL", "http://pdf:5002")

def generate_key():
    r = requests.get(f"{KEYGEN_URL}/generate")
    if r.status_code == 200:
        data = r.json()
        ui.label(f"Public Key: {data['public_key']}")
        ui.image(data['qr'])
    else:
        ui.notify("Error generating key", color="negative")

def download_pdf():
    r = requests.get(f"{PDF_URL}/pdf")
    if r.status_code == 200:
        with open("keypair.pdf", "wb") as f:
            f.write(r.content)
        ui.notify("PDF downloaded", color="positive")
    else:
        ui.notify("Error generating PDF", color="negative")

def show_history():
    r = requests.get(f"{PDF_URL}/history")
    if r.status_code == 200:
        for key in r.json():
            ui.label(f"{key['public_key']} at {key['generated_at']}")
    else:
        ui.notify("Error loading history", color="negative")

with ui.row():
    ui.button("Generate Key", on_click=generate_key)
    ui.button("Download PDF", on_click=download_pdf)
    ui.button("Show History", on_click=show_history)

ui.run(port=8080, host="0.0.0.0")
