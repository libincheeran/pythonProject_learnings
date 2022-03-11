class InnerOne:
    def __init__(self, name):
        self.name = name

    @property
    def get_val(self):
        return self.name + " from inner"
