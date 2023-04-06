import jwt

# jwt key value in the config file
key = "dhLUVrQLOxxxrPf"
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGxvd0dyb3VwIjoiOTcxMWQzNWQtMTJlZi00N2NkLWFkYWQtOGEyODQwMDRiOWRjIiwiZXhwIjoxODM4NDQwNzIwLCJuYW1lIjoic2VlZCIsInJvbGUiOiJub2RlIn0.ge7i-WY12xyHqs9i_D_p7L1VyGxG-dhma6TFuepvcdI"

decoded_token = jwt.decode(jwt_token, key, algorithms=["HS256"])
print(decoded_token)
