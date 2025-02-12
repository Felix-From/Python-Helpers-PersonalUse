class InputChecker:
    """
    A class used to perform various input validation checks.
    
    Methods
    -------
    checkFor(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False) -> bool
        Checks if the input message contains the specified types of characters.
    checkForWithExtraInfos(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False)
        Checks if the input message contains the specified types of characters and returns additional information about the counts of each type.
    checkForLength(InputMsg, MinLength=0, MaxLength=16) -> bool
        Checks if the length of the input message is within the specified range.
    checkIsEmail(InputMsg) -> bool
        Checks if the input message is a valid email address.
    checkIsPhoneNumber(InputMsg, minLength=5) -> bool
        Checks if the input message is a valid phone number with a minimum length.
    checkPassword(InputMsg, MinLength=8, MaxLength=16, Letters=True, Numbers=True, Symbols=True, Spaces=False) -> bool
        Checks if the input message is a valid password based on the specified criteria.
    inputCleaner(InputMsg) -> str
        Cleans the input message by stripping leading and trailing whitespace.
    getCountOf(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False)
        Counts the occurrences of the specified types of characters in the input message and returns an array with the counts.
    """

    def checkFor(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False) -> bool:
        """
        Checks if the input message contains or does not contain specific types of characters based on the provided flags.
        Args:
            InputMsg (str): The input message to be checked.
            Letters (bool, optional): If True, the input must contain at least one letter. If False, the input must not contain any letters. Defaults to False.
            Numbers (bool, optional): If True, the input must contain at least one number. If False, the input must not contain any numbers. Defaults to False.
            Symbols (bool, optional): If True, the input must contain at least one symbol (non-alphanumeric and non-space character). If False, the input must not contain any symbols. Defaults to False.
            Spaces (bool, optional): If True, the input must contain at least one space. If False, the input must not contain any spaces. Defaults to False.
        Returns:
            bool: True if the input message meets the specified criteria, False otherwise.
        Raises:
            Exception: If an error occurs during the processing of the input message.
        """
        try:
            InputMsg = str(InputMsg)
            has_letter = any(c.isalpha() for c in InputMsg)
            has_number = any(c.isdigit() for c in InputMsg)
            has_symbol = any(not c.isalnum() and not c.isspace() for c in InputMsg)
            has_space = any(c.isspace() for c in InputMsg)

            if Letters and not has_letter:
                return False
            if Numbers and not has_number:
                return False
            if Symbols and not has_symbol:
                return False
            if Spaces and not has_space:
                return False

            if not Letters and has_letter:
                return False
            if not Numbers and has_number:
                return False
            if not Symbols and has_symbol:
                return False
            if not Spaces and has_space:
                return False

            return True
        except Exception as e:
            raise e;
    
    def checkForWithExtraInfos(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False):
        """
        Checks the input message for the presence of letters, numbers, symbols, and spaces based on the specified flags,
        and returns an array with the count of each type and a boolean indicating if all specified types are present.

        Args:
            InputMsg (str): The input message to be checked.
            Letters (bool, optional): If True, count the letters in the input message. Defaults to False.
            Numbers (bool, optional): If True, count the numbers in the input message. Defaults to False.
            Symbols (bool, optional): If True, count the symbols in the input message. Defaults to False.
            Spaces (bool, optional): If True, count the spaces in the input message. Defaults to False.

        Returns:
            list: An array with the first element being a boolean indicating if all specified types are present,
                  followed by the counts of each specified type in the order: [CheckResult, Letters, Numbers, Symbols, Spaces].
                  The array only includes counts for the types marked as True, but maintains the order.

        Raises:
            Exception: If an error occurs during the processing of the input message.
        """
        try:
            InputMsg = str(InputMsg)
            resultArray = InputChecker.getCountOf(InputMsg,Letters,Numbers,Symbols,Spaces)
            resultArray.insert(0,InputChecker.checkFor(InputMsg,Letters,Numbers,Symbols,Spaces))
            return resultArray
        except Exception as e:
            raise e;

    def checkForLength(InputMsg, MinLength=0, MaxLength=16) -> bool:
        """
        Checks if the length of the input message is within the specified range.

        Args:
            InputMsg (str): The input message to check.
            MinLength (int, optional): The minimum allowable length of the input message. Defaults to 0.
            MaxLength (int, optional): The maximum allowable length of the input message. Defaults to 16.

        Returns:
            bool: True if the length of the input message is within the specified range, False otherwise.

        Raises:
            Exception: If an error occurs during the length check.
        """
        try:
            if len(InputMsg) < MinLength or len(InputMsg) > MaxLength:
                return False
            return True
        except Exception as e:
            raise e;

    def checkIsEmail(InputMsg) -> bool:
        """
        Checks if the given input is a valid email address.

        Args:
            InputMsg (str): The input string to be checked.

        Returns:
            bool: True if the input is a valid email address, False otherwise.

        Raises:
            Exception: If an unexpected error occurs during the validation process.
        """
        try:
            splits = str(InputMsg).split('@')
            if len(splits) != 2:
                return False
            if splits[0] == '' or splits[1] == '':
                return False
            if splits[1].count('.') < 1:
                return False
            return True
        except Exception as e:
            raise e

    def checkIsPhoneNumber(InputMsg, minLength=5) -> bool:
        """
        Checks if the given input message is a valid phone number.

        Args:
            InputMsg (str): The input message to be checked.
            minLength (int, optional): The minimum length of the phone number. Defaults to 5.

        Returns:
            bool: True if the input message is a valid phone number, False otherwise.

        Raises:
            Exception: If an error occurs during the execution.
        """
        try:
            InputMsg = str(InputMsg)
            if len(InputMsg) <= minLength:
                return False
            if not InputMsg.isdigit():
                return False
            return True
        except Exception as e:
            raise e;

    def checkPassword(InputMsg, MinLength=8, MaxLength=16, Letters=True, Numbers=True, Symbols=True, Spaces=False) -> bool:
        """
        Checks if the given password meets the specified criteria.

        Args:
            InputMsg (str): The password to be checked.
            MinLength (int, optional): The minimum length of the password. Defaults to 8.
            MaxLength (int, optional): The maximum length of the password. Defaults to 16.
            Letters (bool, optional): Whether the password must contain letters. Defaults to True.
            Numbers (bool, optional): Whether the password must contain numbers. Defaults to True.
            Symbols (bool, optional): Whether the password must contain symbols. Defaults to True.
            Spaces (bool, optional): Whether the password can contain spaces. Defaults to False.

        Returns:
            bool: True if the password meets all criteria, False otherwise.

        Raises:
            Exception: If an error occurs during the password check.
        """
        try:
            InputMsg = str(InputMsg)
            if not InputChecker.checkForLength(InputMsg, MinLength, MaxLength):
                return False
            if not InputChecker.checkFor(InputMsg, Letters, Numbers, Symbols, Spaces):
                return False
            return True
        except Exception as e:
            raise e;

    def inputCleaner(InputMsg) -> str:
        """
        Cleans the input message by converting it to a string and stripping any leading or trailing whitespace.

        Args:
            InputMsg: The input message to be cleaned.

        Returns:
            str: The cleaned input message as a string.
        """
        return str(InputMsg).strip()
    
    def getCountOf(InputMsg, Letters=False, Numbers=False, Symbols=False, Spaces=False):
        """
        Counts the occurrences of specified character types in the input message.
        Parameters:
        InputMsg (str): The input message to be analyzed.
        Letters (bool): If True, count the number of letters in the input message.
        Numbers (bool): If True, count the number of digits in the input message.
        Symbols (bool): If True, count the number of symbols (non-alphanumeric and non-space characters) in the input message.
        Spaces (bool): If True, count the number of spaces in the input message.
        Returns:
        list: A list containing the counts of the specified character types in the following order: [letters, numbers, symbols, spaces].
              The list will only include counts for the character types that were marked as True in the parameters, but will maintain the order.
        Examples:
        >>> getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False)
        [5, 3, 1]
        >>> getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=True)
        [5, 3, 1, 0]
        >>> getCountOf("Hello123!", Letters=True, Numbers=False, Symbols=True, Spaces=False)
        [5, 1]
        """
        # Function die zählt wieviel von dem exisitiert was man mit "True" angegeben hat.
        # Gibt ein Array zurück mit den Werten in der Reihenfolge: [Buchstaben, Zahlen, Symbole, Leerzeichen]
        # Dieses Array hat nur die Werte, die man mit True markiert hat, trotzdem gleiche Reihenfolge wie oben.
        # Beispiel: getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False)
        # Output: [5, 3, 1] -> 5 Buchstaben, 3 Zahlen, 1 Symbol
        # Beispiel: getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=True)
        # Output: [5, 3, 1, 0] -> 5 Buchstaben, 3 Zahlen, 1 Symbol, 0 Leerzeichen
        # Beispiel: getCountOf("Hello123!", Letters=True, Numbers=False, Symbols=True, Spaces=False)
        # Output: [5, 1] -> 5 Buchstaben, 1 Symbol
        try:
            InputMsg = str(InputMsg)
            resultArray = []
            if Letters:
                has_letter = sum(1 for c in InputMsg if c.isalpha())
            else:
                has_letter = 0
                
            if Numbers:
                has_number = sum(1 for c in InputMsg if c.isdigit())
            else:
                has_number = 0
                
            if Symbols:
                has_symbol = sum(1 for c in InputMsg if not c.isalnum() and not c.isspace())
            else:
                has_symbol = 0
                
            if Spaces:
                has_space = sum(1 for c in InputMsg if c.isspace())
            else:
                has_space = 0
                
            if Letters:
                resultArray.append(has_letter)
            if Numbers:
                resultArray.append(has_number)
            if Symbols:
                resultArray.append(has_symbol)
            if Spaces:
                resultArray.append(has_space)
                
            return resultArray
        except Exception as e:
            raise e;

