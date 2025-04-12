def build_profile(name:str, surname:str, **kwargs) -> str:
    output:str = f"{name} {surname}"

    for key, value in kwargs.items():
        output += f", {key} {value}"

    print(output)

build_profile("Andrea", "Mastropietro", age = 19, weight = 85)