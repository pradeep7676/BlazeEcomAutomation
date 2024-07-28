# User data for testing different scenarios
USER_DATA = {
    # Valid user credentials for successful login and signup
    "valid": {
        "username": "sqnl1@9912.com",  # Valid username for testing
        "password": "91291919"           # Valid password for testing
    },
    # Existing user credentials to test scenarios with already registered users
    "existing": {
        "existing_username": "wings",  # Existing username
        "existing_password": "123123"  # Existing password
    },
    # Invalid user credentials for negative testing
    "invalid": {
        "username": "lnlri@123",     # Invalid username for testing
        "password": "lnlei@123123"     # Invalid password for testing
    },
    # User credentials with special characters for testing input handling
    "specialcha": {
        "spcecial_characters_username": "s1$wd1@!#$.com",  # Username with special characters
        "special_char_Password": "t%$@ewpw@12#"             # Password with special characters
    }
}

# User details for filling out forms during checkout and other processes
USER_DETAILS = {
    'name': 'John Doe',                 # Name of the user
    'country': 'USA',                   # Country of the user
    'city': 'New York',                 # City of the user
    'card': '1234567812345678',         # Credit card number for testing
    'month': '12',                      # Expiry month of the card
    'year': '2025'                      # Expiry year of the card
}
