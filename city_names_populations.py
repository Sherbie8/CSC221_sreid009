from city_functions import city_names               ########-----Modified version with population included

print("Enter 'q' to quit.")

while True:
    city = input ("\nPlease enter a city name: ")
    
    if city == 'q':
        break
    country = input("Please enter the country: ")
    if country == 'q':
        break
    population = int(input("Please enter the population: "))
    if population == 'q':
        break
    
    formatted_name = city_names(city, country, population)
    
    print(f"\tNeatly formatted name: {formatted_name}.")