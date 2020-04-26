# Alga 2 második ZH solver algoritmusok

### Futtatáshoz kellék:
* python 3.6+
* numpy (https://solarianprogrammer.com/2017/02/25/install-numpy-scipy-matplotlib-python-3-windows/)
* tabulate (`pip install tabulate` - pip verzióra figyelve, lehet pip3 fog kelleni!)

### Működés geom_alga.py:
* Parancssorban adható paraméterek:
  * Első paraméter:
    * `f`: Forgásirány számítás (az értéket adja vissza), 3 pontot kér
    * `m`: Metsző szakaszpárok: 4 forgásirány értékét adja vissza (ABC, ABD, CDA, CDB) , 4 pontot kér
    * `s`: Söprés: Metsző szakaszpárok keresése
      * Ha a szakaszok: AD EB FC GH akkor a pontokat sorban a szakaszok szerint kell beírni, azaz rendre A1 A2 D1 D2 E1 E2 stb
    * `p`: Polárszög szerinti rendezés
    * `g`: Graham pásztázás
    * `j`: Jarvis menetelés
  * Második paramétertől:
    * A pontok koordinátái space-el elválasztva
    * Pl.: A(1,2) B(3,4) C(6.3 -0.7) esetén `1 2 3 4 6.3 -0.7`
* Példa:
  * `>./geom_alga.py f 2 4 -2 0 9 2`
  * `36.00`

### Működés rabin.py:
* Parancssori paraméterek:
  * Első paraméter egy szöveg (esetünkben számjegyekből álló string)
  * Második paraméter a substring amit vizsgálunk (egy másik számjegyekből álló string)
  * Harmadik paraméter a modulus, amivel a hash-t készítjük
* Példa:
  * `>./rabin.py 3613203214 321 11`
  
### Működés kmp.py:
* Parancssori paraméterek:
  * Első paraméter egy string
  * Második paraméter a substring amit vizsgálunk
* Példa:
  * `>./kmp.py aaabaababa aababa`
  
### Működés mod_exp.py:
* Parancssori paraméterek:
  * Első paraméter egy szám: hatványalap
  * Második paraméter is szám: hatvány kitevő
  * Harmadik paraméter is szám: a modulus
* Példa:
  * `>./mod_exp.py 7 13 17`
  
### Működés dfa.py:
* Parancssori paraméterek:
  * Első paraméter egy string
  * Második paraméter a substring amit illesztünk
* Példa:
  * `>./dfa.py abcbaacacabbac acabbac`
