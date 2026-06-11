import os
import subprocess

def create_desktop_shortcut():
    print("[Shortcut Creator] Initializing Desktop shortcut creation...")
    
    root_dir = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(root_dir, "start_meridian.bat")
    
    # Locate user desktop path
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.exists(desktop):
        # Fallback to OneDrive Desktop if synced
        desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
        
    if not os.path.exists(desktop):
        print("Error: Could not locate Windows Desktop directory.")
        return
        
    shortcut_path = os.path.join(desktop, "Meridian-X.lnk")
    
    # PowerShell command to create shortcut via WScript.Shell COM object
    ps_script = f"""
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
    $Shortcut.TargetPath = "{bat_path}"
    $Shortcut.WorkingDirectory = "{root_dir}"
    $Shortcut.Description = "Launch Meridian-X Autonomous offline Desktop Agent"
    $Shortcut.Save()
    """
    
    try:
        # Run PowerShell script
        subprocess.run(
            ["powershell", "-Command", ps_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print(f"[Shortcut Creator] Successfully created Desktop shortcut at '{shortcut_path}'.")
    except Exception as e:
        print(f"Error creating shortcut via PowerShell: {e}")

if __name__ == "__main__":
    create_desktop_shortcut()
