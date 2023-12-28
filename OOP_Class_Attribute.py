class Bird:
    # Class attribute
    is_hungry = True




# 1st use case. accessing attribute with class name
# parakeet = Bird()
# parrot = Bird()

# Bird.is_hungry = False

# print("parakeet.is_hungry: ", parakeet.is_hungry)
# print("parrot.is_hungry: ", parrot.is_hungry)



#2nd use case. accessing attribute with instance name
parakeet = Bird()
parrot = Bird()

parakeet.is_hungry = False

print("parakeet.is_hungry: ", parakeet.is_hungry)
print("parrot.is_hungry: ", parrot.is_hungry)
