import base64
import hashlib
import hmac

"""
def aes_decrypt(ciphertext, key):
  
  Dekripsi data menggunakan AES-256.

  Args:
    ciphertext: Data yang dienkripsi.
    key: Kunci enkripsi.

  Returns:
    Data yang didekripsi.
  

  cipher = hashlib.sha256(key.encode()).digest()
  iv = cipher[:16]
  key = cipher[16:]

  return base64.b64decode(hmac.new(key, ciphertext, hashlib.sha256).digest())
"""

def aes_decrypt(ciphertext, key):
  """
  Dekripsi data menggunakan AES-256.

  Args:
    ciphertext: Data yang dienkripsi.
    key: Kunci enkripsi.

  Returns:
    Data yang didekripsi.
  """

  key = key.encode()  # Encode the string to bytes.

  cipher = hashlib.sha256(key).digest()
  iv = cipher[:16]
  key = cipher[16:]

  return base64.b64decode(hmac.new(key, ciphertext, hashlib.sha256).digest())

if __name__ == "__main__":
  token = "EDDGxGCNH1NdNOaeAbEb2g=="
  key = "BPJSHealthkhaton2023"

  plaintext = aes_decrypt(token, key)
  print(plaintext)
