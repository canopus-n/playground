from typing import List
from itertools import chain


class Romanizer:
    romans: List[str] = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I'
    ]
    arabics: List[int] = [
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    ]
    assert len(romans) == len(arabics)

    def romanize(self, num) -> str:
        if num == 0:
            return ''
        for i in range(len(self.arabics)):
            if num // self.arabics[i] == 0:
                continue
            return '%s%s' % (self.romans[i], self.romanize(num-self.arabics[i]))

    def romanize_2(self, num):
        remainder = num
        _romans = []
        for i in range(len(self.arabics)):
            if remainder // self.arabics[i] == 0:
                continue
            _romans.append(self.romans[i:i+1]*(remainder // self.arabics[i]))
            remainder = remainder % self.arabics[i]
        return ''.join(chain.from_iterable(_romans))


def main():
    romanizer = Romanizer()
    print(romanizer.romanize_2(333))


if __name__ == '__main__':
    main()
