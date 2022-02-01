from turtle import Turtle


#interface
class ICollideable:
    #Parameter needs to inherit from Turtle and ICollideable
    def CheckCollision(self: Turtle, object: Turtle, tolerance: int = 22) -> bool:
        return self.distance(object) < tolerance