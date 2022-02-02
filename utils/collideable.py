from turtle import Turtle

class Collideable:
    #Parameter needs to inherit from Turtle and Collideable
    def CheckCollision(self: Turtle, object: Turtle, tolerance: int = 22) -> bool:
        return self.distance(object) < tolerance