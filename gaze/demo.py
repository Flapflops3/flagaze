"""Generate a synthetic trajectory; no recorded observations are used."""
import argparse,json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .clusters import cluster_points
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='results/gaze');args=parser.parse_args()
    dest=Path(args.output);dest.mkdir(parents=True,exist_ok=True)
    rng=np.random.default_rng(42)
    points=np.vstack([rng.normal(center,.08,(60,2)) for center in [(.3,.4),(.8,.7),(1.3,.3)]])
    labels,score=cluster_points(points)
    np.savetxt(dest/'synthetic_points.csv',points,delimiter=',',header='x,y',comments='')
    fig,ax=plt.subplots();ax.scatter(*points.T,c=labels,cmap='viridis',s=15);ax.set(xlabel='x (arbitrary units)',ylabel='y (arbitrary units)',title='Synthetic points - DBSCAN')
    fig.savefig(dest/'clusters.png');plt.close(fig)
    summary={'source':'synthetic generator; not participant data','points':len(points),'clusters':len(set(labels)-{-1}),'silhouette':score}
    (dest/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary))
if __name__=='__main__':main()
