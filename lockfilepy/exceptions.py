class LolClientNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("League of legends client was not found.")


class LockfileNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Lockfile was not found.")
