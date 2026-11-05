FROM python:3.11-slim

WORKDIR /app

COPY persistent_auditor.py .
COPY product.py .
COPY inventory.py .
COPY inventory.json .
COPY physical_product.py .
COPY can_be_shipped.py .
COPY digital_product.py .

CMD ["python", "persistent_auditor.py"]