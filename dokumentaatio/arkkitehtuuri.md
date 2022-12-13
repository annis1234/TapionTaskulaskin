# Arkkitehtuurikuvaus

## Rakenne

![Luokkakaavio](https://github.com/annis1234/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/luokkakaavio.png)

## Käyttöliittymä

Käyttöliittymä sisältää viisi näkymää:

- Sisäänkirjautuminen
- Uuden käyttäjän luominen
- Koealalistaus ja koealan lisääminen
- Puiden lisääminen koealalle
- Koealan tietojen katselu

Näkymät ovat eriytettyinä omiin luokkiinsa. Luokka UI vastaa näkymien 
esittämisestä ja niiden vaihtamisesta. Käyttöliittymän luokat käyttävät 
PlotService-luokan metodeja toiminnallisuuksien toteuttamiseen.

## Sovelluslogiikka

Sovelluksen keskeiset luokat ovat User ja Tree, jotka vastaavat sovelluksen käyttäjän ja sovelluksen kautta luotujen puiden
kuvaamisesta.

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
