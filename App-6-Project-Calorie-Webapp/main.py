from temperature import Temperature
from calories import Calories

if __name__ == '__main__':
    temperature = Temperature("egypt", "sharm-el-sheikh").get()
    if temperature:
        print(f'temperature: {temperature} degrees Celsius')
        calories = Calories(75, 178, 37, temperature)
        print(f'calories: {calories.calculate()}')