# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import urllib3
from rasa_sdk.events import AllSlotsReset, SessionStarted, ActionExecuted

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        email = tracker.get_slot("email")
        print(email)
        businessName = tracker.get_slot("businessName")
        print(businessName)

        # TODO: über status codes zurück schicken ob es geklappt hat  oder nicht
        http = urllib3.PoolManager()
        encoded_body = json.dumps({
        "email": email,
        "businessName": businessName,
        })
        r = http.request('POST', 'https://us-central1-innocard-prod.cloudfunctions.net/sendEmail',
                 headers={'Content-Type': 'application/json'},
                 body=encoded_body)

        response = r.status
        if response == 200:
            dispatcher.utter_message(text="Wir haben deine Daten erfolgreich gesendet. Klicke auf diesen Link, um zu erfahren, wie es weiter geht: https://innocard-dev.web.app/onboarding?success=true")
        else :
            dispatcher.utter_message(text="Etwas ist schief gelaufen, bitte probiere es erneut.")

        return []

class ResetSlot(Action):
    def name(self) -> Text:
        return "action_reset_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Erfolgreich zurückgesetzt.")

        # Return the function to run it
        return [AllSlotsReset()]

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hi :)")

        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))

        return events