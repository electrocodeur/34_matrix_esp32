from machine import Pin
import time

# Configuration des broches GPIO
rows = [Pin(15, Pin.OUT), Pin(2, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT), Pin(21, Pin.OUT), Pin(22, Pin.OUT)]  #pour les lignes
cols = [Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(27, Pin.OUT), Pin(26, Pin.OUT), Pin(25, Pin.OUT), Pin(33, Pin.OUT), Pin(32, Pin.OUT)]  #pour les colonnes
#cablage
"""ESP32 GPIO  |  Matrice LED 788BS
------------|-------------------
GPIO 15     |  Ligne 1 (Anode)
GPIO 2      |  Ligne 2 (Anode)
GPIO 4      |  Ligne 3 (Anode)
GPIO 5      |  Ligne 4 (Anode)
GPIO 18     |  Ligne 5 (Anode)
GPIO 19     |  Ligne 6 (Anode)
GPIO 21     |  Ligne 7 (Anode)
GPIO 22     |  Ligne 8 (Anode)
GPIO 13     |  Colonne 1 (Cathode)
GPIO 12     |  Colonne 2 (Cathode)
GPIO 14     |  Colonne 3 (Cathode)
GPIO 27     |  Colonne 4 (Cathode)
GPIO 26     |  Colonne 5 (Cathode)
GPIO 25     |  Colonne 6 (Cathode)
GPIO 33     |  Colonne 7 (Cathode)
GPIO 32     |  Colonne 8 (Cathode)"""


# Fonction pour initialiser la matrice
def init_matrix():
    for row in rows:
        row.off()
    for col in cols:
        col.on()

# Fonction pour afficher un motif sur la matrice LED
def display_pattern(pattern):
    for row_idx, row_val in enumerate(pattern):
        for col_idx in range(8):
            cols[col_idx].value((row_val >> col_idx) & 1)
        rows[row_idx].on()
        time.sleep(0.001)
        rows[row_idx].off()

# Exemple de motif (8x8)
pattern = [
    0b11111111,
    0b10000001,
    0b10111101,
    0b10100101,
    0b10111101,
    0b10000001,
    0b11111111,
    0b00000000
]
a = [
    0b00000000,
    0b00111100,
    0b01000010,
    0b01000010,
    0b01111110,
    0b01000010,
    0b01000010,
    0b01000010
]
h = [
    0b10111101,
    0b10111101,
    0b10111101,
    0b10000001,
    0b10000001,
    0b10111101,
    0b10111101,
    0b10111101
]
huit = [
    0b11111111,
    0b10000001,
    0b10111101,
    0b10111101,
    0b10000001,
    0b10111101,
    0b10111101,
    0b10000001
]
# Initialisation de la matrice
init_matrix()

# Boucle principale
while True:
    display_pattern(huit)
