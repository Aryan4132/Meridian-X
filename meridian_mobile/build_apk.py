#!/usr/bin/env python
"""
Meridian-X Mobile APK Builder Entrypoint.
Delegates to root build_mobile.py for consistent Flutter app builds.
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
build_script = os.path.join(root_dir, "build_mobile.py")

if __name__ == "__main__":
    if not os.path.exists(build_script):
        print(f"[Error] Core builder script not found at: {build_script}")
        sys.exit(1)
    
    # Execute build_mobile.py with current arguments
    import subprocess
    cmd = [sys.executable, build_script] + sys.argv[1:]
    res = subprocess.run(cmd)
    sys.exit(res.returncode)
