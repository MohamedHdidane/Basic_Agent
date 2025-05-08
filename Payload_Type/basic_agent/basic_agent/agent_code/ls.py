import os

def execute_ls():
    """Execute ls command on the target."""
    try:
        return os.popen("ls").read()
    except Exception as e:
        return f"Error executing ls: {e}"