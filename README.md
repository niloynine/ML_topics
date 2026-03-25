# ML Topics Learning Repository

This repository tracks hands-on machine learning practice, notes, and experiments.

## What this repo contains

- Practical Python experiments for core ML concepts
- Jupyter notebooks for end-to-end workflows
- Daily learning notes and reflections
- Reading tracker for ML papers

## Project structure

- `experiments/` - scripts and notebooks for model-building practice
- `notebooks/` - additional notebook work
- `notes/` - daily ML learning notes
- `papers/` - paper reading logs
- `myenv/` - local Python virtual environment (workspace-local)

## Quick start

1. Create and activate a virtual environment (if needed):

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1
```

2. Install common dependencies:

```powershell
pip install numpy pandas scikit-learn matplotlib jupyter ipykernel
```

3. Run a script:

```powershell
python experiments\linear_regression_scratch.py
```

4. Start notebooks:

```powershell
jupyter notebook
```

## Typical workflow

1. Add experiments and notes.
2. Check git status:

```powershell
git status
```

3. Commit and push:

```powershell
git add .
git commit -m "Update experiments and notes"
git push origin main
```

## Notes

- This repository is focused on learning progress and iterative experimentation.
- Notebooks and notes may evolve frequently as concepts are refined.
