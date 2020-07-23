from django.core.management.base import BaseCommand, CommandError
import evolution.modules.pokemon as poke


class Command(BaseCommand):
    help = 'Fill a newly created db with all the available chains'

    def handle(self, *args, **options):
        res = poke.temp()
        self.stdout.write("done")
