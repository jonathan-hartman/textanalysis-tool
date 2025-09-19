def hello(name: str = "User") -> str:
    if name == "":
        raise ValueError("Name cannot be empty.")
    return f"Hello, {name}!"
