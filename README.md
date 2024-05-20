# helloidol2
---

1. startproject helloidol2
   1. python -m pip install django~=4.2 
   2. django-admin startproject helloidol2 .
   3. Files > Settings... > Language & Frameworks > Django
      [v] Enable Django Support
   4. Run > Edit Configurations... > + > Django Server > Name : runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp t1
   1. python manage.py startapp t1
   2. 't1', in INSTALLED_APPS in settings.py
3. t1/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
         2. __str__(): 객체를 출력할 때, 알맞은 string으로 출력하자
      2. python manage.py makemigrations t1
      3. python manage.py migrate t1
   2. admin
      1. Character
      2. python manage.py createsuperuser
   3. views
      1. R: CharacterListView
   4. templates/t1/
      1. character_list.html
   5. urls
      1. t1:character_list