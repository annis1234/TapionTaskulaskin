# Tapion Taskulaskin

Tapion taskulaskin on aputyökalu metsänmittaamiseen. Sovelluksen käyttäjä voi sisäänkirjautumisen jälkeen luoda koealoja csv-tiedostona ja 
lisätä valitsemalleen koealalle puita. Puun yhteydessä tallennetaan puulaji sekä puun
läpimitta ja pituus. Sovellus laskee ja palauttaa käyttäjä valitseman 
koealan puista lasketut koealakohtaiset keskitunnukset: pääpuulajin,
 keskiläpimitan, keskipituuden ja hehtaarikohtaisen tilavuusestimaatin. Lisäksi sovellus piirtää kuvaajan koealan puiden pituus-läpimitta-relaatioista.
 
 Koeala nimetään ilman .csv-päätettä. Puutunnukset kirjataan kokonaislukuna tai desimaalilukuna, jolloin desimaalierottimena toimii piste.
Sovellus olettaa, että mitatut koealat ovat standardikokoisia 50 x 50 m aloja.

Koealatiedostot eivät ole käyttäjäkohtaisia, mikä mahdollistaa sen, että kaikki käyttäjät, joilla on pääsy hakemistoon, voivat kirjata puita samaan tiedostoon. Puun tallentamisen yhteydessä kirjataan myös sen tallentanut käyttäjä.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
[Työaikakirjanpito](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
[Changelog](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
[Arkkitehtuurikuvaus](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
[Käyttöohje](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kayttoohje.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta sovellus komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

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
