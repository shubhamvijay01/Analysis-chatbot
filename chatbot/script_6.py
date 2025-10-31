
import zipfile
import io
import os

# Create enhanced ZIP with all files including screenshots info
zip_buffer = io.BytesIO()

with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add all project files
    for filepath, content in all_project_files.items():
        full_path = f"bajaj-finserv-chatbot/{filepath}"
        zipf.writestr(full_path, content)
    
    # Add placeholder text files for screenshots (user will add actual images)
    screenshot_note = """# Screenshot Placeholders

Please add your actual screenshot images here:

1. chatbot-main.png - Take screenshot of main chatbot interface after running app
2. chat-response.png - Screenshot showing AI responding to a query
3. mobile-view.png - Screenshot of mobile responsive view

To generate screenshots:
1. Run: npm run dev
2. Open: http://localhost:3000
3. Use browser's screenshot tool or Snipping Tool
4. Save images in this directory

The README.md file references these images.
"""
    zipf.writestr('bajaj-finserv-chatbot/screenshots/INSTRUCTIONS.txt', screenshot_note)

# Save ZIP file
zip_buffer.seek(0)
with open('bajaj-finserv-chatbot-COMPLETE.zip', 'wb') as f:
    f.write(zip_buffer.read())

# Get file size
file_size = os.path.getsize('bajaj-finserv-chatbot-COMPLETE.zip')

print("=" * 70)
print("✅ COMPLETE ZIP FILE CREATED SUCCESSFULLY!")
print("=" * 70)
print(f"\n📦 File Name: bajaj-finserv-chatbot-COMPLETE.zip")
print(f"📊 File Size: {file_size:,} bytes ({file_size / 1024:.2f} KB)")
print(f"📁 Total Files: {len(all_project_files) + 1}")
print("\n" + "=" * 70)
print("PACKAGE CONTENTS:")
print("=" * 70)

# List all files in the ZIP
with zipfile.ZipFile('bajaj-finserv-chatbot-COMPLETE.zip', 'r') as zipf:
    file_list = sorted(zipf.filelist, key=lambda x: x.filename)
    
    # Group by directory
    dirs = {}
    for info in file_list:
        parts = info.filename.split('/')
        if len(parts) > 1:
            dir_name = parts[1] if len(parts) > 2 else 'root'
            if dir_name not in dirs:
                dirs[dir_name] = []
            dirs[dir_name].append(info)
    
    for dir_name in sorted(dirs.keys()):
        print(f"\n📂 {dir_name.upper()}/")
        for info in dirs[dir_name]:
            file_kb = info.file_size / 1024
            filename = info.filename.split('/')[-1]
            if filename:  # Skip directory entries
                print(f"   ├── {filename:<40} {file_kb:>8.2f} KB")

print("\n" + "=" * 70)
print("✅ READY TO USE!")
print("=" * 70)
print("\nWhat's included:")
print("  ✓ Complete source code (20 files)")
print("  ✓ Configuration files")
print("  ✓ React components")
print("  ✓ Financial data JSON")
print("  ✓ Setup & deployment guides")
print("  ✓ Enhanced README with documentation")
print("  ✓ Screenshot placeholders")
print("\n" + "=" * 70)
