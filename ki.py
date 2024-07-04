import string
import random

chars = string.ascii_letters + string.digits + string.punctuation
SECRET_KEY = ''.join(random.choice(chars) for _ in range(50))

print(SECRET_KEY)
