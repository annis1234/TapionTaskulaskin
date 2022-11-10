# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on toimia metsänmittauksen apuvälineenä. 
Sovellukseen tallennetaan koeala, johon lisätään koealalta mitatut 
puut ja niitä kuvaavat tunnukset. Puutunnusten perusteella sovellus laskee 
ja palauttaa koealakohtaisia keskitunnuksia.

Alkuvaiheessa tallennettavat puutunnukset ovat puulaji, pituus ja 
rinnankorkeusläpimitta, ja palautettavat keskitunnukset ovat pääpuulaji, keskipituus 
(m) ja keskitilavuus (m3/ha). Perusversiossa oletuksena on, että 
mitattavat koealat ovat yhden hehtaarin kokoisia.

Metsänmittaaja kirjautuu sovellukseen tunnuksella, ja mitatut koealat 
tallennetaan tunnuksen yhteyteen.

## Käyttäjät

Sovelluksessa on (ainakin alkuvaiheessa) vain yksi käyttäjärooli, normaali 
käyttäjä.

## Käyttöliittymäluonnos

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ja salasanan
  - Salasanan on oltava vähintään 8 merkkiä pitkä ja sen tulee sisältää:
    - iso kirjain
    - pieni kirjain
    - numero
    - erikoismerkki

### Kirjautumisen jälkeen

- Käyttäjä näkee tunnukselleen tallennetut koealat
- Käyttäjä pystyy lisäämään koealan ja tallentamaan koealalle puita
- Käyttäjä näkee tulosteen koealan puista lasketuista keskitunnuksista
- Käyttäjä pystyy siirtymään koealan tiedoista takaisin koealalistaukseen, ja valitsemaan toisen koealan
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

- Tallennettavien puutunnusten lisääminen (esim. ikä, latvusrajan korkeus, 
20 metrin läpimitta) 
- Palautettavien puustotunnusten lisääminen (esim. pohjapinta-ala, 
keski-ikä, runkoluku, puulajisuhteet)
- Koealaa kuvaavien tunnusten lisääminen (esim. kasvupaikka, kivisyys, 
kunttaisuus, metsätuhot)
- Yksittäisten puiden hakeminen ja tarkastelu id-numerolla ja tunnusten 
laskeminen yksittäisistä puista
- Mahdollisuus hakea ja tarkastella toisten mittaamien kuvioiden tietoja
- Muun kuin hehtaarin kokoisten koealojen tallentaminen, jolloin 
keskitilavuus muunnetaan hehtaarikohtaisiksi
- Paikkatiedon lisääminen koealoille/mitattuihin puihin
- Tarkastelutason laajentaminen: koealat kuuluvat metsikkökuviolle, ja kuviot muodostavat metsän
- Nimensä mukaisesti sovellus olisi parhaimmillaan, jos tiedot voisi 
tallentaa suoraan metsässsä, joten jokin mobiilisovellus/verkossa toimiva 
versio sovelluksesta olisi hyödyllinen
