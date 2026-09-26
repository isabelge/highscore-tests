## Installation
 
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e .
```
 
## Running the server
 
```bash
python main.py
```

## Beispiele
 
```bash
curl -X POST http://127.0.0.1:8000/api/highscores \
  -H "Content-Type: application/json" \
  -d '{"name": "Isabel", "score": 1200, "modus": "pro"}'
 
curl "http://127.0.0.1:8000/api/highscores?modus=pro"
```


## Aufgabenstellung

### Teil 1: Code lesen und API testen

Installiert alle Dependencies und startet das Programm. Der Server läuft, wenn im Terminal eine Meldung wie `Uvicorn running on http://127.0.0.1:8000` erscheint.


Öffnet danach im Browser http://127.0.0.1:8000/docs. 
Hier kann die API direkt ausprobiert werden.

### Ausprobieren

- Welche Endpunkte gibt es und was machen sie?
- Ruft `GET /api/highscores` auf, was wird zurückgegeben, wenn noch nichts gespeichert wurde?
- Speichert vier verschiedene Einträge mit `POST` und ruft `GET` erneut auf. In welcher Reihenfolge werden die Einträge zurückgegeben?
- Probiert diese Abfragen aus:

| Abfrage | Statuscode | Antwort (Kurzfassung) |
|---|---|---|
| `?modus=pro` | | |
| `?modus=PRO` | | |
| `?modus=xyz` | | |

- Testet mit fehlerhaften `POST`-Anfragen:

| Eingabe | Statuscode | Fehlermeldung |
|---|---|---|
| `name` = `""` (leer) | | |
| `name` mit 13 Zeichen | | |
| `name` = `"Müller"` | | |
| `score` = `-1` | | |
| `score` = `"100"` (als Text) | | |
| `score` = `true` | | |
| `modus` = `"xyz"` | | |
| `name` fehlt ganz | | |

- Speichert mehr als 10 Einträge. Was passiert? 
- Stoppt den Server und startet ihn wieder neu und ruft `GET` auf. Was passiert? 

### Ausprobieren

- Was macht `normalisiere`? Warum wirft die Funktion einmal einen `TypeError` und einmal einen `ValueError`?
- In `speichere` steht `isinstance(score, bool) or not isinstance(score, int)`. Warum reicht `not isinstance(score, int)` nicht? (Tipp: Probiert `isinstance(True, int)` in der Python-Konsole aus.)
- Wozu dienen in `topten` die Teile `reverse=True` und `[:LEADERBOARD_SIZE]`?
- Was bedeuten die Statuscodes `201` und `422`?
- Wo werden die Highscores gespeichert? Welche Folgen hat das?

### Besprechung

- Besprecht die Antworten zu dritt.
- Markiert Punkte, bei denen ihr euch uneinig seid.
- Woher wisst ihr, was "richtig" ist und was "falsch"?


## Teil 2: Anforderungen und Tests

- Lest die Anforderungen durch, werden die Punkte, bei denen ihr euch uneinig wart, beantwortet?
- Verteilt die Anforderungen auf die Personen.

- Plant die Tests, bevor ihr diese schreibt.
  - mindestens ein gültiger Fall (Normalfall, muss klappen)
  - mindestens ein ungültiger Fall (muss abgelehnt werden oder ein anderes Ergebnis liefern)
  - die Grenzwerte, also die Werte direkt an der Grenze

Beispiel für ANF-02 (Namenslänge):

| Testfall | Anf. | Eingabe | Erwartet |
|---|---|---|---|
| 1 | ANF-02 | `name` = `"A"` (1 Zeichen) | `201` |
| 2 | ANF-02 | `name` = `"aaaaaaaaaaaa"` (12 Zeichen) | `201` |
| 3 | ANF-02 | `name` = `""` (0 Zeichen) | `422` |
| 4 | ANF-02 | `name` = 13 Zeichen | `422` |


Schreibe die Tests anhand der zuvor definierten Testfälle.

- Sind alle Tests grün? Gibt es rote Tests? Ist der Test falsch oder ist der Code falsch?