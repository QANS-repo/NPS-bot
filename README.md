# NPS bot
### Chatbot do pomiaru i poprawy NPS 

- Chatbot prowadzi badanie NPS za pośrednictwem dialogu na stronie internetowej, Facebooku, WhatsApp i w innych kanałach.
- Analizuje tekst uzasadnienia odpowiedzi i generuje analizę głównych czynników poprawiających i osłabiających NPS.
- W trakcie interakcji proponuje interwencję (poprawia NPS) poprzez usunięcie problemu zgłoszonego przez klienta.

Przykład działania [chatbota](https://www.qans.pl/services/test-bot/). Przykładowe badanie i demonstracja jak wyniiki są generowane na żywo.   
Wskazówki jak użyć [chatbota](https://www.qans.pl/services/) do identyfikacji czynników wpływających na NPS i do jego poprawy.

### Instrukcja instalacji 
Chatbot działa w oparciu o system [Rasa](https://github.com/RasaHQ/rasa). 
Uwaga! Potrzebna jest Rasa wersja 1.0 a nie 2.0.  
Dodatkowo pomocna (ale nie niezbędna) jest [Rasa X](https://rasa.com/docs/rasa-x/), system do projektowania dialogów (ang. Conversation-Driven Development (CDD)).  

Ten sytem był testowany lokalnie i na serwerze przy użuciu wersji Rasa 1.10.16 i Rasa X 0.32.2  

### Instalacja na lokalnym komputerze 

Instalacja Rasa Open Source 
[instrukcja](https://rasa.com/docs/rasa/installation/)  
Uwaga! Trzeba podać wcześniejszą wersję, a więc:
pip3 install rasa==1.10.16 

Instrukcja instalacji Rasa X
Trzeba podać wcześniejszą wersję jak w przykładzie poniżej:
python3 -m pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple/rasa-x/rasa-x-0.32.4.tar.gz 

### Instalacja na serwerze 
[Instrukcja instalacji](https://rasa.com/docs/rasa-x/0.32.x/installation-and-setup/install/docker-compose#manual-installation) przy użyciu Docker Compose 

W przypadku problemów tu można szukać poprawnej wersji rasa X: https://pypi.rasa.com/simple/rasa-x/

### Modyfikacje - rozszerzenia  
Czatbot NPS to model wytrenowany na systemie Rasa. 
Został on rozszerzony o nastepujące elementy:  
-  Custom Actions specyficzne dla badania NPS
-  Zapisywanie aspektów w Google Sheets (zamiast lokalnej bazie danych). To dla demonstracji 

Pierwszy element wymaga zaimplementowania actions.py - serwera akcji. 
Drugi wymaga dodatkowej biblioteki i skonfigurowania Google Sheet. 
Instrukcja instalacji [gspread](https://gspread.readthedocs.io/en/latest/)
Połącznie [Rasy do Google Sheet](https://forum.rasa.com/t/storing-user-data-to-google-sheets/33287/3)
W folderze actions musisz umieścić plik credentials.json wygenerowany w sposób opisany w wideo z linka powyżej. 

Jeśli używsz instalacji na serwerze w folderze actions znajduje się plik Dockerfile, który doda bibliotekę gspread do kontenera z serwerem akcji.   

### Problemy z instalacją, używaniem czatbota 
Zaletą wykorzytania systemu Rasa jest to że jest masa materiałów i wsparcia online. 
Wyszukanie konkretnego błędu lub opisanie problemów doprowadzi Cię na forum lub do innego źródła gdzie znajdziesz rozwiązanie. 

W kontekście NPS i tego systemu pracujemy nad dokładna instrukcją.

### Czy planujemy przejście z wersji Rasa 1 na nowszą?
Rasa rozwija się bardzo szybko. Jesienią 2020 gdy powstawł NPS bot to były najnowsze wersje Rasy.  
Planujemy uaktualnienie do nowszej wersji ale prawdopodobnie poczekamy do wersji 3. 


### Jak zmodyfikować kod na potrzeby własnego badania
W dużej mierze to jak trenowanie nowego bota. Potrzeba dialogów, aspektów i przykładowych odpowiedzi od uzytkowników.
Rasa ma świetne materiały edukacyjne, oraz bezpłatne [szkolenie na Udemy](https://www.udemy.com/course/rasa-for-beginners/)
 

Czatbot może być używany w następujących kanałach:
- Facebook Messenger
- Slack
- Google Hangouts
- Webex Teams
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- Własny kanał


## Licencja
MIT. Licencja na ten model i kod do badania NPS. Rasa ma odrębną licencję opisaną w ich dokumentacji. 
