## Installation

### 1. Install System Dependencies (macOS / Linux Only)
If you are on macOS or Linux, ensure you have the core GDAL binaries installed on your system before proceeding:
* **macOS (Homebrew)**: `brew install gdal`
* **Linux (Ubuntu/Debian)**: `sudo apt-get install libgdal-dev`
* **Windows**: Skip this step.

### 2. Setup the Python Environment
Clone the repository, navigate to the folder, and run the following commands to install dependencies:

```bash
# Install standard dependencies and the installation utility
pip install -r requirements.txt

# Run the installer tool to link GDAL to your Python environment
gdal-installer
```
