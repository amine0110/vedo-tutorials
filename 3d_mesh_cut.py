import vedo
from vedo.applications import FreeHandCutPlotter
from vedo import load, Volume

vedo.settings.use_parallel_projection = True  # to avoid perspective artifacts

def cut_3d(file_path : str):
    if file_path.endswith('.nii') or file_path.endswith('.nii.gz'):
        # Load a volume/segmentation (nii / nii.gz)
        mesh = Volume(file_path).isosurface()

    if file_path.endswith('.stl'):
        # Load an STL file
        mesh = load(file_path).color('red')

    plt = FreeHandCutPlotter(mesh).add_hover_legend()
    plt.start(axes=0, interactive=1).close()


cut_3d('./data/file.stl')