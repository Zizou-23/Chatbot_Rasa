from tkinter import *
import requests

# URL de l'API Rasa
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

# Fonction pour envoyer un message au bot
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return

    chat_log.insert(END, f"Vous: {user_message}\n")
    user_input.delete(0,END)

    # Envoyer le message à l'API Rasa
    try:
        response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
        if response.status_code == 200:
            bot_responses = response.json()
            if bot_responses:
                for bot_response in bot_responses:
                    bot_message = bot_response.get("text", "")
                    if bot_message:
                        chat_log.insert(END, f"Bot: {bot_message}\n")
            else:
                chat_log.insert(END, "Bot: Je n'ai pas compris votre message.\n")
        else:
            chat_log.insert(END, "Bot: Erreur lors de la connexion au serveur Rasa.\n")
    except Exception as e:
        print(f"Erreur lors de l'appel à Rasa : {e}")
        chat_log.insert(END, "Bot: Erreur lors de la connexion au serveur.\n")



BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root = Tk()

root.title("Chatbot Rasa")
screen_x = int(root.winfo_screenwidth())
screen_y = int(root.winfo_screenheight())
root_x = 800
root_y = 600

posX = (screen_x //2) - (root_x //2)
posY = (screen_y //2) - (root_y //2)
geo = "{}x{}+{}+{}".format(root_x,root_y,posX,posY)

root.geometry(geo)
root.resizable(width=False, height=False)
#root.configure(width=470, height=550, bg=BG_COLOR)

head_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR,
                   text="BIENVENUE SUR CHATBOT RASA", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)

# tiny divider
line = Label(root, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)

chat_log = Text(root, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                        font=FONT, padx=5, pady=5)
chat_log.place(relheight=0.745, relwidth=1, rely=0.08)


scrollbar = Scrollbar(chat_log,command=chat_log.yview)
scrollbar.place(relheight=1, relx=0.974)
chat_log['yscrollcommand'] = scrollbar.set

bottom_label = Label(root, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

user_input = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
user_input.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
user_input.focus()

"sendimg=PhotoImage(file='sent.png')"
send_button = Button(bottom_label, text="Envoyer", font=FONT_BOLD, width=20, bg=BG_GRAY,command=send_message)
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


root.mainloop()
