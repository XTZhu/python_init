def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile


zwz = build_profile('zhu', 'wenzhe',  age=20, like='pc', height=180, )
print(zwz)
