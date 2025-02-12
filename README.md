# Python Helpers

This repository is a collection of Python scripts that are used for faster programming. It includes various utility scripts that can help streamline your coding process, but it is intended for personal use.

## Scripts

## Usage
To use any of the scripts, simply import them into your Python project:

```python
from InputChecker import *
from RandomValues import *
```

### InputChecker.py
This script contains functions to validate and sanitize user inputs. It helps ensure that the inputs meet the required criteria before processing.
A more detailed function test is inside the InputChecker.py file.

#### Example Usage:
```python
from InputChecker import InputChecker

# Check if the input contains letters
print(InputChecker.checkFor("Hello", Letters=True))  # True

# Check if the input length is within the specified range
print(InputChecker.checkForLength("Hello", MinLength=1, MaxLength=5))  # True

# Check if the input is a valid email address
print(InputChecker.checkIsEmail("Bob@web.de"))  # True

# Check if the input is a valid phone number
print(InputChecker.checkIsPhoneNumber("123456"))  # True

# Check if the input is a valid password
print(InputChecker.checkPassword("Hello1234!", MinLength=8, MaxLength=16, Letters=True, Numbers=True, Symbols=True, Spaces=False))  # True

# Clean the input by stripping leading and trailing whitespace
print(InputChecker.inputCleaner(" Hello "))  # "Hello"

# Get the count of specified character types in the input
print(InputChecker.getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False))  # [5, 3, 1]

# Check for specified character types and get additional information
print(InputChecker.checkForWithExtraInfos("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False))  # [True, 5, 3, 1]
```


### RandomValues.py
This script provides functions to generate random values, such as random numbers, strings, and other data types. It is useful for testing and generating sample data.
A more detailed function test is inside the RandomValues.py file. (Generated Data is in German)

#### Example Usage:
```python
from RandomValues import RandomValues

# Generate random personal information
print("Person Name: " + RandomValues.Person.getName())
print("Person LastName: " + RandomValues.Person.getLastName())
print("Person Birthday: " + RandomValues.Person.getBirthDay().strftime("%d.%m.%Y"))
print("Person Address with Number: " + RandomValues.Person.getAddress())
print("Bank Balance: " + str(RandomValues.Person.getBankBalance()))

# Generate random arrays
print("Array Int: " + str(RandomValues.Array.getArrayRandInt()))
print("Array Str: " + str(RandomValues.Array.getArrayRandStr()))
print("Array Float: " + str(RandomValues.Array.getArrayRandFloat()))
print("Array Mix: " + str(RandomValues.Array.getArrayRandMixed()))

# Generate random product information
print("Product Name: " + RandomValues.Product.getName())
print("Product Description: " + RandomValues.Product.getDescription())
print("Product Price: " + str(RandomValues.Product.getPrice()) + " €")
print("Product Size: " + RandomValues.Product.getSize())
print("Product Stock: " + str(RandomValues.Product.getStock()))
```

## Contributing
Feel free to contribute to this repository by submitting pull requests. Any improvements or additional utility scripts are welcome.

## License
This project is licensed under the MIT License.
