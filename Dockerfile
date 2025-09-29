FROM ubuntu:latest
WORKDIR /app
COPY app.py .
run apt-get update && apt install -y  python3

CMD ["python3", "app.py"]
