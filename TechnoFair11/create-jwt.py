import jwt

# Sample payload data
payload = {
    "id": 1,
   "username": "user",
   "role": "admin",
   "iat": 1719714187,
   "exp": 1719717787
}

# **Warning: Using 'none' algorithm is highly discouraged for security reasons**
encoded_jwt = jwt.encode(payload, "", algorithm="none")

print(encoded_jwt)

