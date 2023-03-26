import re
from Core.exceptions import ValidationAPIException

# not working properly
def validate_password(password):
    patterns = [
        '[A-Z]',
        '[a-z]',
        '[0-9]',
        '[#?!@$%^&*\-_]'
    ]
    
    results = []
    for pattern in patterns:
        matchResult = re.search(pattern, password)
        if matchResult is not None:
            print(matchResult)
            results.append(re.match(pattern, password))
    
    print(len(results))
    return len(results) == len(patterns)


def validate_verificationCode(code):
    return bool(re.search("\d{4}", code))

def validate_passportType(value, format):
    return bool(re.search(format, value))