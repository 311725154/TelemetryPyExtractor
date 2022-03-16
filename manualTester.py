import mission
import header

m = mission

m.scan_destination_for_mp4_files()

for path in header.source_files_list:
    print(path)






# EXPERIMENTAL CODE CONTAINER

# header.source_folder_path = folder_path.get()