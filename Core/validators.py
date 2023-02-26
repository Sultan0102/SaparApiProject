import re
from Core.exceptions import ValidationAPIException

# not working properly
def validate_password(password):
    patterns = [
        r'([A-Z])',
        r'([a-z])',
        r'([0-9])',
        r'([#?!@$%^&*-_])'
    ]
    
    results = []
    for pattern in patterns:
        matchResult = re.match(pattern, password)
        if matchResult is not None and len(matchResult.group(0)) != 0:
            print(matchResult.group(0))
            results.append(re.match(pattern, password))
    
    print(results)
    print(len(results))
    return len(results) == len(patterns)
