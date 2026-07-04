# 🌌 Meteorite Landing Data Visualizer

Automated pipeline that turns NASA's public meteorite landing dataset into charts, using GitHub Actions to run the analysis on every push.

## What it does
Takes NASA's [Meteorite Landings](https://data.nasa.gov/) CSV data, loads and processes it with pandas, and generates visualizations (via `load_meteorites.py` / `streamlit_app.py`) showing patterns in landing locations, mass distribution, and time trends — no manual chart-building required.

## How it works
1. **Drop a CSV** into the `/data` folder (sample meteorite data included: `meteorites_sample.csv`)
2. **Push to GitHub** — commit and push your changes
3. **GitHub Actions runs automatically** — the workflow executes `load_meteorites.py` on every push
4. **Charts appear as downloadable artifacts** in the Actions run, or live via the Streamlit app

## Run it locally
```bash
git clone https://github.com/pallasArchive/nasa-github-starter.git
cd nasa-github-starter
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Results
*(Add 1-2 screenshots or a sample chart here — this is the single highest-impact thing missing right now. A committee member scanning your repos will judge this in 5 seconds by whether they can see the output without cloning it.)*

## Tech
Python · pandas · Streamlit · GitHub Actions

## License
MIT
