"""DBSCAN exploration without participant files or diagnostic labels."""
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
def cluster_points(points,eps=.2,min_samples=3):
    points=np.asarray(points,dtype=float)
    if points.ndim!=2 or points.shape[1]!=2 or not len(points) or not np.isfinite(points).all():
        raise ValueError('expected a non-empty finite N x 2 array')
    labels=DBSCAN(eps=eps,min_samples=min_samples).fit_predict(points)
    valid=labels!=-1;count=len(set(labels[valid]))
    score=float(silhouette_score(points[valid],labels[valid])) if 1<count<valid.sum() else None
    return labels,score
