def userid(user_id):  # Function for user ID
    if len(user_id) > 256:
        return 0, 0  # Return 0,0 if the length exceeds the maximum allowed
    elif user_id[0] == '@':
        return 0, 0  # Return 0,0 if the user ID starts with '@'
    else:
        if '@' in user_id:
            parts = user_id.split('@', 1)  # Ensure only the first '@' is used to split
            if len(parts) != 2:
                return 0, 0  # Return 0,0 if there's not exactly one '@'
            local, domain = parts
            status_local = check_local(local)  # Check if the local part is valid
            status_dom = check_domain(domain)  # Check if the domain part is valid
            return status_local, status_dom
    return 0, 0  # Return 0,0 if '@' is not present

def allowed():  # Function to return allowed characters for validation
    lowercase_letters = ''.join([chr(i) for i in range(97, 123)])  # Generate lowercase letters
    uppercase_letters = ''.join([chr(i) for i in range(65, 91)])  # Generate uppercase letters
    numbers = '0123456789'  # Numbers
    sym_bols = '!@#$%&*_'
    alpha_numeric = lowercase_letters + uppercase_letters + numbers + sym_bols  # Combine all allowed characters
    return alpha_numeric

def check_local(local):  # Function to check the local part of the email
    x = allowed()  # Get allowed characters
    for i in range(len(local)):
          if local[i] not in x:  # If any character in local is not allowed
            return 0  # Return 0 if invalid character is found
          return 1  # Return 1 if all characters are valid

def check_domain(domain):  # Function to check the domain part of the email
    y = allowed()  # Get allowed characters
    tld = ['com', 'org', 'edu']  # Valid top-level domains (TLD)
    
    if domain[0] == '-' or domain[-1] == '-':  # Domain cannot start or end with '-'
        return 0
    
    domain_parts = domain.split('.')  # Split domain by '.'
    if len(domain_parts) < 2:  # There must be at least one '.' in the domain
        return 0
    
    for part in domain_parts[:-1]:  # Check all parts except the last (TLD)
        for char in part:
            if char not in allowed():  # If any character is not allowed
                return 0
    
    if domain_parts[-1] not in tld:  # Check if the last part is a valid TLD
        return 0
    
    return 1  # Return 1 if domain is valid

# Handling multiple user IDs
n = int(input("Enter the number of users: "))
for i in range(n):
    user_id = input("Enter the user id: ")
    check_id_1, check_id_2 = userid(user_id)  # Function call for checking user id
    
    if check_id_1 and check_id_2:  # If both local and domain are valid
        print("**VALID** --", user_id)
    else:
        print("INVALID --", user_id)
