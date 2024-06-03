import os
import subprocess
import urllib.request

image_url = "https://unsplash.com/photos/0VawIhTEdpM/download?ixid=M3wxMjA3fDB8MXxhbGx8MTZ8fHx8fHwyfHwxNzE3NDEzMzgzfA&force=true"
image_path = os.path.expanduser("~/Desktop/downloaded_image.jpg")
debug = False

urllib.request.urlretrieve(image_url, image_path)
print(f"Downloaded image to {image_path}")

applescript_command = f"""
tell application "System Events"
    set desktopImage to POSIX file "{image_path}"
    tell every desktop
        set picture to desktopImage
    end tell
end tell
"""

process = subprocess.run(['osascript', '-e', applescript_command], capture_output=True, text=True)

debug and print("Output:", process.stdout)
debug and print("Errors:", process.stderr)
