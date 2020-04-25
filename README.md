# Alga 2 második ZH solver algoritmusok a geometriai részhez

### Futtatáshoz kellék:
* python 3.6+
* numpy

### Működés:
* Parancssorban adhatók paraméterek:
  * Első paraméter:
    * `f`: forgásirány számítás (az értéket adja vissza), 3 pontot kér
    * `m`: metsző szakaszpárok: 4 forgásirány értékét adja vissza (ABC, ABD, CDA, CDB) , 4 pontot kér
    * `p`: Polárszög szerinti rendezés, 8 pontot kér
    * `g`: Graham pásztázás, 8 pontot kér
    * `j`: Jarvis menetelés, 8 pontot kér
  * Második paramétertől:
    * A pontok koordinátái space-el elválasztva
    * Pl.: A(1,2) B(3,4) C(6.3 -0.7) esetén `1 2 3 4 6.3 -0.7`
* Példa:
  * `>./geom_alga.py f 2 4 -2 0 9 2`
  * `36.00`
