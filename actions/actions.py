from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHandleResponse(Action):

    def name(self) -> Text:
        return "action_handle_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Récupérer le message utilisateur
        user_message = tracker.latest_message.get("text", "")

        # Si le message utilisateur est vide
        if not user_message:
            dispatcher.utter_message("Je n'ai pas compris votre demande.")
            return []

        # Ajouter une réponse statique ou traiter dynamiquement le message utilisateur
        dispatcher.utter_message(f"Vous avez dit : {user_message}")
        return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re


class ActionPerformCalculation(Action):

    def name(self) -> Text:
        return "action_perform_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Récupérer le texte de l'utilisateur
        user_message = tracker.latest_message.get('text')

        # Identifier les nombres et l'opération
        pattern = r"(\d+)\s*([\+\-\*\/])\s*(\d+)"
        match = re.search(pattern, user_message)

        if match:
            num1 = float(match.group(1))
            operator = match.group(2)
            num2 = float(match.group(3))

            # Effectuer le calcul
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2 if num2 != 0 else "Erreur : division par zéro"
            else:
                result = "Opération non reconnue"
        else:
            result = "Je n'ai pas pu comprendre votre calcul. Veuillez vérifier votre syntaxe."

        # Envoyer la réponse
        dispatcher.utter_message(text=f"Le résultat est : {result}")
        return []
