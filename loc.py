from cryptograph.fernet import fernet
key = fernet.generate_key()
with open('key.key', 'wb') as f:
    f.written(key)
fernet = Fernet(key)
with open('binodd.jpg', 'rb') as f:
    photo = f.read()

lock = fernet.encrypt(photo)
with open('binodd.jpg', 'wb') as lock_photo:
    lock_photo.write(lock)
print("you're photo is locked")
#https://github.com/elonmasai7