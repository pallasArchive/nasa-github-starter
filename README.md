# NASA GitHub Starter: Meteorite Landings Mini-Project

A beginner-friendly starter repo to practice **Python + GitHub** while working with a NASA dataset (Meteorite Landings). It includes a small sample dataset, a processing script, and a minimal Streamlit app.

---

## What’s inside
- `src/load_meteorites.py` — cleans the dataset and creates a quick summary + chart
- `streamlit_app.py` — tiny dashboard to explore the data locally
- `data/meteorites_sample.csv` — tiny sample so everything works out of the box
- `images/` — charts created by the script land here
- `outputs/` — CSV summaries land here
- `.github/workflows/python.yml` — runs the script in CI on every push
- `.gitignore`, `requirements.txt`, `LICENSE`

---

## Quickstart (local)
1. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the data script (uses the included sample by default)**
   ```bash
   python src/load_meteorites.py --input data/meteorites_sample.csv
   ```

   Outputs:
   - `outputs/summary.csv`
   - `images/mass_vs_year.png`

4. **(Optional) Launch the Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## Use the full NASA dataset
The official dataset is **Meteorite Landings** on data.nasa.gov. Download the CSV and run:
```bash
python src/load_meteorites.py --input /path/to/Meteorite_Landings.csv
```

> Tip: If the CSV uses a `year` column with full timestamps, the script will parse it automatically.


---

## GitHub: First Venture Checklist (do these after downloading this starter)
1. **Create a new repo on GitHub** (name suggestion: `nasa-github-starter`).
2. **Upload the contents** of this folder (or clone + push from your computer).
3. Add a clear **README** (this file) and **License** (MIT included).
4. Create your first **issue**: “Load full NASA dataset + make plot.”
5. Create a **branch**: `feat/full-dataset`.
6. Commit changes (`git add -A && git commit -m "Add full NASA dataset workflow"`), then **open a Pull Request** from your branch.
7. Merge the PR and **close the issue**.
8. Add a **screenshot** of your chart to `/images` and reference it in README using Markdown (see below).
9. Create a **Release** (tag `v0.1.0`).

### Add a chart preview to README
```markdown
## Chart Preview
![Mass vs Year](images/mass_vs_year.png)
```

---

## Project Ideas to Extend
- Add filters for **class**, **mass**, and **decade** in the Streamlit app.
- Compute **top-10 meteorites by mass** and map them by coordinates.
- Publish a short writeup in the README explaining your insights.

---

## License
MIT © 2025 Your Name
