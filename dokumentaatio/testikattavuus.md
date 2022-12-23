## Testausdokumentti

Sovellusta on testattu manuaalisesti järjestelmätasolla sekä unittest-moduulin automaatisoiduilla yksikkö- ja integraatiotason testeillä.

Sovelluslogiikasta vastaavia PlotService- ja CalcService-luokkia on testattu services_test-tiedoston TestPlot-luokassa. UserService on testattu näistä erillään TestUser-luokassa. Service-oliot käyttävät testeissä samoja repository-olioita kuin varsinainen ohjelmakin. Testikäyttäjien tiedot tallennetaan erilliseen testitietokantaan, joka on konfiguroitu .env.test-tiedostossa.

UserRepository- ja PlotRepository-luokat ovat testattu TestUserRepository- ja TestPlotRepository-luokissa. TestUserRepository-luokka käyttää testitietokantaa, ja TestPlotRepository-luokka luo testejä varten erilliset testikoealatiedostot.

### Testauskattavuus

Testauksen haaraumakattavuus on 95 %. Käyttöliittymä on jätetty testauksen ulkopuolelle.

![testikattavuus](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/testikattavuus.png)

Testeissä on käyty läpi kaikki ohjelman keskeisimmät toiminnallisuudet. On myös testattu, että virheelliset syötteet tai kirjautumistiedot tuottavat halutut virheviestit.

Testatut skenaariot ovat tilanteita, joihin voi päätyä, kun sovellusta käytetään graafisen käyttöliittymän kautta. Testaamatta ovat siis jääneet esimerkiksi tilanteet, joissa käyttäjä yrittää käsitellä tiedostoa, jota ei ole olemassa.
