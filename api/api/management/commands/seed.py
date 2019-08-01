from django.core.management.base import BaseCommand
from api.factories import ExampleFactory


class Command(BaseCommand):
    help = "Seeds the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--example",
            default=200,
            type=int,
            help="The number of fake examples to create.",
        )

    def handle(self, *args, **options):
        print("Populating database...")
        for _ in range(options["example"]):
            ExampleFactory()
        print("Done.")
