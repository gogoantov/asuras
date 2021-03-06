from pygame import image

from libs.vec2d import Vec2d
from vehicle import Vehicle

class NormalVehicle(Vehicle):
    DEFAULTS = {
        'weight': 1200,
        'inventory': 16,
        'dimenstions': (40, 70),
        'slots': {
            'motions': 4,
            'engines': 4,
            'shields': 4,
            'addons': 8,
            'generators': 1,
            'weapons': 1
        },
    }
    top_speed = 50
    speed = 0
    weight = 0.4
    acceleration = 1
    rotation = 0

    def __init__(self, position, items_layer, *groups):
        super().__init__(position, items_layer, *groups)
        self.image = image.load('resources/tank.png')
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.items_layer = items_layer
        self.points = [Vec2d(-7, -32),
                       Vec2d(-20, -23),
                       Vec2d(-20, -13),
                       Vec2d(-15, -8),
                       Vec2d(-15, 8),
                       Vec2d(-20, 13),
                       Vec2d(-20, 23),
                       Vec2d(-7, 32),
                       Vec2d(7, 32),
                       Vec2d(20, 23),
                       Vec2d(20, 13),
                       Vec2d(15, 8),
                       Vec2d(15, -8),
                       Vec2d(20, -13),
                       Vec2d(20, -23),
                       Vec2d(7, -32)]
        self.pivot_points = [Vec2d(0, -5)]
