# django-film

## Galerie d'images

<div style="display: flex; flex-wrap: wrap;">
  <div style="flex: 1 0 21%; margin: 5px;">
    <img src="https://github.com/arnaud-rein/django-film/blob/main/images/homepage.png" alt="Description de l'image 1" style="width: 100%;">
  </div>
  <div style="flex: 1 0 21%; margin: 5px;">
    <img src="https://github.com/arnaud-rein/django-film/blob/main/images/listes_films.png.png" alt="Description de l'image 2" style="width: 100%;">
  </div>
  <div style="flex: 1 0 21%; margin: 5px;">
    <img src="https://github.com/arnaud-rein/django-film/blob/main/images/search.png.png" alt="Description de l'image 3" style="width: 100%;">
  </div>
  
</div>



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
