class CartePizzeriaException(Exception):
    def __init__(self, name: str):
        super().__init__(f"La pizza '{name}' n'existe pas sur la carte.")
        self.name = name