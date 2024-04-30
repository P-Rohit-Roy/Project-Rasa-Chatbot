from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractVehicleEntity(Action):

    def name(self) -> Text:
        return "action_order_vehicle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        vehicle_entity = next(tracker.get_latest_entity.values('vehicle'), None)

        if vehicle_entity:

            dispatcher.utter_message(text=f"Please select {vehicle_entity}as your vehicle.")

        else:
            dispatcher.utter_message(text=f"Sorry you have not selected your vehicle.")

            return[]

class SelectVehicleEntity(Action):
    def name(self) -> Text:
        return "action_select_vehicle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Select your vehicle.")


class ConfirmVehicle(Action):
    def name(self) -> Text:
        return "action_confirm_vehicle"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        vehicle_entity = next(tracker.get_latest_entity.values('vehicle'), None)

        if vehicle_entity:

            dispatcher.utter_message(text=f"I have Selected{vehicle_entity}as the vehicle.")

        else:
            dispatcher.utter_message(text=f"Sorry you have not selected your vehicle.")

            return[]

