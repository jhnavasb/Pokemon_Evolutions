from rest_framework import viewsets, generics

from evolution.modules.serializers import pokemonSerializer
from evolution.modules.edit import _pokemon
from evolution.models import pokemon, chain


class PokemonViewSet(generics.ListAPIView):
    serializer_class = pokemonSerializer

    def get_queryset(self, **kwargs):
        name = self.kwargs.get('pk')
        context_data = dict()
        try:
            a = pokemon.objects.all().filter(name=name)[0].evo_chain_id
            a = pokemon.objects.all().filter(evo_chain_id=a)
        except:
            return [0]

        context_data['q1'] = pokemon.objects.all().filter(name=name)
        context_data['q2'] = a.exclude(name=name)

        data = _pokemon(context_data['q1'], context_data['q2'])

        return [data]
