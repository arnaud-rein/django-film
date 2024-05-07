import factory

from monapp.models import Film

class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Film

    title = factory.Faker('sentence', nb_words=4)
    year = factory.Faker('year')
    style = factory.Faker('word')
    director = factory.Faker('name')
    description = factory.Faker('paragraph')