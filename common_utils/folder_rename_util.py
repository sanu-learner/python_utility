import os

def rename_folders(input_dir):
    subdir_list = [subdir for subdir in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, subdir))]
    
    for dirname in subdir_list:
        print("Renaming subdirectory : ", dirname)
        
        os.rename(os.path.join(input_dir, dirname),
                  os.path.join(input_dir, dirname.lower()))
        
    print("Renamed all folders successfully...")

if __name__ == "__main__":
    rename_folders("test_dir")