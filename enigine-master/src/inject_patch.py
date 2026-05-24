import os
from pathlib import Path

# The header you want to force-include
PATCH_INCLUDE = '#include "math_patch.h"\n'

# Folders you want the script to completely ignore
IGNORE_FOLDERS = {'build', '.git', '.conan2', 'assets', '.vscode'}

def patch_cpp_files():
    root_dir = Path.cwd()
    count = 0
    
    print(f"Scanning for .cpp files in: {root_dir}")
    
    for path in root_dir.rglob('*.cpp'):
        # Check if the file lives inside a folder we want to ignore
        if any(ignored in path.parts for ignored in IGNORE_FOLDERS):
            continue
            
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                
            # Skip if the file already has the patch included
            if "math_patch.h" in content:
                print(f"[-] Already patched: {path.relative_to(root_dir)}")
                continue
                
            # Inject the header right at the top
            patched_content = PATCH_INCLUDE + content
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(patched_content)
                
            print(f"[+] Successfully patched: {path.relative_to(root_dir)}")
            count += 1
            
        except Exception as e:
            print(f"[!] Error processing {path.name}: {e}")
            
    print(f"\nFinished! Patched {count} new .cpp files.")

if __name__ == '__main__':
    patch_cpp_files()
