# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .

# Install dependencies into a dedicated virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage (non-root)
FROM python:3.11-slim

WORKDIR /app

# Copy the pre-built virtual environment
COPY --from=builder /opt/venv /opt/venv
COPY main.py .

# Put virtualenv binaries in PATH
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Create a non-root system user and set ownership
RUN useradd -u 10001 -m appuser && \
    chown -R appuser:appuser /app

USER 10001

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]