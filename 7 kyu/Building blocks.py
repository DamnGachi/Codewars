class Block:
    def __init__(self, x):
        self.x = x

    def get_width(self):
        return self.x[0]

    def get_length(self):
        return self.x[1]

    def get_height(self):
        return self.x[2]

    def get_volume(self):
        return self.x[0] * self.x[1] * self.x[2]

    def get_surface_area(self):
        return (self.x[0] * self.x[1] + self.x[0] * self.x[2] + self.x[1] * self.x[2]) * 2
