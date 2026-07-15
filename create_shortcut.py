import os
import subprocess

def create_desktop_shortcut():
    print("[Shortcut Creator] Initializing Desktop shortcut creation...")
    
    root_dir = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(root_dir, "start_meridian.bat")
    
    # Locate user desktop paths
    desktops = []
    standard_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    if os.path.exists(standard_desktop):
        desktops.append(standard_desktop)
    
    onedrive_desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
    if os.path.exists(onedrive_desktop):
        desktops.append(onedrive_desktop)
        
    if not desktops:
        print("Error: Could not locate Windows Desktop directory.")
        return
        
    for desktop in desktops:
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
            print(f"Error creating shortcut at '{shortcut_path}' via PowerShell: {e}")

if __name__ == "__main__":
    create_desktop_shortcut()
