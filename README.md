## Калькулятор

Простой калькулятор на PyQt6 и Python3  

### Git Flow
В проекте используется простой git flow  
Ветка main для готовых версий  
Ветка dev - основная ветка разработки  
При работе над фичей создается отдельная ветка ```feat/<название>```, которая после вливается в dev 
Названия коммитов в формате:
```feat: <краткое описание изменений>```  
```fix: <краткое описание изменений>```  
В нашем git flow используется уникальная система разрешения merge conflicts  
За создание мерж конфликтов выдается ~~пендель~~ право разрешить его самостоятельно

### Установка
Требуется установленный python (рекомендуемая версия ^3.11)
#### WINDOWS
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```
#### LINUX
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

