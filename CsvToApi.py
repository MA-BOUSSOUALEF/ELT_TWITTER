from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Charger les données CSV
def load_data():
    try:
        return pd.read_csv('refined_tweets.csv')
    except FileNotFoundError:
        return pd.DataFrame()  # Si le fichier n'existe pas, retourner un DataFrame vide

# Sauvegarder les données dans le fichier CSV
def save_data(df):
    df.to_csv('refined_tweets.csv', index=False)

# Initialiser les données
df = load_data()
df = df[['id', 'author', 'content', 'language', 'number_of_likes', 'number_of_shares', 'date_time']]

@app.route('/api/data', methods=['GET'])
def get_data():
    """Retourner toutes les données."""
    data = df.to_dict(orient='records')  # Convertir le DataFrame en liste de dictionnaires
    return jsonify(data)

@app.route('/api/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    """Retourner les données pour un ID spécifique."""
    record = df[df['id'] == id]  # Filtrer par ID
    if record.empty:
        return jsonify({'error': 'ID not found'}), 404
    return jsonify(record.to_dict(orient='records')[0])

@app.route('/api/data', methods=['POST'])
def add_data():
    """Ajouter une nouvelle ligne à partir des données JSON."""
    new_data = request.get_json()
    global df  # Utiliser la variable globale
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    save_data(df)  # Sauvegarder les modifications dans le CSV
    return jsonify({'message': 'Data added successfully'}), 201

@app.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    """Supprimer une ligne par ID."""
    global df
    df = df[df['id'] != id]  # Supprimer les données avec cet ID
    save_data(df)  # Sauvegarder les modifications dans le CSV
    return jsonify({'message': 'Data deleted successfully'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
