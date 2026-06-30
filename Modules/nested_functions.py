def greet_pythons(items: list) -> None:
    greetings = "Hello"  # enclosing scope for make_greetings
    print(f"The id of `greeting` in `greet_pythons` is {id(greetings)}")
    print(f"local namespace `greet_python`(1): {locals()}")

    def make_greeting(item: str) -> str:
        print(f"local namespace`make_greeting`(1): {locals()}")
        greetings = "Hi"
        print(f"The id of `greeting` in `make_greeting` is {id(greetings)}")
        print(f"local namespace `make_greeting`(2): {locals()}")
        return f"{greetings} {item}"

    for item in items:
        print(make_greeting(item))
    print(f"Inside greet_pythons, `greetings` is {greetings}")
    print(f"The id of `greeting` in `greet_pythons` is {id(greetings)}")
    print(f"local namespace `greet_python`(2): {locals()}")


names = ["John"]  # ,"Eric", "Graham", "Terry", "Michael"]

greet_pythons(names)
