import os
import sys
import glob
from pathlib import Path

def get_user_input():
    """Get input from the user interactively"""
    print("📁 Universal File Renamer Tool 📁")
    print("=" * 40)
    
    # Get directory path
    while True:
        directory = input("Enter directory path [current folder]: ").strip()
        if directory == '':
            directory = '.'
        
        if not os.path.isdir(directory):
            print(f"❌ Error: '{directory}' directory not found!")
            create = input("Create directory? (y/N): ").strip().lower()
            if create in ['y', 'yes']:
                try:
                    os.makedirs(directory, exist_ok=True)
                    print(f"📁 Created directory: {directory}")
                    break
                except Exception as e:
                    print(f"❌ Could not create directory: {e}")
            else:
                print("Please enter a valid directory path.")
        else:
            break
    
    # List files in directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print("❌ No files found in this directory!")
        return None, None, None, None, None
    
    print(f"📊 Found {len(files)} files in directory")
    
    # Get base name
    base_name = input("Enter base name (e.g., 'photos'): ").strip()
    if not base_name:
        base_name = "file"
    
    # Get starting number
    while True:
        start_input = input("Start from number [1]: ").strip()
        if not start_input:
            start_number = 1
            break
        try:
            start_number = int(start_input)
            if start_number < 0:
                print("❌ Please enter positive number")
                continue
            break
        except ValueError:
            print("❌ Please enter valid number")
    
    # Get digit padding
    while True:
        digits_input = input("Number of digits (e.g., 2 for 01,02) [2]: ").strip()
        if not digits_input:
            digits = 2
            break
        try:
            digits = int(digits_input)
            if digits < 1:
                print("❌ Minimum 1 digit required")
                continue
            break
        except ValueError:
            print("❌ Please enter valid number")
    
    # Get file selection pattern
    pattern = input("File pattern (e.g., '*.jpg' for only JPG files) [all files]: ").strip()
    
    return directory, base_name, start_number, digits, pattern

def filter_files(directory, pattern):
    """Filter files based on pattern"""
    if not pattern:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    else:
        # Use glob to match pattern
        pattern_path = os.path.join(directory, pattern)
        files = [os.path.basename(f) for f in glob.glob(pattern_path) 
                if os.path.isfile(f)]
    
    return sorted(files)

def preview_changes(directory, base_name, start_number, digits, pattern):
    """Show preview of changes"""
    files = filter_files(directory, pattern)
    
    if not files:
        print(f"❌ No files found matching pattern '{pattern}'!")
        return False
    
    print(f"\n🔍 Preview of changes ({len(files)} files):")
    print("-" * 60)
    count = start_number
    for filename in files:
        name, ext = os.path.splitext(filename)
        serial = str(count).zfill(digits)
        new_name = f"{base_name}_{serial}{ext}"
        print(f"📄 {filename} → {new_name}")
        count += 1
    
    return True

def rename_files(directory, base_name, start_number, digits, pattern):
    """Rename files"""
    files = filter_files(directory, pattern)
    
    if not files:
        return 0
    
    count = start_number
    renamed = 0
    
    print("\n🔄 Renaming files...")
    for filename in files:
        name, ext = os.path.splitext(filename)
        serial = str(count).zfill(digits)
        new_name = f"{base_name}_{serial}{ext}"
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Check if new name already exists
        if os.path.exists(new_path) and old_path != new_path:
            print(f"⚠️  Skipping {filename}: {new_name} already exists")
            count += 1
            continue
            
        if old_path != new_path:
            try:
                os.rename(old_path, new_path)
                print(f"✅ {filename} → {new_name}")
                renamed += 1
            except Exception as e:
                print(f"❌ Error renaming {filename}: {e}")
        
        count += 1
    
    return renamed

def main():
    try:
        # Get user input
        directory, base_name, start_number, digits, pattern = get_user_input()
        if directory is None:
            return
        
        # Show preview
        if not preview_changes(directory, base_name, start_number, digits, pattern):
            return
        
        # Confirm
        confirm = input("\n⚠️  Proceed with renaming? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Operation cancelled")
            return
        
        # Rename files
        renamed_count = rename_files(directory, base_name, start_number, digits, pattern)
        print(f"\n🎉 Done! {renamed_count} files renamed successfully!")
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
