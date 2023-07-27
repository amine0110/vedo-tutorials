from vedo import load, show, Volume

path_nifti = "volume.nii.gz"
path_stl = "output_file.stl"

def visualize_stl(path_to_file, bg=(1,1,1), mesh_color=(1,0,0)):
    # Load an STL file
    mesh = load(path_to_file)
    mesh.color(mesh_color)

    # Show the mesh
    show(mesh, bg=bg)

def visualize_nifti(path_to_file, bg=(1,1,1), mesh_color=(1,0,0)):
    # Load a NIfTI file
    vol = Volume(path_to_file)

    # Show the volume
    show(vol, bg=bg)


visualize_stl(path_stl)
visualize_nifti(path_nifti)