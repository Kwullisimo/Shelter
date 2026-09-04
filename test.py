# 4. @proprety | a better solution if the function is a description and not an action
# class Person(frozen=True) = all arguments in this class frozen
# 5. @classmethod | 
# field

from dataclasses import dataclass, field

@dataclass
class Person():
    login: str
    password: str = field(repr=False)

    def info(self) -> str:
        print(f'{self.login} | {self.password}')

p1 = Person('John', '1234')
p1.info()