def FunctionTest_InputChecker():
    print("FunctionTest - InputChecker")
    print()
    print("CheckFor")
    print()
    print(InputChecker.checkFor("Hello", Letters=True))  # True
    print(InputChecker.checkFor("Hello12", Numbers=True))  # False Cuz it has letters
    print(InputChecker.checkFor("Hello12!", Symbols=True))  # False Cuz it has letters and Numbers
    print(InputChecker.checkFor("Hello 123", Letters=True, Numbers=True, Spaces=True))  # False cuz it has Letters and Numbers and no Spaces
    print(InputChecker.checkFor("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False))  # True has all except spaces
    print()
    print("checkForLength")
    print()
    print(InputChecker.checkForLength("Hello", MinLength=1, MaxLength=5)) # True
    print(InputChecker.checkForLength("Hello12",  MinLength=1, MaxLength=5)) # False
    print(InputChecker.checkForLength("H",  MinLength=3, MaxLength=20)) # False
    print(InputChecker.checkForLength("Hel",  MinLength=3, MaxLength=5)) # True
    print(InputChecker.checkForLength("",  MinLength=1, MaxLength=5)) # False
    print()
    print("checkIsEmail")
    print()
    print(InputChecker.checkIsEmail(None))  # False no dot
    print(InputChecker.checkIsEmail(2))  # False no dot
    print(InputChecker.checkIsEmail("Bob2webde"))  # False no dot
    print(InputChecker.checkIsEmail("Bob@web.de"))  # True Valid
    print(InputChecker.checkIsEmail("Bob@we.b.de"))  # True Valid
    print(InputChecker.checkIsEmail("Bobaweb.de"))  # False no @
    print(InputChecker.checkIsEmail("Bobwebde"))  # False no @ and dot
    print()
    print("checkIsPhoneNumber")
    print()
    print(InputChecker.checkIsPhoneNumber("1234"))  # False too short
    print(InputChecker.checkIsPhoneNumber("123456"))  # True
    print(InputChecker.checkIsPhoneNumber("123456789"))  # True
    print(InputChecker.checkIsPhoneNumber("1234",minLength=3))  # True
    print()
    print("checkPassword")
    print()
    print(InputChecker.checkPassword("Hello1234", MinLength=8, MaxLength=16, Letters=True, Numbers=True, Symbols=True, Spaces=False))  # False has all is 8-16 long, got letters, numbers but no spaces and symbols
    print(InputChecker.checkPassword("Hello1234!", MinLength=8, MaxLength=16, Letters=True, Numbers=True, Symbols=True, Spaces=False))  # True has all is 8-16 long, got letters, numbers and symbols and no spaces
    print(InputChecker.checkPassword("Hello!!", MinLength=8, MaxLength=16, Letters=True, Numbers=False, Symbols=True, Spaces=False))  # False is not long enough, got letters, symbols but no spaces and numbers
    print()
    print("inputCleaner")
    print()
    print(InputChecker.inputCleaner(" Hello ")) # Hello without spaces
    print(InputChecker.inputCleaner("Hello")) # Hello without spaces
    print(InputChecker.inputCleaner("Hello ")) # Hello without spaces
    print(InputChecker.inputCleaner(" Hello")) # Hello without spaces
    print()
    print("getCountOf")
    print()
    print(InputChecker.getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False))
    print(InputChecker.getCountOf("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=True))
    print(InputChecker.getCountOf("Hello!", Letters=True, Numbers=False, Symbols=True, Spaces=False))
    print(InputChecker.getCountOf("Hello12 3!", Letters=True, Numbers=False, Symbols=True, Spaces=False))
    print(InputChecker.getCountOf("Hello!", Letters=True, Numbers=True, Symbols=True, Spaces=False))
    print()
    print("checkForWithExtraInfos")
    print()
    print(InputChecker.checkForWithExtraInfos("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=False))
    print(InputChecker.checkForWithExtraInfos("Hello123!", Letters=True, Numbers=True, Symbols=True, Spaces=True))
    print(InputChecker.checkForWithExtraInfos("Hello!", Letters=True, Numbers=False, Symbols=True, Spaces=False))#
    print(InputChecker.checkForWithExtraInfos("Hello12 3!", Letters=True, Numbers=False, Symbols=True, Spaces=False))
    print(InputChecker.checkForWithExtraInfos("Hello!", Letters=True, Numbers=True, Symbols=True, Spaces=False))
    
    # FunctionTest - InputChecker

    # CheckFor

    # True
    # False
    # False
    # True
    # True

    # checkForLength

    # True
    # False
    # False
    # True
    # False

    # checkIsEmail

    # False
    # False
    # False
    # True
    # True
    # False
    # False

    # checkIsPhoneNumber

    # False
    # True
    # True
    # True

    # checkPassword

    # False
    # True
    # False

    # inputCleaner

    # Hello
    # Hello
    # Hello
    # Hello

    # getCountOf

    # [5, 3, 1]
    # [5, 3, 1, 0]
    # [5, 1]
    # [5, 1]
    # [5, 0, 1]

    # checkForWithExtraInfos

    # [True, 5, 3, 1]
    # [False, 5, 3, 1, 0]
    # [True, 5, 1]
    # [False, 5, 1]
    # [False, 5, 0, 1]
