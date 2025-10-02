FROM python:3.11-slim
WORKDIR /app
COPY keygen.py .
RUN pip install fastapi uvicorn bitcoin qrcode
CMD ["uvicorn", "keygen:app", "--host", "0.0.0.0", "--port", "5001"]
