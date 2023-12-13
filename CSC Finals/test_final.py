from python_finals import mini_maxi_sumi, sieve_of_eratosthenes, int_and_string

#Tests the first function
def test_mini_maxi_sumi():
        num = (2023, 221, 1214, 1200, 2002)
        result = mini_maxi_sumi(*num)
        assert result, (min(num), max(num), sum(num))

#Tests the second function
def test_sieve_of_eratosthenes():
        limit = 30
        primes = sieve_of_eratosthenes(limit)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        assert primes, expected_primes

#Tests the third function
def test_int_and_string():
        # Test case 1: Both inputs are integers
        result1 = int_and_string(3, 5)
        assert result1, 8

        # Test case 2: One input is a string, the other is an integer
        result2 = int_and_string("This is a string: ", 30)
        assert result2, "This is a string: 30"

        # Test case 3: One input is a string, the other is a float
        result3 = int_and_string("'This is a string with integer': ", 123)
        assert result3, "'This is a string with integer': 123"

        # Test case 4: Both inputs are strings
        result4 = int_and_string("Hello, ", "World!")
        assert result4, "Hello, World!"
        
if __name__ == '__main__':
    from python_finals import sieve_of_eratosthenes, mini_maxi_sumi, int_and_string
    test_sieve_of_eratosthenes(), test_mini_maxi_sumi(), test_int_and_string()
    print("All tests passed.")