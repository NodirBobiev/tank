
class Game:
    def __init__(self):
        self.objects = []

    def update(self, deltatime: float):
        for o in self.objects:
            o.update(deltatime)
        
        for o in self.objects:
            print(o)
    

    def render(self, surface):
        for o in self.objects:
            o.render(surface)




