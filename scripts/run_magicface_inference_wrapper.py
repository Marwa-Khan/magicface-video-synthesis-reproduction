
import sys
import os
import runpy
from pathlib import Path

repo_dir = Path(r"/content/drive/MyDrive/magicface_reproduction/official_MagicFace")
inference_py = repo_dir / "inference.py"

sys.path.insert(0, str(repo_dir))
os.chdir(repo_dir)

import torch
import torchvision
import torchvision.transforms

print("="*60)
print("MagicFace Wrapper")
print("="*60)
print("Torch:", torch.__version__)
print("Torchvision:", torchvision.__version__)
print("CUDA:", torch.cuda.is_available())

#
# IMPORTANT
# Forward every argument exactly as received.
#
sys.argv = [str(inference_py)] + sys.argv[1:]

runpy.run_path(str(inference_py), run_name="__main__")
