# Arkkitehtuurikuvaus

## Rakenne

Ohjelma sisältää hakemistot ui, repositories, services ja entities. Hakemisto ui sisältää ohjelman käyttöliittymän koodin ja services sovelluslogiikkaa hoitavan koodin. Hakemiston repositories sisältävä koodi vastaa tiedon tallentamisesta, ja entities sisältää sovelluksen tietokohteita kuvaavat luokat.

Sovelluksen rakenne luokkakaaviona:

![Luokkakaavio](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/luokkakaavio.png)

## Käyttöliittymä

Käyttöliittymä sisältää viisi näkymää:

- Sisäänkirjautuminen
- Uuden käyttäjän luominen
- Olemassa olevien koealatiedostojen listaus ja uuden tiedoston luominen
- Puiden lisääminen valittuu koealatiedostoon
- Valitun koealan puustotietojen katselu

Näkymät ovat eriytettyinä omiin luokkiinsa. Luokka UI vastaa näkymien  esittämisestä ja niiden vaihtamisesta. Käyttöliittymän luokat käyttävät 
PlotService-luokan metodeja toiminnallisuuksien toteuttamiseen.

## Sovelluslogiikka

Sovelluksen keskeiset luokat ovat User ja Tree, jotka vastaavat sovelluksen käyttäjän ja sovelluksen kautta luotujen puiden kuvaamisesta. Luokka PlotService toteuttaa sovelluksen toiminnallisuudet. Sovelluksen keskeisimmät toiminnallisuudet ovat:

- Käyttäjän luominen
- Sisäänkirjautuminen olemassaolevalla tunnuksella ja salasanalla
- Koealatiedoston luominen
- Puun tallentaminen koealalle
- Valitun koealan puustotietojen laskeminen 

PlotService-luokka sisältää metodit jokaisen toiminnallisuuden toteuttamiseksi. Tiedostojen käsittelystä vastaavat PlotRepository- ja UserRepository-luokat

## Tiedon pysyväistallennus

Tiedon tallentamisesta vastaavat luokat PlotRepository ja UserRepository.

Puut tallennetaan csv-tiedostoon, jonka nimen käyttäjä määrittelee. Tiedosto tallennetaan erillisessä konfiguraatiotiedostossa määritellyn polun mukaisesti data/plots-hakemistoon.

Käyttäjän tallentamiseen käytetään SQLite-tietokantaa, joka alustetaan initialize_database.py-tiedostossa.

## Päätoiminnallisuudet

### Koealan luominen ja valitseminen

![Sekvenssikaavio1](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssikaavio_1.png)

Koealan luomisnäkymässä kirjoitetaan koealan nimi ja klikataan "Luo koeala". Tapahtumankäsittelijä kutsuu luokan PlotService 
metodia create_plot parametrinaan käyttäjän antama koealan nimi. PlotService puolestaan kutsuu PlotRepository-luokan metodia 
create (parametrina edelleen koelana nimi), joka luo csv-tiedoston annetulla nimellä. Koealan valitseminen tapahtuu samalla 
periaatteella, paitsi tiedoston luomisen sijasta PlotRepository-luokan metodi select_plot asettaa sille parametrina annetun 
tiedoston nimen polkuun.

### Puun lisääminen koealalle ja koealan keskitunnusten tarkastelu

![Sekvenssikaavio2](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/sekvenssikaavio_2.png)

Puun lisääminen tapahtuu kirjoittamalla puutunnukset ja klikkaamalla "Lisää puu". Tapahtumakäsittelijä kutsuu luokkaa Tree, 
jossa luodaan Tree-olio annetuilla parametreilla.

Koealan tiedot haetaan klikkaamalla "Näytä koealan tiedot". Tapahtumakäsittelijä kutsuu PlotService-luokasta keskitunnukset 
laskevia metodeja. Metodit kutsuvat PlotRepositorysta listan kyseisen  puista, ja laskevat listalta keskitunnukset, jotka 
palautetaan käyttöliittymälle näytettäväksi.
