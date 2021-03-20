# IT2901 CrunchWiz

CrunchWiz computes measurements from devices like tobi eyetrakers, Empatica E4 wristband and skeltal data from openPose.

## Dashboard

### Start dashboard

- `cd frontend && yarn start`

### Start websocket

- `cd backend/websocket && python3 websocket.py`

## CrunchWiz

- `cd backend && python3 app.py`

## Test
* backend test `pytest --cov=backend/` 
* frontend lint `yarn lint`
* backend lint `flake8`
* backend check import order `isort`

## Building OenPose from source
***Note* These are only the specific versions i used to compile, other combinations might work**

- Windows 10
- Nvidia Pascal GPU
- CUDA v11.1
- cuDNN v8.0.5 for CUDA v11.1
- python v3.7
- Visual Studio 2019 Enterprise

Refer to the [official documentation](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md) for further reading
### Prerequisites 
1. Install CMake GUI (`cmake-X.X.X-rc5-windows-x86_64.msi`) from https://cmake.org/download/

2. Install `Visual Studio 2019 Enterprise` (Community will not work)
	- Make sure to enable all C++ related flags in installation setup
	- *Note these are the flags i used, everything might not be required.*
	![](https://i.gyazo.com/83253a69dea33d8370fef6fa2c94c96d.png)
	![](https://i.gyazo.com/fb25c8572c287d6ba026d9c81de14c62.png)
	![](https://i.gyazo.com/73700a1f5f121e87e65d0649b22d19fa.png)
	
3. Download and install `CUDA v11.1`
    - Make sure to install CUDA after Visual Studio
    

4. Download `cuDNN v8.0.5` for CUDA v11.1
    - To install cuDNN unzip and copy the content into the CUDA folder (C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.1)

5. Install python version `3.7.x` (`3.8` and `3.9` will likely cause compilation failure)

6. Install `opencv-python (pip install opencv-python)`

### installation
If you face any issues with this refer to the [official documentation](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md#clone-openpose)

#### CMake configuration
1. Open CMake-GUI
2. Select the `openpose` folder as source. Create an empty folder in the root folder named `build` and select that as the build folder
![](https://i.gyazo.com/9fc9e27f829b99d6dcd26f3a770c26ef.png)
3. Press `Configure` and select `Visual Studio 16 2019` as the generator and `x64` as the platform for generator. Press `Finish`
![](https://i.gyazo.com/53bd3446411cf604a25b54f606d2823d.png)
4. Enable the `BUILD_PYTHON` flag and press `Configure` again

![](https://i.gyazo.com/613a94ae8b07e9c7686a63ca26804e33.png)

5. Press `Configure` once more. It should show `Configuring done` on the last line of the bottom box.
6. Press `Generate` to generate the Visual Studio solution
7. When `Generating done` appears in the bottom box, press `Open Project` to open the solution in Visual Studio

#### Compilation
1. In `Visual Studio` change the build configuration from `Debug` to `Release`
![](https://i.gyazo.com/e8645fe5b511a78d02748cc4376f39d7.png)
2. Press `F7` to compile the project.
3. Press `F5` to run the project with default settings.

#### Running the python API
Follow the (official documenation)[https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/03_python_api.md#installation]
1. Make sure there is a filed named `pyopenpose.cpXX-win_amd64.pyd` in `openpose\build\python\openpose\Release` and that the numbers match the python version you are trying to run (3.7). 
