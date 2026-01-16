from abc import ABC, abstractmethod
import random
import string
import nltk

nltk.download('words')

class PasswordGenerator(ABC):
    '''
    Abstract base class for password generators.
    '''
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    '''
    Generates a numeric PIN of specified length.
    '''
    def __init__(self, length: int = 8):
        self.length = length

    def generate(self) -> str:
        return(''.join(random.choice(string.digits) for _ in range(self.length)))
       


class RandomPasswordGenerator(PasswordGenerator):
    '''
    Generates a random password with options for length, symbols, and numbers.
    '''
    def __init__(self, length: int = 8, include_symbols: bool = False, include_numbers: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
            
    def generate(self) -> str:
        return(''.join(random.choice(self.characters) for _ in range(self.length)))
    


class MemorablePasswordGenerator(PasswordGenerator):
    '''
    Generates a memorable password using words from the NLTK corpus.
    '''
    def __init__(self, words_list: list = None, num_words: int = 4, separator: str = '-', capitalize: bool = False):
     
        if words_list is None:
            words_list = nltk.corpus.words.words()
            
        self.words_list = words_list   
        self.capitalize = capitalize
        self.num_words = num_words
        self.separator = separator
              
    def generate(self) -> str:
        password_words = [random.choice(self.words_list) for _ in range(self.num_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word for word in password_words]
        return self.separator.join(password_words)


if __name__ == "__main__":
    pin_gen = PinGenerator(length=6)
    print("Generated PIN:", pin_gen.generate())

    random_pass_gen = RandomPasswordGenerator(length=12, include_symbols=True, include_numbers=True)
    print("Generated Random Password:", random_pass_gen.generate())

    memorable_pass_gen = MemorablePasswordGenerator(num_words=3, separator=' ', capitalize=True)
    print("Generated Memorable Password:", memorable_pass_gen.generate())