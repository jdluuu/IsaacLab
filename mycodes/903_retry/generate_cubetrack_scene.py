'''
Author: Wtrwater 1921852290@qq.com
Date: 2024-09-03 23:23:28
LastEditors: Wtrwater 1921852290@qq.com
LastEditTime: 2024-09-03 23:42:26
FilePath: /IsaacLab/mycodes/903_retry/generate_cubetrack_scene.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from pxr import Usd, UsdGeom, UsdPhysics, Gf


def list_rigid_bodies_with_poses(usd_file):
    # Open the USD file
    stage = Usd.Stage.Open(usd_file)

    # Dictionary to store rigid bodies and their poses (position and rotation)
    rigid_bodies_info = {}

    # Traverse the stage to find all rigid body objects
    for prim in stage.Traverse():
        # Check if the prim has a rigid body API applied
        rigid_body_api = UsdPhysics.RigidBodyAPI(prim)
        if rigid_body_api:
            # Get the transformable API to access the position and rotation
            xformable = UsdGeom.Xformable(prim)
            if xformable:
                # Get the transformation matrix
                transform = xformable.GetLocalTransformation()

                # Extract the translation (position) component from the matrix
                position = transform.ExtractTranslation()
                position[2] += 0.15

                # Extract rotation as a quaternion
                rotation = transform.ExtractRotation().GetQuaternion()

                # Format prim path to include ENV_REGEX_NS
                formatted_prim_path = f"{{ENV_REGEX_NS}}{prim.GetPath().pathString}"

                # Store the rigid body path, position, and rotation
                rigid_bodies_info[formatted_prim_path] = {"position": position, "rotation": (rotation.GetReal(), rotation.GetImaginary()[0], rotation.GetImaginary()[1], rotation.GetImaginary()[2])}

    return rigid_bodies_info


def generate_init_state_code(rigid_bodies_info):
    init_code = ""
    for prim_path, data in rigid_bodies_info.items():
        if "right_belt" in prim_path or "left_belt" in prim_path:
            # Determine if it's a left or right belt
            if "right_belt" in prim_path:
                belt_side = "R"
            else:
                belt_side = "L"
            init_code += f"{belt_side}_Belt{prim_path.split('/')[-1][-3:]}: RigidObjectCfg = BELT_CFG.replace(prim_path=\"{prim_path}\", init_state=RigidObjectCfg.InitialStateCfg(pos={data['position']}, rot={data['rotation']}))\n"
    return init_code


# Path to your USD file
usd_file_path = "/home/jiadong/CubeTrack/CubeTrack_Isaac/509_NoBelts/CubeTrackV2_Nobelts.usd"

# List all belts with their poses
belt_info = list_rigid_bodies_with_poses(usd_file_path)

# Generate the initialization code
init_code = generate_init_state_code(belt_info)

# Print the generated initialization code
print("Generated Python initialization code for belts:")
print(init_code)
