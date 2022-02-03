from turtle import Turtle

class Collideable:
    #Parameter needs to inherit from Turtle and Collideable
    def CheckCollision(self: Turtle, entity: Turtle, tolerance: int = 27) -> bool:
        return self.distance(entity) < tolerance