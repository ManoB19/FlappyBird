import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y



class Pipe(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

    def update(self, *args):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()
       
#class Coin(Obj):

#    def __init__(self, image, x, y, *groups):
#        super().__init__(image, x, y, *groups)
#
#    def update(self, *args):
#        pass    