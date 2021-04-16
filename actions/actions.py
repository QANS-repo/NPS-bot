from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
from rasa_sdk.events import SlotSet, FollowupAction, EventType
from rasa_sdk.forms import FormAction
import csv

import gspread
import time


class NPSForm(FormAction):
    """Custom form action to fill all slots (for now only score) required to validate NPS score provided."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "nps_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["nps_score"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "nps_score": self.from_entity(entity="number",
                                          not_intent="affirm")}

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_nps_score(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate nps_score value."""

        if self.is_int(value) and 10 >= int(value) >= 0:
            return {"nps_score": value}
        else:
            dispatcher.utter_message(template="utter_form_wrong_nps_score")
            # validation failed, set slot to None
            return {"nps_score": None}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        nps_score = tracker.get_slot('nps_score')
        nps_score = int(nps_score)

        my_text="utter_form_nps_uzasadnienie_detraktor"
        nps_group = "detractor"

        if 7 <= nps_score <= 8:
            my_text="utter_form_nps_uzasadnienie_passive"
            nps_group = "passive"

        if nps_score >= 9:
            my_text="utter_form_nps_uzasadnienie_promotor"
            nps_group = "promotor"

        dispatcher.utter_message(template=my_text)

        connection = SheetQueryingMethods()
        sheet = connection.connect_to_sheet()
        row = connection.prepare_NPSform_data(tracker, nps_group)
        index = 2
        sheet.insert_row(row, index)

        return [SlotSet("nps_group", nps_group)]

class MissingProductForm(FormAction):
    """Custom form action to fill all slots required for Missing Product Form
    Triggered when customer says she had a problem finding product. Asks for details of what was hard to find"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "missing_product_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["missing_product_type", "had_problems_finding_product"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"missing_product_type": self.from_entity(entity="product_type",
                                                 intent=["inform", "dostępność_brak"]),
                "had_problems_finding_product": self.from_trigger_intent(intent="dostępność_brak", value=True)
                }

    def validate_had_problems_finding_product(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """No validation is done this time. Using it only to save . """

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return {"had_problems_finding_product": True}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, do something"""

        dispatcher.utter_message(template="utter_form_missing_product")
        ## this was not working check after retraining

        connection = SheetQueryingMethods()
        connection.submit_action_data_entity(tracker)

        return [SlotSet("had_problems_finding_product", True)]


class ActionSetProductQuality(Action):
    """Uruchamiany w odpowiedzi na intent Dostawa - kopije tekst"""

    def name(self) -> Text:
        return "action_set_product_quality"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)
        return []

class ActionSetProductDesign(Action):
    """Uruchamiany w odpowiedzi na intent Dostawa - kopije tekst"""

    def name(self) -> Text:
        return "action_set_product_design"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []


class ActionSetProductPrice(Action):
    """Uruchamiany w odpowiedzi na intent Dostawa - kopije tekst"""

    def name(self) -> Text:
        return "action_set_product_price"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []


class ProductForm(FormAction):
    """Custom form action to fill all slots required to get product."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "product_form"


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["product_type"]


    def slot_mappings(self) -> Dict[Text, Any]:
        return {"product_type": [self.from_entity(entity="product_type",
                                                 not_intent=["dostępność_brak"]),
                                 self.from_text(not_intent="out_of_scope")
                                 ]}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, display text"""
        dispatcher.utter_message(template="utter_form_product")

        connection = SheetQueryingMethods()
        connection.submit_action_data_entity(tracker)

        return []

