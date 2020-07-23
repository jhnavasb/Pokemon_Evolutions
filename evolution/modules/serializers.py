from rest_framework import serializers
from evolution.models import pokemon, chain


class pokemonSerializer(serializers.Serializer):
    class Meta:
        model = pokemon
        fields = '__all__'

    def to_representation(self, instance):

        try:
            temp = instance.id
        except:
            return {'not': 'found'}

        representation = {
            'id': instance.id,
            'name': instance.name,
            'features': {
                'height': instance.height,
                'weight': instance.weight
            },
            'base_stats': {
                'hp': instance.hp,
                'attack': instance.attack,
                'defense': instance.defense,
                'special_attack': instance.special_attack,
                'special_defense': instance.special_defense,
                'speed': instance.speed
            },
            'evolution': instance.evolutions
        }

        return representation
