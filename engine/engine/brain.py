import math

class Brain:

    def energia(self, refs):
        return math.log(1 + len(refs) + 1e-9)

    def peso_estructura(self, profundidad):
        return 1 / (1 + profundidad)

    def score(self, refs, profundidad):
        return self.energia(refs) * self.peso_estructura(profundidad)
