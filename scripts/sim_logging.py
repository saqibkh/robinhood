#!/usr/bin/python

import os
import logging
import time
import string
import datetime


class SIMLOG:
    def __init__(self, debug=False, error=True, info=True, warning=True):
        self.debug_log = debug
        self.error_log = error
        self.info_log = info
        self.warning = warning

        # Delete existing log files if they exists
        if os.path.exists("log.txt"):
            os.remove("log.txt")

    def debug(self, i_msg):
        if self.debug_log:
            print("DEBUG LOG: " + str(i_msg))
        file_object = open('log.txt', 'a+')
        file_object.write("DEBUG LOG: " + str(i_msg) + "\n")
        file_object.close()

    def error(self, i_msg):
        if self.error_log:
            print("ERROR LOG: " + str(i_msg))
        file_object = open('log.txt', 'a+')
        file_object.write("ERROR LOG: " + str(i_msg) + "\n")
        file_object.close()

    def info(self, i_msg):
        if self.info_log:
            print("INFO LOG: " + str(i_msg))
        file_object = open('log.txt', 'a+')
        file_object.write("INFO LOG: " + str(i_msg) + "\n")
        file_object.close()

    def warning(self, i_msg):
        if self.info_warning:
            print("WARNING LOG: " + str(i_msg))
        file_object = open('log.txt', 'a+')
        file_object.write("WARNING LOG: " + str(i_msg) + "\n")
        file_object.close()
