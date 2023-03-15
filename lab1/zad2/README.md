# Zadanie 2

Powyższy folder zawiera dwa pliki:

 * [`homophonic.py`](homophonic.py) - implementacja biblioteki tworzącej szyfr homofoniczny z podanym maskowaniem charakterystyki.
 * [`homo.ipynb`](homo.ipynb) - Zeszyt obliczeniowy Jupyter Notebook zawierający wykresy oraz dane statystyczne ukazujące szyfr w akcji.

## Przykłady

Szyfr można wykorzystać w interkatywnym interpreterze języka Python:

```python
 > python -i homophonic.py
>>> cipher = HomophonicCipher(POLISH_CHARACTERISTIC, ALPHABET)
>>> cipher.encrypt('test')
'4ce48fc6'
>>> cipher.encrypt('test')
'fee46905'
>>> t = cipher.encrypt('test')
>>> cipher.decrypt(t)
'test'
>>> 
```