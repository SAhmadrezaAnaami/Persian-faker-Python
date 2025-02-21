import random
from src.utils.loadData import load_data
from src.utils.ir_national_code import ir_national_code

class PersianDataFaker:
    def __init__(self):
        print("Welcome to Persian Fake Data Generator.")
        self.personal_data = load_data("src/data/person.json")
        self.INC = ir_national_code()
        
    # Persian Fake name and family generator
    
    def getFirstName(self, gender : str | None = None) -> str:
        """
        Returns a random Persian first name based on gender
        
        Args:
            gender (str): Must be either "male" or "female" or "None" (no different)
        Returns:
            str: A random Persian first name
        Raises:
            Returns "Invalid gender" if gender is not "male" or "female"
        """
        
        if gender is None:
            return random.choice(self.personal_data["M"] + self.personal_data["F"])
        
        if gender == "male":
            return random.choice(self.personal_data["M"])
        elif gender == "female":
            return random.choice(self.personal_data["F"]) 
        else:
            return "Invalid gender"
        
    def getLastName(self) -> str:
        """
        Returns:
            str: A random Persian last name
        """

        return random.choice(self.personal_data["LN"])
    
    def getTitleForName(self, gender : str | None = None) -> str:
        """
        Args:
            gender (str): Must be either "male" or "female" or "None" (no different)

        Returns:
            str: A random Persian title for name
        """

        if gender is None:
            return random.choice(self.personal_data["Titles"]["M"] + self.personal_data["Titles"]["F"])

        if gender == "male":
            return random.choice(self.personal_data["Titles"]["M"])
        elif gender == "female":
            return random.choice(self.personal_data["Titles"]["F"])
        else:
            return "Invalid gender"
        
    def getUserName(self, gender : str | None = None , haveTitle : bool = False , nameSeprator : str = " ") -> str:
        """
        Args:
            gender (str): Must be either "male" or "female" or "None" (no different)
            haveTitle (bool): add title to the start of the username or not
            nameSeprator (str) : string that seprate first name and lastname and title

        Returns:
            str: A random Persian username based on the input gender
        """

        firstName = self.getFirstName(gender)
        lastName = self.getLastName()

        if haveTitle:
            title = self.getTitleForName(gender)
            return title + nameSeprator + firstName + nameSeprator + lastName

        return firstName + nameSeprator + lastName

    # Persian Fake National Code generator

    def getRandomNationalCode(self , getCityName : bool = True) -> str:
        """
        Args:
            getCityName (bool) if true returns the name of the city of national code too
        
        Returns:
            str: A random Persian national code
        """
        if getCityName:
            return self.INC.randomCode()
        else:
            return self.INC.randomCode()[0]
        
    def validateNationalCode(self, nationalCode : str) -> bool:
        """
        Args:
            nationalCode (str): The national code to be validated

        Returns:
            bool: True if the national code is valid, False otherwise
        """
        return self.INC.validator(nationalCode)
