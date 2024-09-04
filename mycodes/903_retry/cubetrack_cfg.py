'''
Author: Wtrwater 1921852290@qq.com
Date: 2024-09-03 18:03:39
LastEditors: Wtrwater 1921852290@qq.com
LastEditTime: 2024-09-04 18:52:26
FilePath: /IsaacLab/mycodes/903_retry/cubetrack_cfg.py
Description: Configuration for a simple CubeTrack robot.

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAACLAB_NUCLEUS_DIR

CubeTrack_SIMPLE_ACTUATOR_CFG = ImplicitActuatorCfg(
    joint_names_expr=["lf_wheel_joint", "lh_wheel_joint", "rf_wheel_joint", "rh_wheel_joint"],
    # saturation_effort=120.0,
    # effort_limit=80.0,
    # velocity_limit=7.5,
    stiffness={".*": 0.0},
    damping={".*": 10000.0},
)

# CubeTrack_ROB_ACTUATOR_CFG = ImplicitActuatorCfg(
#     joint_names_expr=['Flipper_to_R_QsETM_Verti', 'Flipper_to_L_QsETM_Verti'],
#     stiffness={".*": 0.0},
#     damping={".*": 10000.0},
# )
CubeTrack_ROB_ACTUATOR_CFG = ImplicitActuatorCfg(
    joint_names_expr=['Flipper_to_R_QsETM_Verti', 'Flipper_to_L_QsETM_Verti'],
    stiffness={".*": 1000.0},
    damping={".*": 2.0},
)

Useless_ACTUATOR_CFG = ImplicitActuatorCfg(
    joint_names_expr=['R_QsETM_VERTI_Joint', 'L_QsETM_VERTI_Joint', 'r_starwheel_joint', 'l_starwheel_joint'],
    stiffness={".*": 0.0},
    damping={".*": 0.0},
)

CubeTrack_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"/home/jiadong/CubeTrack/CubeTrack_Isaac/509_NoBelts/CubeTrackV2_Nobelts.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            solver_position_iteration_count=32,
            solver_velocity_iteration_count=1,
            # sleep_threshold=0.005,
            # stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(pos=(0.0, 0.0, 0.15),
                                               joint_pos={
                                                   "lf_wheel_joint": 0.0,
                                                   "lh_wheel_joint": 0.0,
                                                   "rf_wheel_joint": 0.0,
                                                   "rh_wheel_joint": 0.0,
                                                   "Flipper_to_L_QsETM_Verti": 0.0,
                                                   "Flipper_to_R_QsETM_Verti": 0.0
                                               }),
    actuators={
        "wheels": CubeTrack_SIMPLE_ACTUATOR_CFG,
        "Useless": Useless_ACTUATOR_CFG,
        "robs": CubeTrack_ROB_ACTUATOR_CFG,
    },
    soft_joint_pos_limit_factor=0.95,
)
