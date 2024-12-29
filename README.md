# Fusion360_Model_Checker

The Model Checker script scans the open Fusion 360 design for common issues related to the components and bodies within the model. Here's a breakdown of its functionality:

Missing Components: It checks if any components are missing in the model.
Invalid Materials: It identifies components that don't have valid materials assigned.
Invalid Densities: The script checks for components without valid densities.
Color Issues: It verifies that the components have colors properly assigned.
Invalid Joints: It checks if there are any problematic joints in the model.
Duplicate Bodies: The script detects duplicate bodies within the design.
Geometry Problems: It identifies components with any problematic geometry, such as faces or edges that might cause issues.

The script gives a report with any detected issues, which helps ensure that the design is well-constructed and ready for export or further work.
