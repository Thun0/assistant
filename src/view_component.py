class ViewComponent:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_dimensions(self, w, h):
        self.w = w
        self.h = h

    def set_width(self, w):
        self.w = w

    def set_height(self, h):
        self.h = h

    def check_click(self, mx, my):
        if self.x <= mx <= self.x+self.w and self.y <= my <= self.y+self.h:
            return True
        return False
