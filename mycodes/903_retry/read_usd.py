'''
Author: Wtrwater 1921852290@qq.com
Date: 2024-09-03 17:35:38
LastEditors: Wtrwater 1921852290@qq.com
LastEditTime: 2024-09-03 22:24:52
FilePath: /IsaacLab/mycodes/903_retry/read_usd.py
Description: Read the positions of rigid bodies in a USD file.

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from pxr import Usd, UsdGeom, UsdPhysics, Gf


def list_rigid_bodies_with_poses(usd_file):
    # Open the USD file
    stage = Usd.Stage.Open(usd_file)

    # List to store rigid bodies and their poses (position and rotation)
    rigid_bodies_info = []

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

                # Extract rotation as a quaternion
                rotation = transform.ExtractRotation()

                # Store the rigid body path, position, and rotation
                rigid_bodies_info.append((prim.GetPath().pathString, position, rotation))

    return rigid_bodies_info


# Path to your USD file
usd_file_path = "/home/jiadong/CubeTrack/CubeTrack_Isaac/509_NoBelts/CubeTrackV2_Nobelts.usd"

# List all rigid bodies with their poses
rigid_bodies_info = list_rigid_bodies_with_poses(usd_file_path)

# Print the list of rigid bodies and their poses
print("Rigid Bodies and their poses in the USD file:")
for body, position, rotation in rigid_bodies_info:
    print(f"Rigid Body: {body}, Position: {position}, Rotation (quaternion): {rotation}")
