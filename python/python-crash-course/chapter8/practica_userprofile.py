def user_info(first,last,**user_data):
    user_data['first'] = first
    user_data['last'] = last
    
    return user_data

user_profile = user_info('lauren','jauregui', ocupation = 'singer', eyes = 'green')
print(user_profile)
