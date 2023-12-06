def city_names(name, country, population=''):                       #########------Original Function!
    if population:
        
        city = f"{name}, {country}, population: {population}"
    
    else:
        city = f"{name}, {country}"
    return city.title()

