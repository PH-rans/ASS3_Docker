# Basis-Image mit Python 3.10
FROM python:3.10

# Arbeitsverzeichnis für alle folgenden Befehle
WORKDIR /app

# COPY lädt nur requirements.txt ins Container-Image
COPY requirements.txt ./

# Installiere Abhängigkeiten (Flask + MySQL Connector)
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere danach den Anwendungs-Code
COPY main.py ./

# Gib Port 5000 für Docker frei (Dokumentationszweck)
EXPOSE 5000

# Starte die App
CMD ["python", "main.py"]


