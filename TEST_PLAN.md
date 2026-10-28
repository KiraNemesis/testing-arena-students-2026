Einhaltung der Datentypen und Formate (ansonsten Value Error)
- city=String
- time=Int (Minuten seit Mitternacht oder konvertiere "hh:mm" zu Minuten, führende nullen sind optional)
- temp=Float (Celsius)

Valide Städtenamen
- "Köln" == True
- "Kln" == False

Reihenfolge der Eingabe der Argumente muss eingehalten werden
- city, time, temp

Case-Insensitive
- "Köln" == "köln"

Time input muss ein limit haben und darf nicht drüber gehen
- 60*24

parse_measurement(line)
- Eingabe muss ein String sein, ansonsten ValueError
- wird durch ";" getrennt, ansonsten raise error
- führende und nachfolgende Leerzeichen werden beseitigt
- time wird in einen float umgewandelt
