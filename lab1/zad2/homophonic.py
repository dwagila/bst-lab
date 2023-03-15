#!/usr/bin/env python

from random import shuffle
from math import ceil, floor

# Types
language_characteristic = list[tuple[str, float]]
alphabet = list[str]

class HomophonicCipher:

    plaintext_characteristic: language_characteristic
    substitution_alphabet: alphabet
    symbol_length: int
    keep_whitespace: bool
    homophones: dict[str, str]

    allow_weak: bool

    def is_alphabet_sufficient(self) -> bool:
        """Sprawdza czy wybrany alfabet podstawień jest wystarczający dla rozmycia podanej charakterystyki"""

        if len(self.substitution_alphabet) < len(self.plaintext_characteristic):
            # Podstawień nie starczy na cały alfabet
            return False

        """
        Trochę bezużytecznej heurystyki:
        np. jeżeli 'a' występuje 24x częściej od 'f'
            to na 'a' powinno przypadać 24x więcej znaków,
            by móc częstotliwość 'a' "rozmyć" na równi z 'f'.

        Za bazową częstotliwość weźmiemy tę największą: 'a' (0.1004)
        Aby wszystko być w stanie do niej przyrównać potrzeba alfabetu o długości:
            sum([ceil(0.1004/x[1]) for x in POLISH_CHARACTERISTIC])
            103
        """

        # max_freq = max(self.plaintext_characteristic, key=lambda x: x[1])
        # s = sum([ceil(max_freq/x[1]) for x in self.plaintext_characteristic])

        # if len(self.substitution_alphabet) < s and not self.allow_weak:
        #     # Podstawień jest za mało by zamaskować charakterystykę języka
        #     # Nie jest to krytyczny błąd, ale lepiej nie używać takiego mapowania
        #     return False

        return True

    def is_alphabet_consistent(self) -> bool:
        """Sprawdza czy alfabet ma znaki równej długości"""
        sample = self.substitution_alphabet[0]
        if False in [len(x) == len(sample) for x in self.substitution_alphabet]:
            return False
        return True

    def generate_homophones(self) -> dict[str, str]:
        """Tworzy nowe losowe mapowanie homofonów maskujące charakterystykę (c) z alfabetu (a)."""

        def split_ratio(arr: list, *ratios: float) -> list[list]:
            """Rozdziela listę na listy o podanej proporcjonalnej długości przynajmniej 1"""

            shuffle(arr)

            o_len = len(arr) - len(ratios)
            m = []
            for ratio in ratios:
                h = [arr.pop()]
                #print(f'A:{1 + round(ratio * o_len)} 4 f:{ratio:.4f} from:{len(arr)}')
                for _i in range(round(ratio * o_len)):
                    try:
                        h.append(arr.pop())
                    except:
                        pass
                m.append(h)
            return m

        translations = split_ratio(
            [l for l in self.substitution_alphabet],
            *[x[1] for x in self.plaintext_characteristic])
        return {x[0]: x[1] for x in zip([a[0] for a in self.plaintext_characteristic], translations)}

    def decrypt(self, c: str) -> str:
        """Odszyfrowuje szyfrogram (c)"""
        plaintext = ''
        consumable = c[:]

        i = 0
        while len(consumable) != 0:

            if consumable[i] in [' ', '\n', '\t'] and self.keep_whitespace:
                plaintext += consumable[i]
                consumable = consumable[1:]
                continue

            s = consumable[:self.symbol_length]
            consumable = consumable[self.symbol_length:]

            if s not in self.substitution_alphabet:
                raise Exception('Invalid ciphertext')

            plaintext += next((x[0]
                              for x in self.homophones.items() if s in x[1]))

        return plaintext

    def encrypt(self, m: str) -> str:
        """Szyfruje tekst jawny (m)"""
        from random import choice

        ciphertext = ''
        for s in m:
            if s in [' ', '\n', '\t'] and self.keep_whitespace:
                ciphertext += s
                continue

            if s not in self.homophones:
                continue

            ciphertext += choice(self.homophones[s])

        return ciphertext

    def __init__(self, characteristic: language_characteristic, alphabet: alphabet, allow_weak: bool = False, keep_whitespace: bool = True) -> None:
        """
        allow_weak:
            Pozwala na utworzenie szyfru dysponującego niebezpiecznie niską ilością homofonów.
        keep_whitespace:
            Ustawienie False powoduje, że znaki białe będą podlegały tłumaczeniu na alfabet.
            Ważne, aby charakterystyka języka zawierała rozkład wliczając białe znaki.
        """

        self.plaintext_characteristic = sorted(characteristic, key=lambda x: x[1])
        self.substitution_alphabet = alphabet
        self.allow_weak = allow_weak
        self.keep_whitespace = keep_whitespace

        if not self.is_alphabet_consistent():
            raise Exception('Alphabet characters have to be of equal length.')

        self.symbol_length = len(alphabet[0])

        if not self.is_alphabet_sufficient():
            raise Exception('Given ciphertext alphabet is too short.')

        self.homophones = self.generate_homophones()


# ogonki są brzydkie, więc zostały unicestwione
POLISH_CHARACTERISTIC = [
    ('a', 0.1004), ('b', 0.0139), ('c', 0.0420),
    ('d', 0.0323), ('e', 0.0849), ('f', 0.0041),
    ('g', 0.0154), ('h', 0.0125), ('i', 0.0809),
    ('j', 0.0226), ('k', 0.0354), ('l', 0.0418),
    ('m', 0.0273), ('n', 0.0602), ('o', 0.0879),
    ('p', 0.0292), ('r', 0.0506), ('s', 0.0504),
    ('t', 0.0394), ('u', 0.0259), ('w', 0.0478),
    ('y', 0.0370), ('z', 0.0589)
]
ALPHABET = [f'{x:02x}' for x in range(256)]
