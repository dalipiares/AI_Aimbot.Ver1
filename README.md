# Screen Object Detection with YOLOv5 and CUDA

This program scans your screen in real-time using a YOLOv5 object detection model, drawing bounding boxes around detected objects and displaying their names with confidence scores. It utilizes CUDA for GPU acceleration, providing fast and efficient inference for aimbot purposes in gaming environments.

## Requirements

- Python 3.x
- NVIDIA GPU with CUDA support
- [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dalipiares/AI_Aimbot.Ver1.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd AI_Aimbot.Ver1
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

4. **Activate the virtual environment:**

   On **Windows (Git Bash)**:

   ```bash
   source .venv/Scripts/activate
   ```

   On **Windows (Command Prompt)**:

   ```cmd
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Install the correct version of PyTorch with CUDA support:**

   Visit the [PyTorch website](https://pytorch.org/get-started/locally/) to find the correct command for your system. For example, for CUDA 12.4:

   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```

7. **Install the package using `pyproject.toml`:**

   ```bash
   pip install .
   ```

## Usage

Run the main script:

```bash
python main.py
```

- The program will start capturing your screen and detecting objects in real-time.
- Press `q` to exit the program.

## Notes

- If using multiple monitors, adjust the `monitor` index in `main.py`.
- Ensure NVIDIA drivers and CUDA Toolkit are properly installed.
