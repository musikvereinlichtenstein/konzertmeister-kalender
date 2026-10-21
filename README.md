# Konzertmeister Kalender-Aggregator

1. GitHub-Repository erstellen und diese Dateien hochladen (auch `.github/workflows/calendar.yml`).
2. Unter Settings > Secrets and variables > Actions ein Repository Secret `ICAL_URLS` erstellen. Als Wert die 9 vollständigen Konzertmeister-iCal-URLs, **jeweils eine pro Zeile**, eintragen.
3. Settings > Pages > Build and deployment > Source: **GitHub Actions** wählen.
4. Actions > Kalender zusammenfuehren > Run workflow ausführen.
5. Die URL lautet `https://BENUTZERNAME.github.io/REPOSITORY/raumbelegung.ics`.

Die Datei wird etwa alle 30 Minuten neu erstellt. GitHub kann zeitgesteuerte Ausführungen verzögern. Bei einem Abruffehler wird nicht neu veröffentlicht; die bisherige Pages-Datei bleibt bestehen.

**Datenschutz:** GitHub Pages ist öffentlich erreichbar, auch bei privaten Repositories. Wer die Kalender-URL kennt, kann die Termine lesen. Nur dafür freigegebene Daten veröffentlichen. Quell-URLs geheim halten.
