# Wellbore geology modeling workflow

**Focus:** applied prediction, grouped validation, and data-coverage diagnostics.

This project explores predicting geological formation information from horizontal-well and typewell data. The local CSRE implementation combines typewell alignment and feature construction with a five-fold, well-grouped modeling workflow. It includes LightGBM and optional CatBoost/Optuna components, plus diagnostic controls that can be run without changing the scoring path.

## What I built and examined

- Python tooling for typewell correspondence, feature generation, model fitting, and prediction.
- A training-coverage table with **57 typewell rows covering 773 wells** in the saved local record.
- Separate diagnostic controls intended to expose behavior of experimental components while preserving the established scoring path.

The project folder also contains a reference notebook credited to Georgy Mamarin. That reference work is not claimed as original CSRE work here.

## Evidence and limits

Saved notebooks contain five-fold error metrics, but several later versions preserve identical output lines. The local evidence review found that **ten notebook variants share the same saved RMSE sequence**. This shows that a modeling workflow and results were recorded; it does not establish that each code revision was independently rerun or improved held-out performance. I have not rerun the competition workflow for this public case study, and I am not claiming a competition rank or production accuracy.

The next useful verification would be a clean run of a selected source revision with recorded data version, group splits, environment, and output provenance.

## Skills demonstrated

- Python data processing and predictive-model experimentation
- Grouped cross-validation and coverage analysis
- Careful separation of saved results from verified improvements

The full code and competition data remain local while attribution and release boundaries are reviewed.

[Back to portfolio](../README.md)
