import hashlib
from hashlib import sha256
texto = "hola"


hash_resultado = hashlib.sha256(texto.encode('utf-8')).hexdigest()


print(f"El hash SHA-256 de '{texto}' es: {hash_resultado}")


texto2 = "Hola"

hash_resultado2 = hashlib.sha256(texto2.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{texto2}' es: {hash_resultado2}")

texto3 = "chao"

hash_resultado3 = hashlib.sha256(texto3.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{texto3}' es: {hash_resultado3}")

texto4 = "Chao"

hash_resultado4 = hashlib.sha256(texto4.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{texto4}' es: {hash_resultado4}")


hash_h = hash_resultado+hash_resultado2
hash = " hola + Hola"

hahs_prueba = hashlib.sha256(hash_h.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{hash}' es: {hahs_prueba}")


hash_h2 = hash_resultado3+hash_resultado4
hash2 = " chao + Chao"

hahs_prueba2 = hashlib.sha256(hash_h2.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{hash2}' es: {hahs_prueba2}")


h3 = hahs_prueba+hahs_prueba2
hash3 = " (hola + Hola) + (chao + Chao)"

hash_prueba3 = hashlib.sha256(h3.encode('utf-8')).hexdigest()

print(f"El hash SHA-256 de '{hash3}' es: {hash_prueba3}")
