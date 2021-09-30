class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        self.perimeter = (2 * self.width) + (2 * self.height)
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal

    def get_picture(self):
        self.picture = ""
        self.colums = "*" * self.width
        row_count = 1
        while row_count <= self.height:
            if self.height > 50 or self.width > 50:
                return "Too big for picture."
            self.picture += self.colums + "\n"
            row_count += 1
        return self.picture

    def get_amount_inside(self, insert_shape):
        self.amount_inside = self.get_area() / insert_shape.get_area()
        self.result_amount = int(str(self.amount_inside).split(".")[0])
        return self.result_amount

    def __str__(self):
        self.values = "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        self.name = self.__class__.__name__
        return self.name + self.values


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.height = side
        self.width = side

    def set_side(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        self.values = "(side=" + str(self.width) + ")"
        self.name = self.__class__.__name__
        return self.name + self.values

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.height = side
        self.width = side


rect = Rectangle(10, 15)
print(rect)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())

sq = Square(5)
print(sq)
# Square area
print(sq.get_area())
# Square diagonal
print(sq.get_diagonal())
# Square picture
print(sq.get_picture())
print("Squares fit inside Rectagle: ", rect.get_amount_inside(sq))
