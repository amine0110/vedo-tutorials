import vedo

# Load your STL file
mesh = vedo.load('./data/file.stl')

# Initialize the plotter
plotter = vedo.Plotter(offscreen=True)  # Use offscreen rendering

# Add the mesh to the plotter
plotter.add(mesh)

# Render and capture a screenshot
plotter.show().screenshot('screenshot_path_2.png')




