# Kittygram Plus

Extended Django REST Framework API for cats — intermediate learning step between [kittygram](https://github.com/Shipovmax/kittygram) (starter) and [kittygram_backend](https://github.com/Shipovmax/kittygram_backend) (production-ready).

---

## What's added vs starter

- **Owner model** — `first_name`, `last_name`; FK to `Cat`; `OwnerSerializer` with reverse `cats` relation
- **Achievement model** — M2M to `Cat` via `AchievementCat` through-table
- **Color choices** — `Cat.color` restricted to `Gray / Black / White / Ginger / Mixed` via `ChoiceField`
- **Hex2NameColor** — custom serializer field; converts hex color codes to CSS names on write
- **Age field** — computed via `SerializerMethodField`
- **LightCatViewSet** — custom viewset with only `create` + `retrieve` actions via `CreateRetrieveViewSet` mixin composition
- **Djoser JWT auth** — `/auth/jwt/create/`, `/auth/jwt/refresh/`

---

## Tech Stack

| | |
|---|---|
| Framework | Django 3.2, DRF 3.12 |
| Auth | Djoser + JWT |
| Color validation | webcolors |
| Database | SQLite3 |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/kittygram_plus
cd kittygram_plus

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

API at `http://127.0.0.1:8000/`

---

## Endpoints

| Endpoint | ViewSet | Actions |
|----------|---------|---------|
| `/cats/` | `CatViewSet` | Full CRUD |
| `/owners/` | `OwnerViewSet` | Full CRUD |
| `/mycats/` | `LightCatViewSet` | Create + Retrieve only |
| `/auth/jwt/create/` | — | Obtain JWT pair |
| `/auth/jwt/refresh/` | — | Refresh token |

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
