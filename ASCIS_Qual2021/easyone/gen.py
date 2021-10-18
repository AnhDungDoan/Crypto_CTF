from pki_helpers import generate_private_key, generate_public_key
private_key = generate_private_key("ca-private-key.pem", "secret_password")
print(private_key)
generate_public_key(private_key, filename="ca-public-key.pem", country="US", state="Maryland", locality="Baltimore", org="My CA Company", hostname="admin",)