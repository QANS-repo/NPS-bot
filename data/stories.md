## Ankieta - czysta ścieźka 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}

## Ankieta - przerwana  
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
* out_of_scope
    - utter_powrot
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye

## Ankieta - kontynuacja 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
* out_of_scope
    - utter_powrot
* affirm
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}

## Ankieta - brak oceny NPS 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
* affirm
    - utter_powrot
* affirm
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}

## brak towarów 
* dostępność_brak
    - missing_product_form
    - form{"name": "missing_product_form"}
    - form{"name": null}
* affirm
    - utter_katalog

* dostępność_brak{"product_type":"pax"}
    - missing_product_form
    - form{"name":"missing_product_form"}
    - slot{"had_problems_finding_product":true}
    - slot{"missing_product_type":["pax"]}
    
* dostępność_brak
    - missing_product_form
    - form{"name": "missing_product_form"}
    - form{"name": null}
* deny
    - utter_kontynuacja
    
## Ankieta - ogólna odpowiedź 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}
* ogólnie
    - utter_ogólnie_dlaczego

## badanie pasywny - nie znaleziono produktu - szklanki
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":7}
    - nps_form
    - slot{"nps_score":7}
    - slot{"nps_group":"passive"}
    - form{"name":null}
* dostępność_brak{"product_type":"szklanki"}
    - missing_product_form
    - form{"name":"missing_product_form"}
    - slot{"had_problems_finding_product":true}
    - form{"name":null}


## badanie pasywny, tłok 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":8}
    - nps_form
    - slot{"nps_score":8}
    - slot{"nps_group":"passive"}
    - form{"name":null}
    - slot{"requested_slot":null}
* tłok
    - action_set_is_crowded
    - utter_tłok
    - utter_planowanie_wizyty
* affirm
    - utter_rady

### tłok - nie chce rad 
* tłok
    - action_set_is_crowded
    - utter_tłok
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja 

## Ankieta - jedzenie 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":8}
    - nps_form
    - slot{"nps_score":8}
    - slot{"nps_group":"passive"}
    - form{"name":null}
    - slot{"requested_slot":null}
* jedzenie
    - food_form
    - form{"name":"food_form"}
    - form{"name": null}
    

## badanie promotor brak konkretów w odpowiedzi, 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":10}
    - nps_form
    - slot{"nps_score":10}
    - slot{"nps_group":"promotor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ogólnie
    - utter_ogólnie_dlaczego


### wpomniano parking  
* parking
    - action_set_parking
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_form_parking_submitted
    - utter_kontynuacja
  
      
## pytania na czym polega ankieta
* na_czym_to_polega
    - utter_opis_ankiety
    - utter_opis_ankiety2
    - utter_opis_ankiety3
    - utter_powrot
* affirm
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}

