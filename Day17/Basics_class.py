class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        self.following+=1
        user.followers+=1


user_1 = User("001", "Jerry")
user_2 = User("002", "Tom")


print(f" id || username || following || followers")
print(f"{user_1.id} ||  {user_1.username}  ||     {user_1.following}      ||  {user_1.followers}")
print(f"{user_2.id} ||  {user_2.username}    ||     {user_2.following}      ||  {user_2.followers}")


user_2.follow(user_1)
print("After calling Function follow ",user_2)
print(f" id || username || following || followers")
print(f"{user_1.id} ||  {user_1.username}  ||     {user_1.following}      ||  {user_1.followers}")
print(f"{user_2.id} ||  {user_2.username}    ||     {user_2.following}      ||  {user_2.followers}")