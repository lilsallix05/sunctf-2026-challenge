# SunCTF 2026 challenges

Two CTF challenges I created for **SunCTF 2026**, the on-site Jeopardy CTF run by the Sunway Cybersecurity Club in Malaysia (6 September 2026).

| Challenge | Category | Points | Type | Folder |
| --- | --- | --- | --- | --- |
| [The Eternal Flame](./osint_the-eternal-flame) | OSINT | 100 | Static (one image) | `osint_the-eternal-flame/` |
| [The Gaslit Gallery](./web_gaslit-gallery) | Web | 200 | Dynamic (Flask in Docker) | `web_gaslit-gallery/` |

## The Eternal Flame · OSINT · 100

One photo of a desert crater that has been burning for decades. Find the exact coordinates of its centre.

## The Gaslit Gallery · Web · 200

An "AI-secured" admin portal built to mislead AI-assisted solvers: decoy content in the front end sends a language model down the wrong path, so players have to read the code themselves.

Run it locally (Docker):

```bash
cd web_gaslit-gallery
docker compose up --build -d
# open http://localhost:8080
docker compose down
```

## Spoilers

Each folder has its own README with the full brief, the flag format and a collapsed **Solution** section that includes the flag. Try the challenge first.

## Author

Selbinyyaz (Salli) Odekova · [lilsallix05](https://github.com/lilsallix05) · [Portfolio](https://selbinyyaz-odekova.web.app)
