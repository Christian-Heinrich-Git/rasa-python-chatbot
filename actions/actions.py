# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import urllib3
from rasa_sdk.events import AllSlotsReset

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionFetchData(Action):

    def name(self) -> Text:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # TODO: über status codes zurück schicken ob es geklappt hat  oder nicht
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://localhost:5001/innocard-prod/us-central1/createAccount?email=mytest@mail')
        print("hier steht r.data: ", r.data)
        response = r.status
        if response == 200:
            dispatcher.utter_message(text="gut")
        else :
            dispatcher.utter_message(text="blöd")

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