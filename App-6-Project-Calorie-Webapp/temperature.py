import requests
from selectorlib import Extractor

class Temperature:
    """
        Represent a temperature value extracted from timeanddate.com/weather webpage
    """

    url = "https://www.timeanddate.com/weather/{}/{}"

    def __init__(self, country, city):
        self.country = country
        self.city = city

    @staticmethod
    def _extract_temp_number(temp_string):
        """Extract the numeric temperature value from temperature string."""
        return float(temp_string.split('°')[0].strip())

    def get(self):
        """Scrape the temperature value from the website."""
        response = requests.get(self.url.format(self.country.replace(' ', '-'),
                                                self.city.replace(' ', '-')))
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        extractor = Extractor.from_yaml_file('temperature.yaml')
        data = extractor.extract(response.text)
        temp_string = data['temp']
        return self._extract_temp_number(temp_string)


if __name__ == '__main__':
    temperature = Temperature("italy", "milan")
    print(f'temperature: {temperature.get()} degrees Celsius')