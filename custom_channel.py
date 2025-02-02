from rasa.core.channels.channel import InputChannel, UserMessage, CollectingOutputChannel
from sanic import Blueprint, response
from sanic.request import Request
import openai

class OpenAIInputChannel(InputChannel):
    def name(self) -> str:
        return "openai"

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint("custom_webhook", __name__)

        @custom_webhook.route("/", methods=["POST"])
        async def receive(request: Request):
            payload = request.json
            user_message = payload.get("message")
            sender_id = payload.get("sender", "default")

            # Appeler OpenAI pour générer une réponse
            openai.api_key = "votre_clé_api"
            completion = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_message,
                max_tokens=150,
                temperature=0.7
            )
            response_text = completion.choices[0].text.strip()

            # Envoyer une réponse au client
            output_channel = CollectingOutputChannel()
            await on_new_message(UserMessage(user_message, output_channel, sender_id))
            return response.json({"response": response_text})

        return custom_webhook
