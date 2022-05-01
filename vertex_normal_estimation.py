import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("/home/myoujin/open3d_practice/pcd_data/bunny.ply")
downpcd = pcd.voxel_down_sample(voxel_size=0.01)
downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd])
print("Print a normal vector of the 0th point")
print(downpcd.normals[0])
print("Print the normal vectors of the first 10 points")
print(np.asarray(downpcd.normals)[:10, :1])

