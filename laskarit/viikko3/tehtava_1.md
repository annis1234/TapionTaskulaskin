classDiagram
    Pelilauta "1" -- "2..8"Pelaaja
    Pelaaja "1" ..> "2" Noppa
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "2..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja 
