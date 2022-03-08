import os
import data
import header
import threading


def scan_destination_for_mp4_files():
    """
    scans the destination folder and collects all mp4 files names
    :return: void
    """
    for file in os.listdir(header.source_folder_path):
        if "mp4" in file:
            header.source_files_list.append(str(file))



def extract_data_from_mp4_for_all_files_in_the_folder(self):
    """
    extracting all meta data from source files via exiftool
    :param self:
    :return:
    """
    threads = []

    for file in header.source_files_list:
        threads.append(threading.Thread(target=os.system, args=("exiftool -ee -a -u -g -b -p \"$accelerometer\" "+header.source_folder_path+"\\"+str(file)+" > "+header.source_folder_path+"\\"+(str(file).split('.'))[0]+".txt",)))

    for thread in threads:
        thread.start()



def raw_data_file_hanling():
    pass

def text_file_handling(file):
    file_io = open(header.source_folder_path + "\\" + (str(file).split('.'))[0] + ".txt", "r")
    header.raw_data[(str(file).split('.'))[0] + ".txt"] = file_io.read()

def read_data_from_text_meta_data(self):
    threads = []
    for file in header.source_files_list:
        threads.append(threading.Thread(target=text_file_handling, args=(str(file),)))

    for thread in threads:
        thread.start()




