## Web Scraping Project: Gintarine & Benu Crawlers

Šis projektas yra įrankis, skirtas duomenų nuskaitymui (web scraping) iš dviejų svetainių: **Gintarine** ir **Benu**. Projektas leidžia nuskaityti informaciją apie produktus iš šių svetainių ir gauti duomenis pasirinktu formatu (JSON, CSV, arba kaip Python sąrašą).

## Programos aprašymas:

Šis įrankis naudojamas nuskaityti duomenis iš dviejų pagrindinių vaistinių svetainių: **Gintarine** ir **Benu**. Jis gali grąžinti informaciją apie produktus įvairiais formatais, priklausomai nuo vartotojo pasirinkimo.

- **Gintarine** svetainės duomenys nuskaityti naudojant `crawl_gintarine`.
- **Benu** svetainės duomenys nuskaityti naudojant `crawl_benu`.

Naudotojas gali pasirinkti laiką, per kurį programa turi atlikti nuskaitymą, ir taip pat gali pasirinkti, kokiu formatu norima gauti duomenis.

Pavyzdys: crawl(source="gintarine", time_limit=60, data_format="json")

Pirmasis parametras nurodo puslapį iš kurios svetainės duomenys bus surenkami:
* gintarinė
* benu

Antrasis parametras nurodo kiek laiko programa veiks

Trečiasis parametras nurodo pagal kokį formatą saugosime gautus duomenis:
* JSON
* CSV
* LIST

## Pypi repozitorija:
pip install mantas-z-mod1-atsiskaitymas
