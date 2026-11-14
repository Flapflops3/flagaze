# FlaGaze

[中文](README.md)

Units and orientation can be more error-prone than the equations themselves. FlaGaze expresses the relationships between physical dimensions, camera offsets and screen pixels as independent functions, then explores spatial point distributions with clustering. The aim is to make each calculation inspectable and composable, with repeatable synthetic examples.

### Two paths through the code

**Coordinates:** supply 2D points, identify their units, choose a screen orientation, and convert using physical and pixel dimensions. Landscape orientations swap the width/height scales; camera mapping also applies positional offsets.

**Clustering:** generate three groups with a fixed seed, run DBSCAN, identify clusters and noise, calculate a silhouette score where valid, then save a plot, point table and summary. A single cluster or all-noise result returns no silhouette score.

- `gaze/coordinates.py` provides `cm_to_pixels`, `pixels_to_cm` and `camera_to_screen`, including input-shape and dimension checks.
- `gaze/clusters.py` exposes `cluster_points`, returning labels and an optional silhouette score.
- `gaze/demo.py` generates 180 synthetic points and writes CSV, JSON and PNG outputs.
- `tests/test_gaze.py` covers round trips in four orientations, a known offset calculation and clustering edge cases.

With Python 3.12:

```sh
python -m pip install -r requirements.txt
python -m gaze.demo
python -m unittest discover -s tests -v
```

Open `results/gaze/clusters.png` for the visualization. `summary.json` records point count, cluster count and silhouette score. The example uses synthetic points in arbitrary units. This project performs coordinate and clustering calculations; it does not estimate gaze from camera images.
