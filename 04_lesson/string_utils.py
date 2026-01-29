class StringUtils:
    def capitalize(self, s: str) -> str:
        if isinstance(s, str):
            return s.capitalize()
        raise TypeError("Input must be a string.")

    def trim(self, s: str) -> str:
        if isinstance(s, str):
            return s.strip()
        raise TypeError("Input must be a string.")

    def contains(self, s: str, char: str) -> bool:
        if isinstance(s, str) and isinstance(char, str):
            return char in s
        raise TypeError("Both inputs must be strings.")

    def delete_symbol(self, s: str, char: str) -> str:
        if isinstance(s, str) and isinstance(char, str):
            return s.replace(char, '')
        raise TypeError("Both inputs must be strings.")





