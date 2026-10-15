# Double-slit numerical prototype

**Focus:** simulation, parameter sweeps, calibration, and error analysis.

I built a Python prototype that propagates states on a discrete lattice and projects the resulting detector response into physical coordinates. It models slit and boundary interactions, measurement impedance, and coherence, then writes detector profiles, figures, CSV data, and a JSON run summary. The prototype is an exploration of a proposed model, not an experimentally established account of optics.

## Saved experiment

One local sweep varied measurement strength across **seven settings** with fixed geometry and an explicit wavelength, slit separation, and screen-distance calibration. The saved summary compares measured fringe spacing with a stated reference relation. Across those settings, the reported spacing error ranges from **0.71% to 58.26%**. Reporting the full range matters: one close setting does not make the model accurate across the sweep.

## Evidence and limits

I inspected the simulator source and its saved run summary for this case study; I did not rerun the sweep or independently validate the physics. The comparison is an internal calibration check against a reference spacing relation. It is not a laboratory measurement or evidence that the broader physical theory is correct.

## Skills demonstrated

- Python, NumPy, and Matplotlib for numerical experiments
- Parameter-sweep design and structured result export
- Calibration and explicit reporting of poor as well as close matches

The prototype source and figures are local working artifacts. A public release would need a focused source and artifact review.

[Back to portfolio](../README.md)
