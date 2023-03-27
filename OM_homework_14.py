class Country:
    """
    Represents a country with a name, population, and capital city.
    """

    def __init__(self, name: str, population: int, capital: str = None):
        """
        Initializes a new instance of the Country class.

        :param name: A string representing the name of the country.
        :param population: An integer representing the population of the country.
        :param capital: A string representing the capital city of the country.
        """
        self.name = name
        self.population = population
        self.capital = capital

    def increase_population(self, increase: int):
        """
        Task 2.
        Increases the population of the country by the specified amount.

        :param increase: An integer representing the amount by which to increase the population.
        """
        self.population += increase

    def add(self, other_country):
        """
        Task 3
        Creates a new country by combining the current country with another country within add method.

        :return: A new Country object.
        """
        new_name = f'{self.name} {other_country.name}'
        new_population = self.population + other_country.population
        return Country(new_name, new_population)

    def __add__(self, other_country):
        """
        Task 4
        Creates a new country by adding the current country with another country within magic previous method.

        :return: A new Country object.
        """
        other_new_name = f'{self.name} {other_country.name}'
        other_new_population = self.population + other_country.population
        return Country(other_new_name, other_new_population)


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
japan.increase_population(5_230_000)
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)  # 15_000_000
print(bosnia_herzegovina.name)  # Bosnia Herzegovina

bosnia_herzegovina2 = bosnia + herzegovina
print(bosnia_herzegovina2.population)  # 15_000_000
print(bosnia_herzegovina2.name)  # Bosnia Herzegovina
