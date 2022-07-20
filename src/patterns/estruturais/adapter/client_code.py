from interface.target import Target

def client_code(target: "Target") -> None:
    """O código cliente suporta todas as classes que seguem a interface Target."""
    print(target.request(), end="")