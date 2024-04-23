#!/usr/bin/python3
'''Module for Base class.'''
from json import dumps, loads
import csv
import turtle
import time

class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with optional id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                list_objs = []
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries represented by json_string."""
        if json_string is None or len(json_string) == 0:
           return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")
        
        dummy_instance.update(**dictionary)
        return dummy_instance

     @classmethod
     def load_from_file(cls):
       '''Loads instances from file.'''
       filename = cls.__name__ + '.json'
       try:
         with open(filename, 'r') as f:
            json_string = f.read()
       except FileNotFoundError:
         return []

       if not json_string:
         return []

      list_dictionaries = cls.from_json_string(json_string)
      instances = [cls.create(**dictionary) for dictionary in list_dictionaries]
      return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
      '''Serializes instances to CSV file.'''
      filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as file:
         writer = csv.writer(file)
          if cls.__name__ == 'Rectangle':
             for obj in list_objs:
                 writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
          elif cls.__name__ == 'Square':
             for obj in list_objs:
                 writer.writerow([obj.id, obj.size, obj.x, obj.y])

     @classmethod
     def load_from_file_csv(cls):
       '''Deserializes instances from CSV file.'''
       filename = cls.__name__ + '.csv'
       try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            instances = []
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    instance = cls.create(
                        width=int(row[1]), height=int(row[2]),
                        x=int(row[3]), y=int(row[4]), id=int(row[0])
                    )
                elif cls.__name__ == 'Square':
                    instance = cls.create(
                        size=int(row[1]), x=int(row[2]),
                        y=int(row[3]), id=int(row[0])
                    )
                instances.append(instance)
            return instances
       except FileNotFoundError:
          return []

       @staticmethod
       def draw(list_rectangles, list_squares):
          """Draws rectangles and squares using Turtle graphics module."""
          screen = turtle.Screen()
          screen.title("Rectangles and Squares")
          screen.setup(width=800, height=600)

        pen = turtle.Turtle()

         for rect in list_rectangles:
             pen.penup()
             pen.goto(rect.x, rect.y)
             pen.pendown()
             pen.color("blue")
             pen.begin_fill()
             for _ in range(2):
                 pen.forward(rect.width)
                 pen.left(90)
                 pen.forward(rect.height)
                 pen.left(90)
             pen.end_fill()

         for square in list_squares:
             pen.penup()
             pen.goto(square.x, square.y)
             pen.pendown()
             pen.color("red")
             pen.begin_fill()
             for _ in range(4):
                 pen.forward(square.size)
                 pen.left(90)
             pen.end_fill()
 
         turtle.done()

 if __name__ == "__main__":
     list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
     list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

     Base.draw(list_rectangles, list_squares)
