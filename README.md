# Pallas Archive – Automated CSV to Chart

This repository contains a Python script that processes CSV files and automatically generates charts/images using **GitHub Actions**.

When you push a CSV file to this repository, the workflow will run and produce output files that you can download directly from the Actions tab.

---

## How It Works
1. **Place your CSV file** inside the `/data` folder (or update script path if needed).
2. **Push changes** to GitHub.
3. GitHub Actions will:
   - Run the Python script.
   - Generate output charts/images.
   - Save them as downloadable artifacts.

---

## Triggering the Workflow

You can trigger the Python CI workflow in **three ways**:

### 1. Push to Any Branch
Make any change in the repo (e.g., edit `README.md`), commit, and push.

```bash
git add .
git commit -m "Trigger workflow"
git push

