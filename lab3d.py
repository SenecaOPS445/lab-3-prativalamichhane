#!/usr/bin/env python3
# Author ID: 167520220
import subprocess
def free_space():
    # Execute the df command and capture the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'",
                            shell=True,
                            capture_output=True,
                            text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())

