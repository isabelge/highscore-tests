## Einträge speichern (`POST /api/highscores`)

| Nr. | Anforderung |
|---|---|
| **ANF-01** | Ein gültiger Eintrag (`name`, `score`, `modus`) muss gespeichert werden. Die Antwort hat den Statuscode `201` und enthält den gespeicherten Eintrag mit den Feldern `name`, `score` und `modus`. |
| **ANF-02** | Der `name` muss ein Text mit 1 bis 12 Zeichen** sein. |
| **ANF-03** | Der `name` muss ausschliesslich aus den Buchstaben `A–Z`, `a–z` und den Ziffern `0–9` bestehen. Leerzeichen, Sonderzeichen und Umlaute sind nicht erlaubt. |
| **ANF-04** | Der `score` muss eine ganze Zahl von 0 oder grösser** sein. Kein Text, keine Dezimalzahl und kein Wahrheitswert (`true`/`false`). |
| **ANF-05** | Der `modus` muss einer der Werte `classic`, `medium` oder `pro` sein. Gross-/Kleinschreibung spielt keine Rolle. Gespeichert und in der Antwort zurückgegeben wird er in Kleinbuchstaben. |
| **ANF-06** | Alle drei Felder sind Pflicht. Fehlt eines, wird der Eintrag abgelehnt. |
| **ANF-07** | Bei ungültiger Eingabe muss die API mit dem Statuscode `422` antworten. Die Antwort enthält im Feld `detail` eine nicht leere Fehlermeldung. Der Eintrag wird nicht gespeichert. |

## Rangliste abfragen (`GET /api/highscores`)

| Nr.        | Anforderung                                                                                                                                                                                                                                                                                    |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ANF-10** | Die Antwort hat den Statuscode `200` und enthält die Felder `highscore` (Liste von Einträgen) und `hinweis` (Text).                                                                                                                                                                            |
| **ANF-11** | Die Einträge in `highscore` müssen nach `score` absteigend sortiert sein (bester zuerst).                                                                                                                                                                                                      |
| **ANF-12** | `highscore` enthält höchstens 10 Einträge, und zwar die 10 besten.                                                                                                                                                                                                                             |
| **ANF-13** | Bei gleichem Score steht der Eintrag, der früher gespeichert wurde, weiter oben.                                                                                                                                                                                                               |
| **ANF-14** | Ein unbekannter `modus` muss mit dem Statuscode `422` und einer Fehlermeldung in `detail` abgelehnt werden.                                                                                                                                                                                    |
| **ANF-15** | Eine Abfrage darf die gespeicherten Daten nicht verändern. Zweimal dieselbe Abfrage ergibt dasselbe Ergebnis.                                                                                                                                                                                  |

## Einschränkungen

| Nr. | Anforderung |
|---|---|
| **ANF-20** | Die Einträge werden nur im Arbeitsspeicher gehalten. Nach einem Neustart des Servers ist die Rangliste leer. |

