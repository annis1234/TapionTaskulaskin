# Arkkitehtuurikuvaus

## Rakenne

Ohjelma sisältää hakemistot ui, repositories, services ja entities. Hakemisto ui sisältää ohjelman käyttöliittymän koodin ja services sovelluslogiikkaa hoitavan koodin. Hakemiston repositories sisältävä koodi vastaa tiedon tallentamisesta, ja entities sisältää sovelluksen tietokohteita kuvaavat luokat.

Sovelluksen rakenne luokkakaaviona:

![Luokkakaavio](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/sovelluslogiikka.png)

## Käyttöliittymä

Käyttöliittymä sisältää viisi näkymää:

- Sisäänkirjautuminen
- Uuden käyttäjän luominen
- Olemassa olevien koealatiedostojen listaus ja uuden tiedoston luominen
- Puiden lisääminen valittuu koealatiedostoon
- Valitun koealan puustotietojen tarkastelu

Näkymät ovat eriytettyinä omiin luokkiinsa. Luokka UI vastaa näkymien  esittämisestä ja niiden vaihtamisesta. Käyttöliittymän luokat käyttävät 
PlotService-luokan metodeja toiminnallisuuksien toteuttamiseen.

## Sovelluslogiikka

Sovelluslogiikkaa hoitava koodi on ylläolevan luokkakaavion mukaisesti eriytetty kolmeen service-luokkaan. Kaavioon on lisätty esimerkkejä kunkin service-luokan sisältämistä metodeista. UserService huolehtii käyttäjään liittyvistä toiminnallisuuksista, PlotService hoitaa koealatiedostoihin liittyvät toiminnallisuudet ja CalcService vastaa puustotunnuksiin liittyvästä laskennasta. 

Sovelluksen keskeisimmät toiminnallisuudet ovat:

- Käyttäjän luominen
- Sisäänkirjautuminen olemassaolevalla tunnuksella ja salasanalla
- Koealatiedoston luominen
- Puun tallentaminen koealatiedostoon
- Valitun koealan puustotietojen laskeminen 

Sovelluksen keskeiset tietokohteet ovat User ja Tree, jotka vastaavat sovelluksen käyttäjän ja sovelluksen kautta luotujen puiden kuvaamisesta. Tiedostojen käsittelystä vastaavat PlotRepository- ja UserRepository-luokat

## Tiedon pysyväistallennus

Tiedon tallentamisesta vastaavat luokat PlotRepository ja UserRepository.

Puut tallennetaan csv-tiedostoon, jonka nimen käyttäjä määrittelee. Tiedosto tallennetaan erillisessä konfiguraatiotiedostossa määritellyn polun mukaisesti data/plots-hakemistoon.

Käyttäjän tallentamiseen käytetään SQLite-tietokantaa, joka alustetaan initialize_database.py-tiedostossa.

## Päätoiminnallisuudet

Koska keskeisimmät toiminnallisuudet liittyvät koealojen luomiseen ja käsittelyyn, kirjautuminen ja käyttäjätietojen käsittely on jätetty tästä osiosta pois. Toimintalogiikka on kuitenkin samankaltainen: käyttäjä valitsee haluamansa toiminnon käyttöliittymän kautta. Käyttöliittymän tapahtumakäsittelijä kutsuu UserService-luokan metodeja, jotka kutsuvat tarvittaessa metodeja UserRepository-luokasta.

### Koealantiedoston luominen ja valitseminen

![Sekvenssikaavio1](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/sekvenssikaavio_2.png)

Koealan luomisnäkymässä kirjoitetaan koealan nimi ja klikataan "Luo koeala". Tapahtumankäsittelijä kutsuu luokan PlotService 
metodia create_plot parametrinaan käyttäjän antama koealan nimi. PlotService puolestaan kutsuu PlotRepository-luokan metodia 
create_plot (parametrina edelleen koelana nimi), joka luo csv-tiedoston annetulla nimellä. Koealan valitseminen tapahtuu samalla 
periaatteella, paitsi tiedoston luomisen sijasta PlotRepository-luokan metodi select_plot asettaa sille parametrina annetun 
tiedoston nimen polkuun. UI päivittää näkymäänsä lisätyn koealatiedoston nimen. Koealatiedostojen nimet haetaan listana PlotService-luokan kautta PlotRepository-luokasta.

### Puun lisääminen koealalle ja koealan keskitunnusten tarkastelu

![Sekvenssikaavio2](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/sekvenssikaavio.png)

Puun lisääminen tapahtuu kirjoittamalla puutunnukset ja klikkaamalla "Lisää puu". Tapahtumakäsittelijä kutsuu luokkaa Tree, 
jossa luodaan Tree-olio annetuilla parametreilla.

Koealan tietoja tarkastellaan klikkaamalla "Näytä koealan tiedot", jolloin näkymä vaihtuu koealan tiedot esittävään näkymään. Kuvaaja alustetaan Charts-luokassa, joka kutsuu CalcService-luokan return_h()- ja return_d()-metodeja. CalcService palauttaa pituudet ja läpimitat listoina, joiden avulla kuvaaja piirretään. Selkeyden vuoksi kuvaajassa on esitetty vain pituuksien hakeminen.

Kuvaajan lisäksi näkymässä esitetään koealan puustotunnukset. Tapahtumakäsittelijä kutsuu CalcService-luokasta keskitunnukset 
laskevia metodeja. Metodit kutsuvat PlotRepositorysta listan kyseisen koealatiedoston puista, ja laskevat listalta halutut keskitunnukset, jotka 
palautetaan käyttöliittymälle näytettäväksi. Selkeyden vuoksi tapahtumien kulku on esitetty kuvaajassa vain pääpuulajin osalta, mutta muiden puutunnusten kohdalla logiikka on sama.
