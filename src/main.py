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

    def getRandomNationalCodeByCityCode(self , cityCode : str , getCityName : bool = True) -> str:
        """
        Args:
            cityCode (str): The city code to generate the national code for
            getCityName (bool) if true returns the name of the city of national code too

        Returns:
            str: A random Persian national code for the given city code
        """
        if getCityName:
            return self.INC.by_citycode(cityCode)
        else:
            return self.INC.by_citycode(cityCode)[0]
        
    def getRandomNationalCodeByCityState(self , cityState : str, getCityName : bool = True) -> str:
        """
        Args:
            cityState (str): The city state to generate the national code for
            getCityName (bool) if true returns the name of the city of national code too

        Returns:
            str: A random Persian national code for the given city state
        """
        if getCityName:
            return self.INC.by_state(cityState)
        else:
            return self.INC.by_state(cityState)[0]
        
    # get Alls
        
    def getAllCityCodes(self) -> dict:
        """
        Returns:
            dict: A dictionary containing all city codes and their corresponding city names
        """
        return self.INC.city_codes
    
    def getAllNames(self, gender:str|None = None) -> dict:
        """
        Args:
            gender (str): Must be either "male" or "female" or "None" (no different)

        Returns:
            dict: A dictionary containing all names based on the input gender
        """
        if gender is None:
            return {
                "M" : self.personal_data["M"],
                "F" : self.personal_data["F"]
            }

        if gender == "male":
            return self.personal_data["M"]
        elif gender == "female":
            return self.personal_data["F"]
        else:
            return "Invalid gender"
    
    # Persian Fake Phone Number generator
    # TODO validate city regions

    def getRandomPhoneNumber(self) -> str:
        """
        Returns:
            str: A random Persian phone number
        """
        return "09" + str(random.randint(10000000, 99999999))
    
    # Persian Fake Telephone generator
    # TODO validate city regions
    
    def getRandomTelephoneNumber(self) -> str:
        """
        Returns:
            str: A random Persian telephone number
        """
        return "0" + str(random.randint(1000000, 9999999))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    