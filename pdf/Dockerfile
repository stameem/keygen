FROM python:3.11-slim
WORKDIR /app
COPY pdf_service.py .
RUN pip install fastapi uvicorn reportlab mysql-connector-python
CMD ["uvicorn", "pdf_service:app", "--host", "0.0.0.0", "--port", "5002"]
