#!/usr/bin/env python

def analyze_ngram(s: str, n: int) -> list[tuple[str, int]]:
    """Zwraca listę dwójek n-gramów oraz ilości ich wystąpień"""

    ngrams = list(zip(*[s.replace(' ', '')[i:] for i in range(n)]))

    distinct_ngrams = set([n for n in ngrams])
    return [(''.join(ngram), ngrams.count(ngram))
            for ngram in distinct_ngrams]


def main(s: str, top: int, longest_n: int) -> None:

    for n in range(1, longest_n + 1):

        ranking = list(analyze_ngram(s, n))
        ranking.sort(key=lambda x: -x[1])

        print(f'{n}-gramy:')
        print(*ranking[:top], sep='\n')
        print()


if __name__ == '__main__':
    
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('szyfrogram', type=str)
    ap.add_argument('top', type=int,
                    help='Ile najpopularniejszych n-gramów wyświetlić')
    ap.add_argument('najdluzszy_ngram', type=int,
                    help='Najdłuższy n-gram do sprawdzenia',
                    default=3, nargs='?')

    args = ap.parse_args()

    main(args.szyfrogram, args.top, args.najdluzszy_ngram)
