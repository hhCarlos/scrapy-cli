# 🧾 Development Log — scrapy-cli

## 🏷️ Flags and Descriptions

Each entry must include at least one flag and a concise description of the change.

| Flag | Description |
|------|--------------|
| **feature** | Added a new functionality or module. |
| **fix** | Corrected a bug, error, or invalid parameter. |
| **refactor** | Rebuilt or reorganized existing code without changing behavior. |
| **update** | Modified global values, configs, or minor non-breaking changes. |
| **docs** | Updated or created documentation (README, Log, etc). |
| **ci** | Changes related to pipelines, workflows, or automation. |

---

### 💡 Notes
- Keep each log concise and action-oriented.  
- Use present tense (e.g., *Add*, *Fix*, *Refactor*) for consistency.  
- Prefer multiple small entries per day instead of one large summary.  
- Each task must be developed in its own branch — multiple branches mean multiple jobs.  
- Not all branches need to be uploaded to the remote repository.

---

## 📅 2025-10-27 — `branch: develop`

- **docs:** Created `Log.md` and established development logging format.  
- **feature:** Initial project setup (`main.py`, linter, structure).  
- **ci:** Added `.flake8` configuration and local testing.  
- **update:** Connected GitHub repo and created `develop` branch.

## 📅 2025-10-27 — `branch: ci/workflows`

- **feature:** Pytest and linter added as well in the pipeline.  
- **ci:** Added `pytest` and configuration per document in /workflows.

## 📅 2025-10-27 — `branch: feat/valid-url-request`

- **feature:** Ask the user in terminal for the URL and validate it.  

## 📅 2025-10-27 — `branch: ci/workflows`

- **ci:** Added `pytest` configuration to clean __pycache__.

## 📅 2025-10-27 — `branch: feat/scrapper-class-and-implementation`

- **feature:** Scraper was change to a class and changes in main to call Scraper as a class.  

## 📅 2025-11-4 — `branch: feat/scrapper-request`

- **feature:** Libraries added pip install requests beautifulsoup4 in order to make the request and look for selectors added.

## 📅 2025-11-4 — `branch: feat/flujo-app-salida-y-browser`

- **feature:** we added two options to main menu, the app knows has three options:
1 Look for elements CLI -> Fast and easy for quick checks
2 Look for elements browser -> Interactive work with browser
3 Exit app
