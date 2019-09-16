from collections import Counter

def deadPpl(b,d):
    birth, death = Counter(b), Counter(d)
    alive, years = 0, {}
    for year in range(min(b), max(d) + 1):
        alive = alive + birth[year] - death[year - 1]
        years[year] = alive
    return max(years, key=years.get)

b = [1903, 1920, 1910, 1951, 2010, 1923, 1970, 1956, 1988, 1975, 1989, 1989]
d = [1976, 1930, 2018, 1952, 2019, 2017, 1998, 2014, 1999, 1994, 1989, 1989]

print(deadPpl(b, d))