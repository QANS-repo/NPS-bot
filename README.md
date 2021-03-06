<h1 align="center">馃挰 NPS bot 馃挰</h1>

### Chatbot do pomiaru i poprawy NPS 

- Chatbot prowadzi badanie NPS za po艣rednictwem dialogu na stronie internetowej, Facebooku, WhatsApp i w innych kana艂ach.
- Analizuje tekst uzasadnienia odpowiedzi i generuje analiz臋 g艂贸wnych czynnik贸w poprawiaj膮cych i os艂abiaj膮cych NPS.
- W trakcie interakcji proponuje interwencj臋 (poprawia NPS) poprzez usuni臋cie problemu zg艂oszonego przez klienta.

Przyk艂ad dzia艂ania [chatbota](https://www.qans.pl/services/test-bot/). Przyk艂adowe badanie i demonstracja jak wyniiki s膮 generowane na 偶ywo.   
Wskaz贸wki jak u偶y膰 [chatbota](https://www.qans.pl/services/) do identyfikacji czynnik贸w wp艂ywaj膮cych na NPS i do jego poprawy.  

<div align="center">
<img align="center" src="./demo/NPS-bot.gif" alt="Chatbot">
</div>

Dialog jest analizowany na bie偶膮co  

<div align="center">
<img align="center" src="./demo/arkusz.gif" alt="Chatbot">
</div>

Wizualizacja danych za pomoc膮 Google Sheet  

<div align="center">
<img align="center" src="./demo/wykres_NPS.png" alt="Chatbot">
</div>



### Instrukcja instalacji 
Chatbot dzia艂a w oparciu o system [Rasa](https://github.com/RasaHQ/rasa).  
Uwaga! Potrzebna jest Rasa wersja 1.0, nie 2.0.  
Dodatkowo pomocna, ale nie niezb臋dna, jest [Rasa X](https://rasa.com/docs/rasa-x/), system do projektowania dialog贸w (ang. Conversation-Driven Development (CDD)).  

Kroki:
1. Skopiuj to repozytorium 
    - `git clone https://github.com/QANS-repo/NPS-bot.git`
    -  zainstaluj gspread `pip3 install gspread`
2. Zainstaluj Rasa (i ewentualnie Rasa X)
    - instrukcja dla wersji lokalnej i serwera w sekcji poni偶ej
3. W folderze z repozytorium z terminala uruchom Rasa i wytrenuj model  
    - Trenowanie modelu `rasa train`
    - Uruchomienie serwera akcji `rasa run actions --debug`
    - Uruchomienie Rasa X `rasa x` lub Rasa w terminalu `rasa shell`

Ten sytem by艂 testowany lokalnie i na serwerze przy u偶yciu Rasa w wersji 1.10.16 i Rasa X 0.32.2  

### Instalacja na lokalnym komputerze 

Instalacja Rasa Open Source 
[instrukcja](https://rasa.com/docs/rasa/installation/).  
Uwaga! Trzeba poda膰 wcze艣niejsz膮 wersj臋, a wi臋c:  
`pip3 install rasa==1.10.16`  

Instrukcja instalacji Rasa X.  
Trzeba poda膰 wcze艣niejsz膮 wersj臋 jak w przyk艂adzie poni偶ej:
`python3 -m pip install -U rasa-x --extra-index-url https://pypi.rasa.com/simple/rasa-x/rasa-x-0.32.2.tar.gz`

### Instalacja na serwerze 
[Instrukcja instalacji](https://rasa.com/docs/rasa-x/0.32.x/installation-and-setup/install/docker-compose#manual-installation) przy u偶yciu Docker Compose 

W przypadku problem贸w [tu](https://pypi.rasa.com/simple/rasa-x/) mo偶na szuka膰 wersji Rasa X.

### Instalacja wymaganych dodatk贸w   
Czatbot NPS to model wytrenowany na systemie Rasa. 
Zosta艂 on rozszerzony o nastepuj膮ce elementy:  
-  Custom Actions specyficzne dla badania NPS
-  Zapisywanie aspekt贸w w Google Sheets (zamiast lokalnej bazie danych). To dla demonstracji 

Pierwszy element wymaga zaimplementowania *actions.py* - serwera akcji. 
Drugi wymaga dodatkowej biblioteki i skonfigurowania Google Sheet. 
Instrukcja instalacji [gspread](https://gspread.readthedocs.io/en/latest/)
Konfiguracja [Google Sheet](https://erikrood.com/Posts/py_gsheets.html)
W folderze actions musisz umie艣ci膰 plik *credentials.json* wygenerowany w spos贸b opisany powy偶ej. 

Je艣li u偶ywsz instalacji na serwerze w folderze actions znajduje si臋 plik Dockerfile, kt贸ry doda bibliotek臋 gspread do kontenera z serwerem akcji.   

### Problemy z instalacj膮, u偶ywaniem czatbota 
Zalet膮 wykorzytania systemu Rasa jest to, 偶e jest wiele materia艂贸w dost臋pnych online. 
Wyszukanie konkretnego b艂臋du lub opisanie problem贸w doprowadzi Ci臋 na forum lub do innego 藕r贸d艂a gdzie znajdziesz rozwi膮zanie. 

Dla NPS i tej implementacji pracujemy nad dok艂adn膮 instrukcj膮.

### Czy planujemy przej艣cie z wersji Rasa 1.0 na nowsz膮?
Rasa rozwija si臋 bardzo szybko. Jesieni膮 2020 gdy powstaw艂 czatbot NPS to by艂a najnowsza wersja Rasy.  
W wersji Rasa 2.0 zmieniono format trenowania danych. 
Uaktualnienimy program do nowszej wersji, ale poczekamy do wersji 3.

### Klient chatbota osadzony na stronie internetowej 
W demo u偶ywamy klienta chatbota osadzonego na stronie internetowej. 
Korzystamy z Botfront [Rasa-webchat](https://github.com/botfront/rasa-webchat)

### Jak zmodyfikowa膰 kod na potrzeby w艂asnego badania
W du偶ej mierze to jak trenowanie nowego bota. Potrzeba dialog贸w, aspekt贸w i przyk艂adowych odpowiedzi od u偶ytkownik贸w.  
Wi臋cej w dokumentacji Rasa oraz w [szkoleniu na Udemy](https://www.udemy.com/course/rasa-for-beginners/).

### NPS Bot mnie nie rozumie albo robi b艂臋dy 
Zobacz teksty na kt贸rych by艂 trenowany w pliku [nlu.md](data/nlu.md)
Je艣li nie ma tam przyk艂adu podobnego do tego co chcesz powiedzie膰 chatbot NPS raczej Ci臋 nie zrozumie. 
Mo偶esz dopisa膰 teksty do modelu j臋zyka i przetrenowa膰 model. 

### Jak zintegrowa膰 chatbota NPS z innymi kana艂ami - np. Facebook.
Trzeba wykona膰 kroki standardowej procedury integracji [Rasy z FB](https://rasa.com/docs/rasa/connectors/facebook-messenger/)
Przyk艂ad integracji chatbota NPS z [FB Messenger](https://m.me/qansbot)
Interakcja z poziomu [naszej strony na FB](https://fb.me/qansbot).  
Dane z tych interakcji s膮 analizowane na 偶ywo i dodawane do arkusza Google Sheet.

Czatbot mo偶e by膰 u偶ywany w nast臋puj膮cych kana艂ach:
- Facebook Messenger
- Slack
- Google Hangouts
- Webex Teams
- Microsoft Bot Framework
- Rocket.Chat
- Mattermost
- Telegram
- Twilio
- W艂asny kana艂


## Licencja
MIT. Licencja na ten model i kod do badania NPS. Rasa ma odr臋bn膮 licencj臋 opisan膮 w ich dokumentacji. 