## Żądanie przerwania
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":3}
    - nps_form
    - slot{"nps_score":3}
    - slot{"nps_group":"detractor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* out_of_scope
    - utter_goodbye


## Bot challenge - deny
* bot_challenge
    - utter_bot_challenge
    - utter_powrot
* deny 
    - utter_kontynuacja
    
## Pytanie o godziny otwarcia 
* pytanie_o_godziny
    - utter_godziny_otwarcia
    - utter_powrot

## Jak trafić
* pytanie_o_lokalizacje
    - utter_lokalizacja
    - utter_powrot

## pogorszenie
* pogorszenie
    - utter_co_sie_pogorszyło

## covid
* covid
    - utter_covid

## Ankieta - ogólna odpowiedź wersja 2
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":9}
    - nps_form
    - slot{"nps_score":9}
    - form{"name":null}
    - slot{"requested_slot":null}
* ogólnie
    - utter_ogólnie_dlaczego

## Ankieta - product form dobra jakość
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":9}
    - nps_form
    - slot{"nps_score":9}
    - form{"name":null}
    - slot{"requested_slot":null}
* jakość_mebli
    - action_set_product_quality
    - product_form
    - form{"name": "product_form"}
    - form{"name":null}
    - utter_katalog
    
## Ankieta - product form marna jakość 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":3}
    - nps_form
    - slot{"nps_score":3}
    - form{"name":null}
    - slot{"requested_slot":null}
* jakość_mebli
    - action_set_product_quality
    - product_form
    - form{"name": "product_form"}
    - form{"name":null} 
    - utter_kontynuacja

       
## Ankieta - product form ceny 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":3}
    - nps_form
    - slot{"nps_score":3}
    - form{"name":null}
    - slot{"requested_slot":null}
* cena
    - action_set_product_price
    - product_form
    - form{"name": "product_form"}
    - form{"name":null}
    - utter_katalog
    - utter_kontynuacja
     
## Ankieta - product form design produktów 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":9}
    - nps_form
    - slot{"nps_score":9}
    - form{"name":null}
    - slot{"requested_slot":null}
* design_produktów
    - action_set_product_design
    - product_form
    - form{"name": "product_form"}
    - form{"name":null}
    - utter_katalog

    
## Asortyment 
* asortyment
    - action_set_assortment
    - utter_katalog

    
## zwrot 
* zwrot
    - action_set_product_return
    - utter_zwrot
    
    
## kolejki
* kolejki
    - action_set_checkout_lines
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_kontynuacja
    
    
## reklamacje 
* reklamacje
    - action_set_complaint_status 
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_kontynuacja

    
## obsługa klienta 
* obsługa
    - action_set_customer_service_status 
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_obsługa
    
## promocje ma kartę Ikea Family
* rabaty_promocje
    - action_set_promo_status
    - utter_promocje 
* inform{"ikea_family":"true"}
    - slot{"ikea_family":"true"}
    - utter_kontynuacja

## promocje nie ma karty Ikea Family
* rabaty_promocje
    - action_set_promo_status
    - utter_promocje 
* inform{"ikea_family":"false"}
    - slot{"ikea_family":"false"}
    - utter_kontynuacja

## promocje, nie jest zainteresowany kartą 
* rabaty_promocje
    - action_set_promo_status
    - utter_promocje
* inform{"ikea_family":"not_interested"}
    - slot{"ikea_family":"not_interested"}
    - utter_kontynuacja

## promocje, uźywam inform bez ustawiania slot'u
* rabaty_promocje
    - action_set_promo_status
    - utter_promocje
* inform
    - utter_kontynuacja
    
    
## Można spędzić cały dzień
* miejsce_na_cały_dzień
    - action_set_spent_full_day
    - store_location_form
    - utter_planowanie_wizyty
* affirm
    - utter_rady
    
## Można spędzić cały dzień
* miejsce_na_cały_dzień
    - action_set_spent_full_day
    - store_location_form
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja
    
## za dużo chodzenia 
* za_dużo_chodzenia
    - action_set_too_much_walking
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_planowanie_wizyty
* affirm
    - utter_rady
 
## za dużo chodzenia - nie chce rad
* za_dużo_chodzenia
    - action_set_too_much_walking
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja
    
    
## duży sklep
* powierzchnia_sklepu
    - action_set_store_size
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_planowanie_wizyty
* affirm
    - utter_rady
    
## duży sklep  2
* powierzchnia_sklepu
    - action_set_store_size
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja

## dostawa 
* dostawa
    - action_set_delivery
    - store_location_form
    - form{"name": "store_location_form"}
    - form{"name": null}
    - utter_rozm_dostawa
    
## montaż
* montaż
    - action_set_assembly
    - store_location_form
    - form{"name": "store_location_form"}
    - slot{"store_location": "wrocław"}
    - form{"name": null}
    - utter_rozm_montaz
    
    
## za dużo chodzenia kilka rund dialogu 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":5}
    - slot{"nps_score":"5"}
    - nps_form
    - slot{"nps_score":5}
    - slot{"nps_group":"detractor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* za_dużo_chodzenia
    - action_set_too_much_walking
    - slot{"walking_text":"za dużo chodzenia"}
    - store_location_form
    - form{"name":"store_location_form"}
    - slot{"requested_slot":"store_location"}
* inform{"store_location":"Warszawa"}
    - slot{"store_location":"Warszawa"}
    - store_location_form
    - slot{"store_location":"Warszawa"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja
    
    
## udane zakupy - eksperymentalnie pytamy o planowanie wizyty
* udane_zakupy
    - utter_planowanie_wizyty
* affirm
    - utter_rady
    
## udane zakupy eksperymentalnie pytamy o planowanie wizyty - odmowa 
* udane_zakupy
    - utter_planowanie_wizyty
* deny
    - utter_kontynuacja 
    
## wygoda - 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":10}
    - slot{"nps_score":"10"}
    - nps_form
    - slot{"nps_score":10}
    - slot{"nps_group":"promotor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* wygoda
    - store_location_form
    - utter_kontynuacja
    
## badany odpowiada tylko nazwą produktu 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}
* inform{"product_type":"billy"}
    - utter_kontynuacja
    
## badany odpowiada tylko nazwą potrawy 
* przywitaj
    - nps_form
    - form{"name": "nps_form"}
    - form{"name": null}
* inform{"food":"zapiekanka"}
    - slot{"food":["zapiekanka"]}
    - utter_kontynuacja
    
## Niezadowolony z obsługi i małego parkingu, mówi do widzenia aby zakończyć 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":5}
    - slot{"nps_score":"5"}
    - nps_form
    - slot{"nps_group":"detractor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* obsługa
    - action_set_customer_service_status
    - store_location_form
    - form{"name":"store_location_form"}
    - slot{"requested_slot":"store_location"}
* inform{"store_location":"Warszawie"}
    - slot{"store_location":"Warszawie"}
    - store_location_form
    - slot{"store_location":["Warszawie","Warszawie"]}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_obsługa
* parking{"transport":"parking"}
    - slot{"transport":["parking","parking"]}
    - action_set_parking
    - slot{"transport_text":"mały parking"}
    - store_location_form
    - form{"name":"store_location_form"}
    - slot{"store_location":"Warszawie"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_form_parking_submitted
    - utter_kontynuacja
* out_of_scope
    - utter_goodbye
    
    
## Ogólnie o produktach, nie o konkretnym 

* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":8}
    - slot{"nps_score":"8"}
    - nps_form
    - slot{"nps_score":8}
    - slot{"nps_group":"passive"}
    - form{"name":null}
    - slot{"requested_slot":null}
* design_produktów
    - action_set_product_design
    - product_form
    - form{"name":"product_form"}
* deny
    - utter_kontynuacja
    
## Dopytanie o szczegóły potrawy 

* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":8}
    - slot{"nps_score":"8"}
    - nps_form
    - slot{"nps_score":8}
    - slot{"nps_group":"passive"}
    - form{"name":null}
    - slot{"requested_slot":null}
* jedzenie{"food":"hot-dogi"}
    - slot{"food":["hot-dogi"]}
    - utter_ogólnie_dlaczego
* inform{"food":"Cebulka z ogórkami"}
    - food_form
    - form{"name":"food_form"}
    - slot{"food":["Cebulka z ogórkami"]}
    - form{"name":null}
    - slot{"requested_slot":null}

## niejasna odpowiedź na ptanie dlaczego 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":7}
    - slot{"nps_score":"7"}
    - nps_form
    - slot{"nps_score":7}
    - slot{"nps_group":"passive"}
    - form{"name":null}
    - slot{"requested_slot":null}
* deny
    - utter_goodbye

## Nie podaje lokalizacji sklepu 
* przywitaj
    - nps_form
    - form{"name":"nps_form"}
    - slot{"requested_slot":"nps_score"}
* inform{"number":1}
    - slot{"nps_score":"1"}
    - nps_form
    - slot{"nps_group":"detractor"}
    - form{"name":null}
    - slot{"requested_slot":null}
* obsługa
    - action_set_customer_service_status
    - store_location_form
    - form{"name":"store_location_form"}
    - slot{"requested_slot":"store_location"}
* deny
    - utter_kontynuacja
* inform 
    - utter_kontynuacja
