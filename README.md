# FlaGaze

[English](README.en.md)

坐标计算里，单位和方向往往比公式更容易出错。FlaGaze 把物理尺寸、摄像头偏移和屏幕像素之间的关系写成独立函数，再用聚类观察点在平面上的分布。项目目标是让转换关系可检查、可组合，并通过可重复的合成示例解释计算结果。

### 两条计算路径

**坐标路径：** 输入二维点 → 确认毫米、厘米或像素单位 → 选择屏幕方向 → 根据物理尺寸和像素尺寸换算。横屏时交换宽高尺度，摄像头映射再结合偏移量计算屏幕位置。

**聚类路径：** 固定种子生成三组点 → 执行 DBSCAN → 标记簇和噪声 → 在有效簇上计算轮廓系数 → 保存散点图、点表和摘要。单簇或全噪声时不计算没有意义的轮廓系数。

### 从哪里读代码

- `gaze/coordinates.py`：`cm_to_pixels`、`pixels_to_cm` 和 `camera_to_screen`，负责单位、方向与偏移计算，并检查输入形状和尺寸。
- `gaze/clusters.py`：`cluster_points` 返回聚类标签和可选的轮廓系数。
- `gaze/demo.py`：生成 180 个合成点，输出 CSV、JSON 和 PNG。
- `tests/test_gaze.py`：验证四种方向的往返转换、已知偏移公式，以及单簇和双簇边界情况。

Python 3.12：

```sh
python -m pip install -r requirements.txt
python -m gaze.demo
python -m unittest discover -s tests -v
```

打开 `results/gaze/clusters.png` 看聚类结果，`summary.json` 记录点数、簇数与轮廓系数。示例使用任意单位的合成点；模块提供的是坐标与聚类运算，不负责从摄像头图像估计视线。
