classDiagram
    Pelilauta "1" -- "2..8"Pelaaja
    Pelaaja "1" ..> "2" Noppa
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "2..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Ruutu --|> Vankila
    Ruutu --|> Aloitusruutu
    Ruutu --|> SattumaJaYhteismaa
    Ruutu --|> AsematJaLaitokset
    Ruutu --|> Kadut 
    Aloitusruutu "1" -- "1" Pelilauta
    Vankila "1" -- "1" Pelilauta
    SattumaJaYhteismaa "1" -- "1" Kortti
    Kadut "1" -- "0..1" Hotelli
    Kadut "1" -- "0..4"Talo
    Hotelli "*" -- "1" Pelaaja
    Talo "*" -- "1" Pelaaja

    class Kadut {
        +String nimi
        +toiminto()
    }
    class Vankila{
        +toiminto()
    }
    class Aloitusruutu{
        +toiminto()
    }
    class AsematJaLaitokset{
        +toiminto()
    }
    class SattumaJaYhteismaa{
        +toiminto()
    }
    class Kortti{
        +toiminto()
    }
