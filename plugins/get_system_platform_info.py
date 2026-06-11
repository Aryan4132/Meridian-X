TIER = 2

import platform

def get_system_platform_info() -> str:
    """
    Returns a string containing the operating system type, platform release version, and processor architecture.
    
    Returns:
        str: A formatted string with system information.
    """
    os_type = platform.system()
    platform_release = platform.release()
    processor_architecture = platform.machine()
    
    return f"Operating System: {os_type}, Release Version: {platform_release}, Processor Architecture: {processor_architecture}"
