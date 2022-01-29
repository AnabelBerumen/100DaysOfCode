def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['lola','lauren','angelina']

greet_users(usernames)