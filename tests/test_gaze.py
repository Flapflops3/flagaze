import unittest
import numpy as np
from gaze.coordinates import cm_to_pixels,pixels_to_cm,camera_to_screen
from gaze.clusters import cluster_points
class GazeTests(unittest.TestCase):
    def test_round_trip_all_orientations(self):
        points=np.array([[1.,2.],[-3.,4.]])
        for orientation in range(1,5):
            px=cm_to_pixels(points,(60,100),(720,1280),orientation)
            np.testing.assert_allclose(pixels_to_cm(px,(60,100),(720,1280),orientation),points)
    def test_camera_formula(self):
        np.testing.assert_allclose(camera_to_screen([[0,0]],(60,100),(5,8),(600,1000),1),[[50,-80]])
    def test_invalid_orientation(self):
        with self.assertRaises(ValueError):cm_to_pixels([[0,0]],(60,100),(720,1280),0)
    def test_single_cluster_has_no_silhouette(self):
        labels,score=cluster_points([[0,0],[0,0],[0,0]],eps=1,min_samples=2)
        self.assertIsNone(score)
    def test_two_clusters(self):
        labels,score=cluster_points([[0,0],[.01,0],[0,.01],[5,5],[5.01,5],[5,5.01]],eps=.1,min_samples=2)
        self.assertEqual(len(set(labels)),2)
        self.assertGreater(score,.9)
