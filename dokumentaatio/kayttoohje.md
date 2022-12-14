# Käyttöohje

## Ohjelman käyttöönotto

Lataa sovelluksen viimeisimmän [releasen](https://github.com/annis1234/TapionTaskulaskin/releases/tag/Loppupalautus) lähdekoodi ja pura se haluamaasi paikkaan. Siirry kansioon TapionTaskulaskin-Loppupalautus ja toimi seuraavasti:

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
## Konfigurointi

Käyttäjätietojen tallennukseen käytettävä tietokanta konfiguroidaan käynnistyshakemiston .env-tiedostossa, jossa sitä on mahdollista muokata. Tietokanta tallennetaan data-hakemistoon. Koealatiedostot konfiguroidaan käyttöliittymän kautta, ja ne tallennetaan data/plots-hakemistoon.

## Kirjautuminen ja uuden käyttäjätunnuksen luominen

Sovellus käynnistyy sisäänkirjautumisnäkymään (kuvassa vasemmalla). Jos käyttäjällä on jo olemassaoleva käyttäjätunnus, sovellukseen kirjaudutaan kirjoittamalla käyttäjätunnus ja salasana syötekenttiin ja painamalla "Kirjaudu sisään". Jos käyttäjällä ei ole käyttäjätunnusta, hän voi luoda sellaisen painamalla "Uusi käyttäjä". Uuden käyttäjän luomisnäkymässä (kuvassa oikealla) käyttäjä kirjoittaa haluamansa tunnuksen ja salasanan, ja klikkaa "Luo uusi". Tunnuksen luomisen jälkeen sovellus kirjaa käyttäjän automaattisesti sisään.

![start](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/start.png)

## Koealatiedostojen käsittely

Kirjautumisen jälkeen aukeaa näkymä, jossa käyttäjä voi luoda uuden koealatiedoston tai avata jo olemassa olevan tiedoston. Näkymässä on listaus mahdollisesti jo olemassaolevista tiedostoista.  Koealatiedosto luodaan kirjoittamalla sen nimi syötekenttään ilman .csv-päätettä, ja klikkaamalla "Luo koeala". Tiedosto avataan klikkaamalla halutun koealan kohdalla olevaa "Avaa koeala"-painiketta. Käyttäjä voi myös poistaa koealatiedoston valitsemalla "Poista koeala". Tällöin on syytä huomoida, että tiedosto katoaa lopullisesti, eikä sitä voi sovelluksen kautta enää palauttaa. Uloskirjautuminen tapahtuu klikkaamalla "Kirjaudu ulos".

![handle_plots_view](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/handle_plots_view.png)

## Puun lisääminen koealalle ja koealan tietojen katselu

Koealatiedoston valittuaan käyttäjä voi lisätä puita koealalle (vasen näkymä). Puun tiedot (puulaji, läpimitta ja pituus) syötetään syötekenttiin, ja klikataan "Lisää puu". Käyttäjä voi tyhjentää koealan klikkaamalla "Tyhjennä koeala". Koealan puustotiedot avautuvat klikkaamalla "Näytä koealan tiedot" (oikea näkymä). Käyttäjä voi siirtyä takaisin puun lisäämisnäkymään sekä puun lisäämisnäkymästä edelleen koealalistaukseen klikkaamalla "Takaisin".

![handle_stand_data](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/handle_stand_data.png)
