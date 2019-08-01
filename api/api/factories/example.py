import factory
import factory.fuzzy


@factory.Faker.override_default_locale("fr_FR")
class ExampleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "api.Example"

    title = factory.Faker("job")
    company = factory.Faker("company")
    description = factory.Faker("text")
