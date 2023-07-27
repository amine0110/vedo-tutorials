# 3D Medical Imaging Visualization with Vedo

This Python project demonstrates how to use Vedo, a powerful module for scientific visualization, analysis, and animation of 3D objects, to visualize medical imaging data. The code includes functions to open and visualize STL (Stereolithography) and NIfTI (Neuroimaging Informatics Technology Initiative) files, which are widely used in medical imaging.

<img width="722" alt="stl" src="https://github.com/amine0110/vedo-visualization/assets/37108394/81709d6e-616a-4b82-90f1-f0f493482e5c">

## Installation
To run this code, you will need to have Python installed on your machine. This project also uses the vedo library, which you can install via pip:
```
pip install vedo
```

## Usage
To use this code, you will need to have STL and NIfTI files available. These are not included in the repository.

Here's how you can visualize an STL or NIfTI file:

```Python
from vedo import load, show, Volume

path_nifti = "path_to_your_file.nii.gz"
path_stl = "path_to_your_file.stl"

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

```

## 🏫 Courses

| Title | Tags | Link |
| --- | --- | --- |
| Python for Medical Imaging | `Dicom` `NIFTI` `ITK` `SimpleITK` `3D` `Python` | [Udemy](https://www.udemy.com/course/python-programming-for-medical-imaging/?referralCode=4EB87F3DE56679A11DA8) |
| How to Work With Dicom Using Python | `Dicom` `Medical Imaging` `Python` | [Udemy](https://www.udemy.com/course/how-to-work-with-dicom-using-python/?referralCode=ECBFF2BA3DED3608BE91) |
| How to Improve Medical Image Classification Results | `Medical Imaging` `Image Classification` `Python` | [YouTube](https://youtu.be/IXJMNGiBWy4) | 
| Automatic Liver Segmentation Using PyTorch and Monai | `Medical Imaging` `Image Segmentation` `Python` | [YouTube](https://youtu.be/AU4KlXKKnac) |
| Learn Tkinter from Scratch to Create Desktop Applications | `Python` `Tkinter` `GUI` | [YouTube](https://youtu.be/Fv82RX4cWW4) |
| Learn C++ for Beginners | `C++` `Basics` | [YouTube](https://youtu.be/94T4RQiD4Lo) |
