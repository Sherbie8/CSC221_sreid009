from city_functions import city_names               ########-------Tests that the function works!

def test_city_country():
    
    formatted_name = city_names('New York', 'United States')
    
    assert formatted_name == 'New York, United States'
    
def test_name_country_population():
    
    formatted_name = city_names(
        'New York', 'United States', '8,000,000')
    
    assert formatted_name == 'New York, United States, 8,000,000'
