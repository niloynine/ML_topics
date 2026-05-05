# ML Topics Learning Repository

This repository tracks hands-on machine learning practice, notes, and experiments.

Repository: https://github.com/niloynine/ML_topics

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

Or install from a `requirements.txt` file if available:

```powershell
pip install -r requirements.txt
```

3. Run a script:

```powershell
python experiments\linear_regression_scratch.py
```

4. Start notebooks:

```powershell
jupyter notebook
```

How to run a notebook (example):

1. Activate the environment:

```powershell
.\myenv\Scripts\Activate.ps1
```
2. Start Jupyter and open the desired notebook under `experiments/`.

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

## Dataset

The repository expects a local CSV dataset at `data/dataset.csv`. Several notebooks and scripts try multiple candidate paths (e.g., `data/dataset.csv` and `../data/dataset.csv`) — update the path in the notebook or move your dataset into the `data/` folder.

## Contributing

- Add experiments under the `experiments/` folder and notes under `notes/`.
- Open an issue or submit a PR if you'd like to add improvements or sample datasets.

## License

This repo is intended for personal learning. If you want to add a license, create a `LICENSE` file at the project root.
