# Solution not complete!!! Edit 18.02.2024 -> solution seems to be working

import re

pattern = r"(.+)@.+(\.[a-z]+)"
domains = (".com", ".bg", ".org", ".net")


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while not email == "End":
    matches = re.findall(pattern, email)
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(matches[0][0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif matches[0][-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()


