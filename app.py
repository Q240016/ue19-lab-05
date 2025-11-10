import requests

def get_random_joke():
    # URL de l'API publique (mode "safe" pour éviter le contenu inapproprié)
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    
    try:
        response = requests.get(url)
        # Lève une exception si la requête a échoué (ex: erreur 404, 500)
        response.raise_for_status()
        
        data = response.json()
        
        # JokesAPI peut renvoyer deux types de blagues : 'single' (une ligne) ou 'twopart' (question/réponse)
        print("\n--- BLAGUE ---")
        if data['type'] == 'single':
            print(data['joke'])
        else:
            print(f"{data['setup']}\n> {data['delivery']}")
        print("----------------\n")
            
    except Exception as e:
        print(f"Une erreur est survenue lors de la récupération de la blague : {e}")

if __name__ == "__main__":
    get_random_joke()
