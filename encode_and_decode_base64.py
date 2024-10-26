import base64

def encode_payload(payload: str, salt_key: str, salt_index: int) -> str:
    if salt_index < 0 or salt_index > len(payload):
        raise ValueError("Salt index is out of bounds.")

    # Insert the salt key into the payload at the specified index
    salted_payload = payload[:salt_index] + salt_key + payload[salt_index:]
    
    # Encode the salted payload into base64
    encoded_bytes = base64.b64encode(salted_payload.encode())
    encoded_str = encoded_bytes.decode()
    
    return encoded_str

def decode_payload(encoded_payload: str, salt_key: str, salt_index: int) -> str:
    # Decode the base64 encoded payload
    decoded_bytes = base64.b64decode(encoded_payload)
    decoded_str = decoded_bytes.decode()
    
    # Check if the salt key is at the correct index
    if decoded_str[salt_index:salt_index+len(salt_key)] != salt_key:
        raise ValueError("Incorrect salt key or salt index.")
    
    # Remove the salt key from the payload
    original_payload = decoded_str[:salt_index] + decoded_str[salt_index+len(salt_key):]
    
    return original_payload

# Example usage
payload = "HelloWorld"
salt_key = "12345"
salt_index = 5

# Encoding
encoded = encode_payload(payload, salt_key, salt_index)
print("Encoded:", encoded)

# Decoding (correct salt)
try:
    decoded = decode_payload(encoded, salt_key, salt_index)
    print("Decoded:", decoded)
except ValueError as e:
    print("Decoding failed:", e)

# Decoding (incorrect salt key or index)
try:
    decoded = decode_payload(encoded, "54321", salt_index)
    print("Decoded with wrong key:", decoded)
except ValueError as e:
    print("Decoding failed with wrong key:", e)

try:
    decoded = decode_payload(encoded, salt_key, salt_index + 1)
    print("Decoded with wrong index:", decoded)
except ValueError as e:
    print("Decoding failed with wrong index:", e)
