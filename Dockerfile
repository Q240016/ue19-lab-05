FROM python:3

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier de dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste de l'application
COPY app.py .

# Commande par défaut lors du démarrage du conteneur
CMD ["python", "app.py"]
