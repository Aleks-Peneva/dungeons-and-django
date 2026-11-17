# Dungeons and Django — a West Marches D&D 5e Campaign Manager for Dungeon Masters

A Django web application built for Dungeon Masters running **West Marches** style Dungeons & Dragons 5th Edition campaigns. Because West Marches campaigns rely on a large, rotating roster of adventurers rather than a fixed weekly party, **The Guild Ledger** centralises character dossiers, equipment satchels, magic item attunement rules, and open frontier quests—all accessible directly through the public web interface with the Django admin panel disabled.

---

## Project Architecture

The application is built with **Django** and organised into **three cohesive apps** following Object-Oriented Programming (OOP) and loose-coupling principles:

1. **`campaign_manager`**: Site-wide orchestration layer providing the Guildhall dashboard (`/`), the West Marches Charter rules overview (`/rules/`), shared custom template tags and filters (`campaign_manager/templatetags/guild_extras.py`), and the custom 404 preview route (`/404-preview/`).
2. **`character`**: Manages `PlayerCharacter` dossiers and `InventoryItem` satchels (Many-to-One relationship). Enforces D&D 5e rules including official class choices, level boundaries (`1–20`), attunement eligibility (`requires_attunement`), and the maximum 3-item magic attunement limit.
3. **`quest`**: Manages the Tavern Quest Board (`Quest` model), featuring a Many-to-Many relationship linking quests to `involved_characters`, status and recommended-level filtering/sorting, and private Dungeon Master secret notes.

---

## Key Features & Technical Highlights

- **Full Front-End CRUD (Admin Disabled)**: Complete Create, Read, Update, and Delete workflows with confirmation pages are provided for `PlayerCharacter`, `InventoryItem`, and `Quest` directly from the navigation bar and clearly labelled **Edit** / **Delete** action buttons. `django.contrib.admin` is disabled to ensure zero admin panel dependency.
- **Empty Database Ready**: Runs out of the box on an empty SQLite database (`db.sqlite3`) and displays clear empty-state prompts and quick-create buttons without relying on fixtures or custom migrations.
- **No Authentication Required**: Publicly accessible with zero login or user registration barriers.
- **Form & Model Validations**:
  - **4 Custom `ModelForm` Classes**: `CharacterCreateForm`, `CharacterUpdateForm`, `InventoryItemForm`, and `QuestForm` with tailored labels, placeholders, help text, and error messages.
  - **Disabled Field**: `CharacterUpdateForm` locks the character's `name` (`disabled=True`) once inscribed in the ledger.
  - **Cross-Field & Model Rules (`clean()`)**:
    - Prevents marking an item as attuned (`is_attuned=True`) unless `requires_attunement=True` (enforced both on the model/form and via live form checkbox toggling).
    - Blocks equipping more than **3 attuned items** per character (accounting for item quantities).
    - Prevents setting a quest to `In Progress` without assigned characters and blocks assigning fallen adventurers (`alive=False`) to open or active quests.
- **Dynamic Filtering & Sorting**:
  - Filter adventurers by status (`Alive` / `Fallen`) or sort by `Level` and `Name`.
  - Filter the Guild Vault by `Attuned Magic Items Only`.
  - Filter the Quest Board by status (`Open`, `In Progress`, `Completed`, `Failed`) and sort by recommended level.
- **Custom Template Tag & Filter (`campaign_manager/templatetags/guild_extras.py`)**:
  - `level_tier`: Custom filter translating D&D 5e levels (`1–20`) into their official Tier of Play (`Tier 1: Local Heroes` through `Tier 4: Masters of the World`).
  - `guild_summary_counts`: Custom simple tag computing live counts of living heroes, fallen heroes, and open quests.
- **Offline-Ready Local Bootstrap 5 & High-Contrast Palette**: Bundles `bootstrap.min.css` and `bootstrap.bundle.min.js` locally inside `static/` (eliminating external CDN latency) with a high-contrast custom palette (**Slate Blue** `#6969B3` background, **Powder Blue** `#98C1D9` surfaces, **Coffee Bean** `#25171A` body text, **Blackberry Cream** `#4B244A` header links, and **Indigo Velvet** `#533A7B` body links).

---

## Local Installation & Setup

### Prerequisites
- Python 3.10 or higher
- `pip` and `venv`

### Step-by-Step Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create and activate a virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. *(Optional)* **Create a `.env` file from `.env.example`:**
   ```bash
   cp .env.example .env
   ```
   *(If skipped, `settings.py` automatically falls back to safe local defaults and SQLite.)*

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Open the application:**
   Visit `http://127.0.0` in your web browser.

---

## Environment Variables (`.env.example`)

`west_marches_manager/settings.py` automatically loads variables from a root `.env` file via `python-dotenv` while providing built-in defaults so the project starts immediately after cloning. An **`.env.example`** template is included in the repository root:

```env
# Django Core Configuration
SECRET_KEY=replace-with-your-own-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Engine ('sqlite3' by default, or 'postgresql')
DB_ENGINE=sqlite3

# Optional PostgreSQL Settings (Only required if DB_ENGINE=postgresql)
DB_NAME=west_marches_db
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

### Testing the Custom 404 Page Locally
Django serves `templates/404.html` automatically for unknown URLs whenever `DEBUG=False`. To verify it locally:
1. Set `DEBUG=False` in `.env` (or temporarily in `west_marches_manager/settings.py`) and ensure `ALLOWED_HOSTS` includes `127.0.0.1` and `localhost`.
2. Start the server with `--insecure` so local `static/` assets continue loading:
   ```bash
   python manage.py runserver --insecure
   ```
3. Visit `http://127.0.0uncharted-hex/` (or preview `/404-preview/` while `DEBUG=True`).
4. Set `DEBUG=True` back before committing.

---

## Site Navigation Map

All pages are reachable via the top navigation bar, footer, or in-page action buttons:

- **Guildhall (`/`)**: Campaign dashboard displaying live telemetry, active quests, highest-level adventurers with D&D 5e Tiers of Play, and recently acquired loot.
- **Adventurers (`/character/`)**: Character roster with status/level/name filters, character dossiers (`/character/<id>/`), creation (`/character/new/`), editing (`/character/<id>/edit/`), and deletion (`/character/<id>/delete/`).
- **Guild Vault (`/character/items/`)**: Global inventory registry with attunement filtering, item logging (`/character/items/new/`), editing (`/character/items/<id>/edit/`), and deletion (`/character/items/<id>/delete/`).
- **Quest Board (`/quest/`)**: Frontier quest notices with status/level filters, quest notices (`/quest/<id>/`), creation (`/quest/new/`), editing (`/quest/<id>/edit/`), and deletion (`/quest/<id>/delete/`).
- **West Marches Rules (`/rules/`)**: Standing campaign charter and ledger regulations.

## License
MIT © 2026 Aleksandra Peneva