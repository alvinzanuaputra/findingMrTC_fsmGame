import os
import glob
from PIL import Image

def normalize_images():
    # Folder character
    char_folder = r"c:\Users\User\Downloads\findingMrTC_fsmGame-main\findingMrTC_fsmGame-main\game\images\character"
    png_files = glob.glob(os.path.join(char_folder, "*.png"))
    
    target_height = 650
    
    for file_path in png_files:
        try:
            img = Image.open(file_path)
            img = img.convert("RGBA")
            
            # Cari bounding box (menghilangkan transparan)
            bbox = img.getbbox()
            if bbox:
                # Crop gambar
                cropped = img.crop(bbox)
                
                # Hitung skala untuk tinggi target
                scale = target_height / float(cropped.height)
                new_width = int(cropped.width * scale)
                
                # Resize
                resized = cropped.resize((new_width, target_height), Image.Resampling.LANCZOS)
                
                # Timpa file lama
                resized.save(file_path)
                print(f"Normalized: {os.path.basename(file_path)} (Width: {new_width}, Height: {target_height})")
            else:
                print(f"Skipped (Empty): {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"Error processing {os.path.basename(file_path)}: {e}")

if __name__ == "__main__":
    normalize_images()
