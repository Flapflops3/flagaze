"""Pure coordinate transforms extracted from the screen-mapping exercises.

Device dimensions and camera offsets use mm; input points use the named units.
No dataset, video, or model is loaded by these functions.
"""
import numpy as np

def _geometry(points,device_mm,screen_px,orientation):
    p=np.asarray(points,dtype=float)
    if p.ndim!=2 or p.shape[1]!=2 or not np.isfinite(p).all():
        raise ValueError('points must be a finite N x 2 array')
    if orientation not in (1,2,3,4):raise ValueError('orientation must be 1, 2, 3 or 4')
    physical=np.asarray(device_mm,dtype=float);screen=np.asarray(screen_px,dtype=float)
    if physical.shape!=(2,) or screen.shape!=(2,) or not np.isfinite([*physical,*screen]).all() or min(*physical,*screen)<=0:
        raise ValueError('device and screen dimensions must be positive finite pairs')
    if orientation in (3,4):physical=physical[::-1]
    return p,screen/physical

def cm_to_pixels(points,device_mm,screen_px,orientation=1):
    p,scale=_geometry(points,device_mm,screen_px,orientation)
    return p*10*scale

def pixels_to_cm(points,device_mm,screen_px,orientation=1):
    p,scale=_geometry(points,device_mm,screen_px,orientation)
    return p/scale/10

def camera_to_screen(points_mm,device_mm,camera_offset_mm,screen_px,orientation=1):
    p,scale=_geometry(points_mm,device_mm,screen_px,orientation)
    x,y=p.T;dx,dy=camera_offset_mm;w,h=device_mm
    if orientation==1:a,b=x+dx,-y-dy
    elif orientation==2:a,b=x-dx+w,-y+dy+h
    elif orientation==3:a,b=x-dy,-y-dx+w
    else:a,b=x+dy+h,-y+dx
    return np.column_stack((a,b))*scale
