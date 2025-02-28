# Persian Faker Python 🇮🇷

Generate realistic Persian fake data with ease! This library provides a comprehensive set of tools for generating culturally appropriate Iranian names, national codes, contact information, and administrative data.

![PyPI](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

## Features ✨

✅ **Current Capabilities**:
- [x] Generate Persian first names (male/female/neutral)
- [x] Create realistic full names with titles
- [x] Valid Iranian national code generation with city/state validation
- [x] Phone number generation (mobile & landline formats)
- [x] Persian-to-Finglish email address generation
- [x] Administrative division data (provinces, cities, regions)
- [x] National code validation system
- [x] City/State-specific data generation

🚧 **Future Enhancements**:
- [ ] Address generation (street names, postal codes)
- [ ] Enhanced phone number validation
- [ ] Bank account/IBAN generation
- [ ] Persian company name generator
- [ ] Historical/Shahnameh-inspired name options
- [ ] Improved Finglish transliteration accuracy
- [ ] Web API interface
- [ ] Comprehensive documentation portal

## Installation 🚀

```bash
pip install persian-faker
```

## Basic Usage 📖

```python
from persian_faker import PersianDataFaker

pdf = PersianDataFaker()

# Generate a full profile
profile = {
    "name": pdf.getUserName(gender="female", haveTitle=True),
    "national_code": pdf.getRandomNationalCode(getCityName=True),
    "phone": pdf.getRandomPhoneNumber(),
    "email": pdf.getEmail(),
    "location": pdf.getRandomNationalCodeByCityState("تهران")[1][0]
}

print(profile)
```

## Key Components 🛠️

### 1. Name Generation
```python
pdf.getFirstName(gender="male")  # Returns "محمد"
pdf.getLastName()                # Returns "رضایی"
pdf.getUserName(haveTitle=True)  # Returns "مهندس سارا محمدی"
```

### 2. National Code System
```python
# Generate valid code with city info
code, city_info = pdf.getRandomNationalCodeByCityCode("001")
print(code)        # "0010035987"
print(city_info)   # ["تهران", "تهران مرکزی"]

# Validate existing code
pdf.validateNationalCode("0079930014")  # Returns True
```

### 3. Contact Information
```python
pdf.getRandomPhoneNumber()   # Returns "09123456789"
pdf.getRandomTelephoneNumber() # Returns "02188765432"
pdf.getEmail()                # Returns "ali.ahmadi@gmail.com"
```

## Data Sources 📚
- Contains administrative data for all 31 provinces
- 10,000+ validated name combinations
- City code database with 700+ entries
- Valid national code patterns from official sources

## Contributing 🤝
We welcome contributions! Please help us by:
1. Reporting bugs
2. Adding new name databases
3. Improving transliteration accuracy
4. Expanding administrative data
5. Creating new data generators

## License 📜
Apache License 2.0 - See [LICENSE](LICENSE) for details

Made with ❤️ for Iranian developers by Ahmadreza Anami