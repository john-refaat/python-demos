class Calories:
    """"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - (self.temperature * 10)
        return result

if __name__ == '__main__':
    calories = Calories(75, 178, 37, 20)
    print(calories.calculate())