class FoodForm(FormAction):
    """Custom form action to fill all slots required to get product."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "food_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["food", "food_mentioned"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"food": self.from_entity(entity="food"),
                "food_mentioned": [self.from_trigger_intent(intent="jedzenie", value=True)]
                }

    def validate_food_mentioned(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """No validation is done this time. Using it only to save data . """

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return {"food_mentioned": True}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        dispatcher.utter_message(
            dispatcher.utter_message(template="utter_form_food_submitted"))
        dispatcher.utter_message(
            dispatcher.utter_message(template="utter_food_form_submitted_links"))
        dispatcher.utter_message(
            dispatcher.utter_message(template="utter_kontynuacja"))

        connection = SheetQueryingMethods()
        connection.submit_action_data_entity(tracker)

        return []



class StoreLocationForm(FormAction):
    """Custom form action to fill all slots required to get product."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "store_location_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["store_location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"store_location": self.from_entity(entity="store_location")}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:
        """Once required slots are filled, do something"""

        connection = SheetQueryingMethods()
        connection.submit_action_data_entity(tracker)

        return []


class ActionSetDelivery(Action):
    """Uruchamiany w odpowiedzi na intent Dostawa - kopije tekst"""

    def name(self) -> Text:
        return "action_set_delivery"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetAssembly(Action):
    """Uruchamiany w odpowiedzi na intent Montaż - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_assembly"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetAssortment(Action):
    """Uruchamiany w odpowiedzi na intent duży asortyment - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_assortment"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetParking(Action):
    """Uruchamiany w odpowiedzi na intent Parking - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_parking"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetProductReturn(Action):
    """Uruchamiany w odpowiedzi na intent Zwrot towaru - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_product_return"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetCheckoutLines(Action):
    """Uruchamiany w odpowiedzi na intent Kolejki - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_checkout_lines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetComplaintStatus(Action):
    """Uruchamiany w odpowiedzi na intent Reklamacje - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_complaint_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetCustomerServiceStatus(Action):
    """Uruchamiany w odpowiedzi na intent Obsługa Klienta  - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_customer_service_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetPromoStatus(Action):
    """Uruchamiany w odpowiedzi na intent Promocje - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_promo_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetStoreSize(Action):
    """Uruchamiany w odpowiedzi na intent wielkość sklepu - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_store_size"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSpentFullDay(Action):
    """Uruchamiany w odpowiedzi na intent Miejsce na cały dzień - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_spent_full_day"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionTooMuchWalking(Action):
    """Uruchamiany w odpowiedzi na intent Za dużo chodzenia  - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_too_much_walking"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []

class ActionSetIsCrowded(Action):
    """Uruchamiany w odpowiedzi na intent Tłok - kopiuje tekst"""

    def name(self) -> Text:
        return "action_set_is_crowded"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        connection = SheetQueryingMethods()
        connection.submit_action_data_intent(tracker)

        return []


class SheetQueryingMethods:
    """Class to connect to Google Sheet and operate on it"""

    def connect_to_sheet(self):
        """ Connect to Sheet,
        to do: put path to json outside and not use the connection if file is missing"""

        gc = gspread.service_account('actions/credentials.json')
        sheet = gc.open("NPSQANS").sheet1

        return sheet

    def prepare_NPSform_data(self,
                             tracker: Tracker,
                             nps_group):
        """ For custom form get data from tracker and prepare it in a format expected in Sheet"""

        row = [tracker.sender_id,
               time.asctime(time.localtime(time.time())),
               tracker.get_slot("nps_score"),
               nps_group,
               'NPS',
               tracker.latest_message.get('entities')[0]['confidence'],
               tracker.latest_message.get('entities')[0]['value']
               ]
        print(tracker)
        return row

    def prepare_action_data_intent(self, tracker: Tracker):
        """ For custom action, get intent data from tracker and prepare it in a format expected in Sheet.
        """

        row = [tracker.sender_id,
               time.asctime(time.localtime(time.time())),
               tracker.get_slot("nps_score"),
               tracker.get_slot("nps_group"),
               tracker.latest_message.get("intent")['name'],
               tracker.latest_message.get('intent')['confidence'],
               tracker.latest_message.get('text'),
               ]

        return row

    def prepare_action_data_entity(self, tracker: Tracker, extracted_entity):
        """ For custom action, get entity data from tracker and prepare it in a format expected in Sheet.
        """

        row = [tracker.sender_id,
               time.asctime(time.localtime(time.time())),
               tracker.get_slot("nps_score"),
               tracker.get_slot("nps_group"),
               extracted_entity["entity"],
               "Nie obliczane",
               extracted_entity["value"]
               ]

        return row

    def submit_action_data_intent(self, tracker: Tracker):
        """ Prepare intent entry and save in sheet """

        sheet = self.connect_to_sheet()
        row = self.prepare_action_data_intent(tracker)
        index = 2
        sheet.insert_row(row, index)

        return

    def submit_action_data_entity(self, tracker: Tracker):
        """ Prepares entity entry and saves in sheet """

        extracted_entity = next(
            (item for item in tracker.latest_message.get("entities") if item["extractor"] == "DIETClassifier"), None)
        """use only items extracted by DIETClassifier, we ignore CRFEntityExtractor for now. 
        Also, we are getting only first product mentioned/ extracted. Iterator is needed to extract all"""

        """Check if anything new was provided in tracker if not then exit without saving """

        if extracted_entity is None:
            'Slots were already populated earlier, nothing to save'
            return

        else:
            sheet = self.connect_to_sheet()
            row = self.prepare_action_data_entity(tracker, extracted_entity)
            index = 2
            sheet.insert_row(row, index)

        return
