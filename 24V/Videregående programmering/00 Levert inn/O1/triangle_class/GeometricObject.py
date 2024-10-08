class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color # Set color
        self.__filled = filled

    def get_color(self):
        return self.__color # Get color

    def set_color(self, color):
        self.__color = color

    def is_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)