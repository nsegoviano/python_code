class Shark:
    #Test comment
    # Class variables
    animal_type = "fish"
    location = "ocean"
    #followers = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")

    def main():
        
new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)



