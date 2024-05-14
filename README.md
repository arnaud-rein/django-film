# django-film
Lien notion pour voir les détails de la conception du projet :
\ 
https://frosted-poison-c40.notion.site/django-film-572cebbf30424b9da226ab43c33ef9e0?pvs=4

\

## Package à Download

Essentiel pour lancer l'application
`pip install requests`

Pour les test et pour vérifier le code : 
- pylint
- pylint-django
- factory-boy
- Faker
  
\

## lancer le projet 

Clonez le projet :
`git clone <le projet>`

Placez-vous dans `django-film\film` dans votre aroborescence. 

N'oubliez pas de download le package `requests`

Vous pouvez maintenant lancer le projet en tapant : 
`python manage.py runserver`

## Lancer les tests 

`python manage.py test`

\

## Lancer un pylint 

`pylint --load-plugins pylint_django monapp/` 
