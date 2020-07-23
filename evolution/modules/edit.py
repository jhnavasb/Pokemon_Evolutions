class _pokemon ():
    id = 0
    name = ""
    height = 0
    weight = 0
    hp = 0
    attack = 0
    defense = 0
    special_attack = 0
    special_defense = 0
    speed = 0
    rank = 0
    evolutions = []

    def main(self, q1):
        self.id = q1.id
        self.name = q1.name
        self.height = q1.height
        self.weight = q1.weight
        self.hp = q1.hp
        self.attack = q1.attack
        self.defense = q1.defense
        self.special_attack = q1.special_attack
        self.special_defense = q1.special_defense
        self.speed = q1.speed
        self.rank = q1.rank

    def set_evo(self, q2):
        r = self.rank
        evo = []

        for x in q2:
            if x.rank > r:
                evo.append({
                    'evolution_type': 'Evolution',
                    'id': x.id,
                    'name': x.name
                })
            elif x.rank < r:
                evo.append({
                    'evolution_type': 'Preevolution',
                    'id': x.id,
                    'name': x.name
                })

        self.evolutions = evo

    def __init__(self, q1, q2):
        self.main(q1[0])
        self.set_evo(q2)
