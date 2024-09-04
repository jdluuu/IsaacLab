"""Launch Isaac Sim Simulator first."""
import argparse

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Tutorial on using the interactive scene interface.")
parser.add_argument("--num_envs", type=int, default=2, help="Number of environments to spawn.")
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app
"""Rest everything follows."""

import time
import torch

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.sim import SimulationContext
from omni.isaac.lab.scene import InteractiveScene
from omni.isaac.lab.assets import Articulation

from cubetrack_scene_ground import CubeTrackSceneCfg


def run_simulator(sim: sim_utils.SimulationContext, scene: InteractiveScene):
    """Runs the simulation loop."""
    # Extract scene entities
    # note: we only do this here for readability.
    robot: Articulation = scene["CubeTrack"]
    Belts = []
    # stack the belts in a list
    for i in range(1, 36):
        prim_path = f"L_Belt{i:03}"
        Belts.append(scene[prim_path])
        prim_path = f"R_Belt{i:03}"
        Belts.append(scene[prim_path])

    # Define simulation stepping
    sim_dt = sim.get_physics_dt()
    count = 0

    last_reset_time = time.time()  # Initialize last reset time

    # Simulation loop
    while simulation_app.is_running():
        # Reset the belt first time
        if count % 300 == 0:
            start_reset_time = time.time()
            # reset counter
            count = 0

            # Calculate the time since the last reset
            time_since_last_reset = start_reset_time - last_reset_time
            print(f"[INFO]: Time since last reset: {time_since_last_reset:.4f} seconds")
            last_reset_time = start_reset_time  # Update last reset time

            # reset the belts
            for belt in Belts:
                belt_state = belt.data.default_root_state.clone()
                belt_state[:, :3] += scene.env_origins
                belt.write_root_state_to_sim(belt_state)

            # reset the robot
            root_state = robot.data.default_root_state.clone()
            root_state[:, :3] += scene.env_origins
            robot.write_root_state_to_sim(root_state)
            # set joint positions with some noise
            joint_pos, joint_vel = robot.data.default_joint_pos.clone(), robot.data.default_joint_vel.clone()
            # joint_pos += torch.rand_like(joint_pos) * 0.1
            robot.write_joint_state_to_sim(joint_pos, joint_vel)
            # clear internal buffers
            scene.reset()

        # Apply random action
        poses = torch.zeros_like(robot.data.joint_pos)
        poses[:, 6:8] = 1.57  # rad。但是在IsaacSim编辑器中是角度制。Fuck

        # import pdb
        # pdb.set_trace()

        velos = torch.zeros_like(robot.data.joint_vel)
        velos[:, 0:4] = 10.0  # rad

        robot.set_joint_velocity_target(velos)
        robot.set_joint_position_target(poses)
        # velos = torch.zeros_like
        # -- apply action to the robot
        # robot.set_joint_effort_target(efforts)
        # -- write data to sim
        scene.write_data_to_sim()
        # Perform step
        sim.step()
        # Increment counter
        count += 1
        # Update buffers
        scene.update(sim_dt)


def main():
    """Main function."""
    # Load kit helper
    # sim_cfg = sim_utils.SimulationCfg(device="cpu", use_gpu_pipeline=False)
    sim_cfg = sim_utils.SimulationCfg(dt=1.0 / 240.0)
    sim = SimulationContext(sim_cfg)
    # Set main camera
    sim.set_camera_view([2.5, 0.0, 4.0], [0.0, 0.0, 2.0])  # type: ignore
    # Design scene
    scene_cfg = CubeTrackSceneCfg(num_envs=args_cli.num_envs, env_spacing=2.0)
    scene = InteractiveScene(scene_cfg)
    # Play the simulator
    sim.reset()
    # Now we are ready!
    print("[INFO]: Setup complete...")
    # Run the simulator
    # create_belt_impl()
    run_simulator(sim, scene)


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()
