def mk_sandwich(*args):
    sandwich:list = []
    for m in args:
        sandwich.append(m)
    print(f"sandwich = {sandwich}")

mk_sandwich("salad", "tomato", "cheese")