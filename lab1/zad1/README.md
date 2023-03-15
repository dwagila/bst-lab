# Zadanie 1

Powyższy program liczy częstotliwość występowania n-gramów w podanym tekście.

## Przykłady

```
usage: ngram.py [-h] szyfrogram top [najdluzszy_ngram]

positional arguments:
  szyfrogram
  top               Ile najpopularniejszych n-gramów wyświetlić
  najdluzszy_ngram  Najdłuższy n-gram do sprawdzenia

options:
  -h, --help        show this help message and exit

```

Przykład zastosowania na szyfrogramie z zadania 1:
```sh
 > python ngram.py 'WXQOWK LXCFRXBCXUAWJO R URXLXCFRXBCXUAWJO J AKAWXQOBM WXNXRUSDEQOWKBCUKBM FDEPACOQK UO NOLDEOWDEROBM' 3 15
1-gramy:
('X', 11)
('O', 10)
('W', 8)

2-gramy:
('DE', 4)
('RX', 3)
('WX', 3)

3-gramy:
('UAW', 2)
('XBC', 2)
('AWJ', 2)

4-gramy:
('XCFR', 2)
('CXUA', 2)
('LXCF', 2)

5-gramy:
('LXCFR', 2)
('CXUAW', 2)
('FRXBC', 2)

6-gramy:
('LXCFRX', 2)
('XCFRXB', 2)
('RXBCXU', 2)

7-gramy:
('LXCFRXB', 2)
('XBCXUAW', 2)
('XCFRXBC', 2)

8-gramy:
('CFRXBCXU', 2)
('FRXBCXUA', 2)
('XBCXUAWJ', 2)

9-gramy:
('RXBCXUAWJ', 2)
('LXCFRXBCX', 2)
('CFRXBCXUA', 2)

10-gramy:
('LXCFRXBCXU', 2)
('FRXBCXUAWJ', 2)
('XCFRXBCXUA', 2)

11-gramy:
('LXCFRXBCXUA', 2)
('CFRXBCXUAWJ', 2)
('FRXBCXUAWJO', 2)

12-gramy:
('XCFRXBCXUAWJ', 2)
('LXCFRXBCXUAW', 2)
('CFRXBCXUAWJO', 2)

13-gramy:
('XCFRXBCXUAWJO', 2)
('LXCFRXBCXUAWJ', 2)

14-gramy:
('LXCFRXBCXUAWJO', 2)

15-gramy:
```