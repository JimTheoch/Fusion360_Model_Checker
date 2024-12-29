import adsk.core, adsk.fusion, adsk.cam

def check_missing_components(root_component):
    missing_components = []
    for occurrence in root_component.occurrences:
        if not occurrence.component:
            missing_components.append(occurrence)
    return missing_components

def check_invalid_materials(component):
    invalid_materials = []
    if hasattr(component, 'bodies'):  # Ensure the component has bodies
        for body in component.bodies:
            if not body.material:
                invalid_materials.append(body)
    return invalid_materials

def check_invalid_densities(component):
    invalid_densities = []
    if hasattr(component, 'bodies'):  # Ensure the component has bodies
        for body in component.bodies:
            if not body.material or not body.material.density:
                invalid_densities.append(body)
    return invalid_densities

def check_color_issues(component):
    color_issues = []
    if hasattr(component, 'bodies'):  # Ensure the component has bodies
        for body in component.bodies:
            if not body.appearance:
                color_issues.append(body)
    return color_issues

def check_joints(root_component):
    invalid_joints = []
    for joint in root_component.joints:
        if not joint.isValid:
            invalid_joints.append(joint)
    return invalid_joints

def check_duplicate_bodies(root_component):
    body_names = {}
    duplicate_bodies = []
    if hasattr(root_component, 'bodies'):  # Ensure the component has bodies
        for body in root_component.bodies:
            if body.name in body_names:
                duplicate_bodies.append(body)
            else:
                body_names[body.name] = body
    return duplicate_bodies

def check_geometry_issues(root_component):
    geometry_issues = []
    if hasattr(root_component, 'bodies'):  # Ensure the component has bodies
        for body in root_component.bodies:
            if not body.isValid:
                geometry_issues.append(body)
    return geometry_issues

def run(context):
    try:
        # Initial setup
        app = adsk.core.Application.get()
        ui = app.userInterface
        doc = app.activeDocument
        
        # Check if active document is a design (part or assembly)
        if not doc.design:
            ui.messageBox("Active document is not a design. Please open a design file.")
            return

        root_component = doc.design.rootComponent

        # Debugging: Print out to confirm script execution
        ui.messageBox("Model Checker Script Started")
        
        # Check for issues
        missing_components = check_missing_components(root_component)
        invalid_materials = check_invalid_materials(root_component)
        invalid_densities = check_invalid_densities(root_component)
        color_issues = check_color_issues(root_component)
        invalid_joints = check_joints(root_component)
        duplicate_bodies = check_duplicate_bodies(root_component)
        geometry_issues = check_geometry_issues(root_component)

        # Prepare report
        report = "Model Check Report:\n\n"
        report += f"Missing Components: {len(missing_components)}\n"
        report += f"Invalid Materials: {len(invalid_materials)}\n"
        report += f"Invalid Densities: {len(invalid_densities)}\n"
        report += f"Color Issues: {len(color_issues)}\n"
        report += f"Invalid Joints: {len(invalid_joints)}\n"
        report += f"Duplicate Bodies: {len(duplicate_bodies)}\n"
        report += f"Geometry Issues: {len(geometry_issues)}\n"

        # Output the results
        ui.messageBox(report)

    except Exception as e:
        ui.messageBox(f"Error: {str(e)}")
