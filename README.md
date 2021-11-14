# Avvio
## Linux/UNIX

Avviare direttamente tramite
`python3 calcolo_tasse.py`

O, in alternativam, rendere il file eseguibile con
`sudo chmod +x calcolo_tasse.py`
e poi eseguirlo con
`./calcolo_tasse.py`

## Windows
Avviare lo script da terminale invocando l'interprete Python


# Funzionamento
All'avvio lo script chiederà, in ordine:
<li>importo lordo</li>
<li>Coefficiente di redditività</li>
<li>Aliquota</li>

Una volta inseriti i valori verranno restituiti:
<li>Importo imponibile</li>
<li>Contributi INPS</li>
<li>Imposta</li>
<li>Netto</li>

# Lo script è valido solo per il regime forfettario, non applicate i suoi calcoli se non aderite a questo tipo di regime fiscale!: