import numpy as np
import open3d as o3d

if __name__ == "__main__":
    print("Downsample the point cloud with a voxel of 0.05")
    pcd = o3d.io.read_point_cloud("/home/myoujin/open3d_practice/pcd_data/frag_115.ply")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    o3d.visualization.draw_geometries([downpcd])

