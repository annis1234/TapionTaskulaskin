# Tapion Taskulaskin

Tapion taskulaskin on aputyökalu metsänmittaamiseen. Sovelluksen tämänhetkisessä versiossa käyttäjä voi tallentaa puutunnuksia csv-tiedostoon, ja tulostaa tallennetut puut.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoidaan _htmlcov_-hakemistoon komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
