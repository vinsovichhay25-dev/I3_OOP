class HundredsCounter:
    def __init__(self, number):
        self.number = number

    def get_complete_hundreds(self):
        return self.number // 100
