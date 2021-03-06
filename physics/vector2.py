import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
         return 'Vector2({}, {})'.format(self.x, self.y)

    def __add__(self, other_vector):
        return Vector2(
            self.x + other_vector.x,
            self.y + other_vector.y
        )

    def __sub__(self, other_vector):
        return Vector2(
            self.x - other_vector.x,
            self.y - other_vector.y
        )

    def __mul__(self, number):
        return Vector2(
            self.x * number,
            self.y * number
        )

    def __truediv__(self, number):
        return Vector2(
            self.x / number,
            self.y / number
        )

    # We cannot use the __len__ method because that method always has to return an integer, 
    # whilst the length of a vector can be a float too
    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # The unit vector of a vector is a vector with the same direction, but with a length of 1
    def get_unitvector(self):
        length = self.get_length()
        if length == 0:
            return self
        return self / length

    # Calculate the distance from this vector to another vector
    def calc_distance_to(self, other_vector):
        vector_between = other_vector - self
        return vector_between.get_length()

    def rotate_90(self):
        return Vector2(-self.y, self.x)

    def rotate_rad(self, angle):
        cos = math.cos(angle)
        sin = math.sin(angle)
        x_component = self.x * cos - self.y * sin
        y_component = self.x * sin + self.y * cos
        return Vector2(x_component, y_component)

    def rotate_deg(self, angle):
        angle_in_rad = (angle / 180) * math.pi
        return self.rotate_rad(angle_in_rad)

    def get_minimal_string(self):
        return '{},{}'.format(self.x, self.y)
