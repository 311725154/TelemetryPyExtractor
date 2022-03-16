#TODO: crearte controler file logic

import header

import data
import threading
import mission


class Controller:

    def __init__(self, action):
        """
        The constructor push to stack threads when the structure is: [<boolean variable - for define ability of parallel execution> , <the thread with parameters> ]
        :param action: string - action identifier
        """
        if action in "extract telemetry from mp4":

            header.stack.append([True, threading.Thread(target=mission.scan_destination_for_mp4_files)])
            header.stack.append([True, threading.Thread(target=mission.extract_data_from_mp4_for_all_files_in_the_folder)])




    def execute(self):
        """
        execution of all threads in the stack according to base flag
        :return: void
        """
        for thread in header.stack:
            if thread[0]:
                thread[1].start()
                thread[1].join()
            else:
                thread[1].start()
