# MKZ CONTROLLER 
This is a workspace repository integrated with docker which is made for path recording and following for a Dataspeed Lincoln MKZ. This codebase was translated into ros2 based on https://github.com/Kchour/MKZ_controller/tree/controllers/vehicle_controllers


## Initializing the repository
The repository is integrated with docker and it's use is highly recommended. Should docker not be utilized, the instructions contained in the [Dockerfile](/Dockerfile) can be utilized from a base install of ROS 2 Humble on Ubuntu 22.04.

If using docker then any distribution of linux can be utilized in addition to Windows with a little extra setup (instructions to be added later)

Assuming that docker is installed, the following steps can be taken to initialize the repository.
1. Clone:
   * `git clone https://github.com/LizFile01/MKZ_SIMULATOR_PROTYPE1`
2. Cd into folder:
   * `cd MKZ_SIMULATOR_PROTYPE1`
3. Build the docker image: 
   * `docker compose build`
4. Add the container running alias to your `.bashrc` with this command :
   * `echo "alias mkz='docker compose -f ~/MKZ_SIMULATOR_PROTYPE1/docker-compose.yml run --rm ros_humble'" >> ~/.bashrc`
   * NOTE: Path will need to be changed if not using home folder for repository
5. Source your `.bashrc` file to utilize new alias
   * `. ~/.bashrc`
   * Or just open a new terminal
6. Open a container within your terminal using the `mkz` alias
   * The rest of the instructions will assume that you are within an MKZ container
7. Once in the container run the `build` command (defined by below alias) to build the ROS 2 workspace

## Running

The following aliases are already within the `.bashrc` file ready for you to use:
* `sc` sources the workspace, this is also done automatically upon entering the container
* `sim` runs the simulation
* `record` runs the waypoint recorder and listens on the `/vehicle/twist_cmd` topic for commands to manually control the vehicle
* `teleop` runs the `teleop_twist_keyboard` node and allows you to control the MKZ when already running `record` in another terminal
* `teleop_gui` instead utilizes `rqt_teleop` for a graphical version of teleop (seems to be fairly buggy)
* `control` runs the lateral and longitudinal controllers and follows the recorded path
