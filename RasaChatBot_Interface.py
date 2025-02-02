import tkinter as tk
import requests

# URL de l'API Rasa
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Fonction pour envoyer un message au bot
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return

    chat_log.insert(tk.END, f"Vous: {user_message}\n")
    user_input.delete(0, tk.END)

    # Envoyer le message à l'API Rasa
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
        if response.status_code == 200:
            bot_responses = response.json()
            if bot_responses:
                for bot_response in bot_responses:
                    bot_message = bot_response.get("text", "")
                    if bot_message:
                        chat_log.insert(tk.END, f"Bot: {bot_message}\n")
            else:
                chat_log.insert(tk.END, "Bot: Je n'ai pas compris votre message.\n")
        else:
            chat_log.insert(tk.END, "Bot: Erreur lors de la connexion au serveur Rasa.\n")
    except Exception as e:
        print(f"Erreur lors de l'appel à Rasa : {e}")
        chat_log.insert(tk.END, "Bot: Erreur lors de la connexion au serveur.\n")

# Interface Tkinter
root = tk.Tk()
root.title("Chatbot Rasa")

chat_frame = tk.Frame(root)
chat_frame.pack(padx=10, pady=10)

chat_log = tk.Text(chat_frame, width=50, height=20, state=tk.NORMAL)
chat_log.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(chat_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log['yscrollcommand'] = scrollbar.set

user_input = tk.Entry(root, width=40)
user_input.pack(pady=10)

send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack()

root.mainloop()
