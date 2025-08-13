# 🌌 Pallas Archive – Automated CSV to Chart

> _Turning your raw CSV data into **beautiful charts** without lifting a finger... well, except to click “Push”._

This repository contains a **Python script** that processes CSV files and automatically generates charts/images using **GitHub Actions**.  
Just drop your data in, push it to GitHub, and **watch the magic happen** ✨.

---

## 🚀 How It Works
1. **📂 Drop Your CSV** – Put your CSV file inside the `/data` folder.  
2. **⬆ Push to GitHub** – Commit and push the changes.  
3. **🤖 Automated Run** – GitHub Actions runs the Python script for you.  
4. **📥 Download Results** – Your shiny new charts will be ready as downloadable artifacts.

---

## 🛠 How to Trigger the Workflow

You can make the **Python CI** workflow run in three ways:
### 1️⃣ Push to Any Branch
```bash
git add .
git commit -m "Trigger workflow"
git push

