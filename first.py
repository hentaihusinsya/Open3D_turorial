import open3d as o3d

if __name__ == "__main__":
    print("Testing IO for point cloud ...")
    pcd = o3d.io.read_point_cloud("pcd_data/person.pcd")
    print(pcd)
    o3d.io.write_point_cloud("copy_os_fragment.pcd", pcd)

    #(2)Mesh
    print("Testing IO for meshes ...")
    mesh = o3d.io.read_triangle_mesh("pcd_data/bunny.ply")
    print(mesh)
    o3d.io.write_triangle_mesh("copy_of_knot.ply", mesh)

    
