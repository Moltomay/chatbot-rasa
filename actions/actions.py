# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class AgeCnssFr(Action):

    def name(self) -> Text:
        return "action_age_cnss_fr"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_age = next(tracker.get_latest_entity_values("age"), None)
        current_age_int=int(current_age)

        if current_age_int>=18:
            dispatcher.utter_message(text="Vous pouvez cotiser.")
            return []
        else :
            dispatcher.utter_message(text="Vous ne pouvez pas cotiser.")
            return []


class AgeCnssAr(Action):

    def name(self) -> Text:
        return "action_age_cnss_ar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_age = next(tracker.get_latest_entity_values("سن"), None)
        current_age_int=int(current_age)

        if current_age_int>=18:
            dispatcher.utter_message(text="يمكنك المساهمة")
            return []
        else :
            dispatcher.utter_message(text="لا يمكنك المساهمة")
            return []

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
