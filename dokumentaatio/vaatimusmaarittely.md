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

Sovelluksessa on vain yksi käyttäjärooli, normaali käyttäjä.

## Käyttöliittymäluonnos

![Käyttöliittymä](https://github.com/annis1234/TapionTaskulaskin/blob/main/dokumentaatio/kuvat/kayttoliittyma.jpeg)

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ja salasanan
  - Salasanan on oltava vähintään 6 merkkiä pitkä ja sen tulee sisältää:
    - iso kirjain
    - pieni kirjain
    - numero
    - erikoismerkki

### Kirjautumisen jälkeen

- Käyttäjä näkee listauksen tallennetuista koealoista
- Käyttäjä pystyy lisäämään uuden koealan tai poistamaan olemassaolevan koealan
- Käyttäjä pystyy tallentamaan koealalle puita
- Käyttäjä pystyy tyhjentämään koealan
- Käyttäjä näkee tulosteen koealan puista lasketuista keskitunnuksista
- Käyttäjä näkee pistekaavion puuston pituus-läpimitta-relaatioista 
- Käyttäjä pystyy siirtymään koealan tiedoista takaisin koealalistaukseen, 
ja luomaan/valitsemaan toisen koealan
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

- Kirjaamisen nopeuttamiseksi puulajien kirjaaminen numerokoodeilla (1=mänty, 2=kuusi, 3=rauduskoivu...) 
- Tallennettavien puutunnusten lisääminen (esim. ikä, latvusrajan korkeus, 
20 metrin läpimitta, kasvutunnukset) 
- Laskettavien puustotunnusten lisääminen (esim. keski-ikä, runkoluku, puulajisuhteet)
- Tilavuusestimaattien tarkentaminen käyttämällä puulajikohtaisia tilavuusyhtälöitä
- Koealaa kuvaavien tunnusten lisääminen (esim. kasvupaikka, kivisyys, 
kunttaisuus, metsätuhot)
- Yksittäisten puiden hakeminen id-numerolla ja tunnusten 
laskeminen yksittäisistä puista
- Muiden kuin standardikokoisten koealojen tallentaminen, jolloin hehtaarikohtaisen
keskitilavuuden muuntamiseksi määritetään koealakohtainen muuntokerroin
- Koordinaattien lisääminen koealoille/mitattuihin puihin
- Tarkastelutason laajentaminen: koealat kuuluvat metsikkökuviolle, ja kuviot muodostavat metsän. Koealamittausten perusteella voidaan estimoida 
metsikkötason tunnuksia.
