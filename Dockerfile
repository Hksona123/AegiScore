FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Set up a non-root user for Hugging Face Spaces
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Create app directories and set ownership early
USER root
RUN mkdir -p /app/instance /app/data && chown -R user:user /app
USER user

# Install python dependencies from the Server folder
COPY --chown=user:user Server/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the rest of the Server folder
COPY --chown=user:user Server/ .

EXPOSE 7860

# Run the Flask server
CMD ["gunicorn", "--worker-class", "eventlet", "-w", "1", "-b", "0.0.0.0:7860", "run:app"]
