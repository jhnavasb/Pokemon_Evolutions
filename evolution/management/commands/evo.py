from django.core.management.base import BaseCommand, CommandError
import evolution.modules.pokemon as poke


class Command(BaseCommand):
    help = 'Fetch and store information from the selected evolution chain'

    def add_arguments(self, parser):
        parser.add_argument(
            'id', type=int, help='Indicates the ID of the evolution chain')

    def handle(self, *args, **options):
        id = options['id']
        res = poke.evo_chain(id)
        self.stdout.write("Evolution chain: %s" % res)
