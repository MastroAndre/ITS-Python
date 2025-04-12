def describe_city(name:str, country:str = "Italy"):
    print(f"{name} is in {country}")

describe_city("Roma")
describe_city("Bangkok", "Tailandia")
describe_city("Milano")