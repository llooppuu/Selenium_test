# Testimisplaan

## Eesmärk

Kontrollida, et Seleniumi skriptid avavad õiged veebilehed,
leiavad vajalikud elemendid ning sooritavad ettenähtud tegevused.

| Test | Tegevus | Oodatud tulemus |
|---|---|---|
| 1. Google'i otsing | Ava Google, sisesta otsingupäring ja käivita otsing | Avaneb Google'i tulemuste leht |
| 2. Screenshot | Käivita `task1_google_search.py` | Tekib fail `screenshots/minu_otsing.png` |
| 3. Tsitaadid | Käivita `task2_quotes.py` | Terminalis kuvatakse tsitaadid koos autoritega |
| 4. Add/Remove Elements | Lisa 5 elementi ja kustuta need | Alguses tekib 5 Delete nuppu ning lõpuks 0 |
| 5. Login | Logi sisse testkasutajaga | Terminalis kuvatakse `TEST ÕNNESTUS` |
| 6. Checkboxes | Ava Checkboxes, märgi mõlemad ja mine tagasi | Mõlemad kastid märgitakse ning brauser liigub tagasi avalehele |

## Testkeskkond

- Windows
- Python 3
- Google Chrome
- Selenium 4

## Võimalikud probleemid

- Google võib näidata küpsiste kinnitamise akent.
- Google võib automatiseeritud brauseri puhul kuvada CAPTCHA.
- Veebilehe aeglase laadimise korral võib olla vaja suurendada `time.sleep()` aega.
- Chrome ja ChromeDriver peavad omavahel sobima, kui draiverit hallatakse käsitsi.
