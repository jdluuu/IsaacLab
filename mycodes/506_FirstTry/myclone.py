# Copyright (c) 2021-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from omni.isaac.kit import SimulationApp

simulation_app = SimulationApp({"headless": False})

import sys

import carb
import numpy as np
from omni.isaac.cloner import GridCloner
from omni.isaac.core import World
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import add_reference_to_stage, get_stage_units

assets_root_path = get_assets_root_path()
if assets_root_path is None:
    carb.log_error("Could not find Isaac Sim assets folder")
    simulation_app.close()
    sys.exit()

my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()

# create initial robot
# asset_path = assets_root_path + "/Isaac/Robots/CubeTrack/CubeTrack.usd"
asset_path = "/home/jiadong/CubeTrack_Isaac/506_FirstTry/CubeTrack.usd"
NewPrim = add_reference_to_stage(usd_path=asset_path, prim_path="/World/CubeTracks/CubeTrack_0")

# create GridCloner instance
cloner = GridCloner(spacing=2)

# generate paths for clones
target_paths = cloner.generate_paths("/World/CubeTracks/CubeTrack", 4)

# clone
position_offsets = np.array([[0, 0, 1]] * 4)

cloner.clone(
    source_prim_path="/World/CubeTracks/CubeTrack_0",
    prim_paths=target_paths,
    position_offsets=position_offsets,
    replicate_physics=True,
    base_env_path="/World/CubeTracks",
)

### @ 这一部分还没有搞懂，这是需要搞懂的。
# # create ArticulationView
# CubeTracks = ArticulationView(prim_paths_expr="/World/CubeTracks/.*/torso", name="CubeTracks_view")
# my_world.scene.add(CubeTracks)

from pxr import UsdGeom, Gf

xformable = UsdGeom.Xformable(NewPrim)

# Access the existing transform ops
xform_ops = xformable.GetOrderedXformOps()
scale_op = None
for op in xform_ops:
    if op.GetOpType() == UsdGeom.XformOp.TypeScale:
        scale_op = op
        break

# If a scale operation is not found, create one
if not scale_op:
    scale_op = xformable.AddScaleOp()

scale_factor = 1.0

my_world.reset()
while simulation_app.is_running():
    scale_factor += 0.01  # Increment scale factor
    scale_op.Set(Gf.Vec3f(scale_factor, scale_factor, scale_factor))
    my_world.step()


simulation_app.close()