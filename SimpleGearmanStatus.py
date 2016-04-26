#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telnetlib
import traceback
import re


class SimpleGearmanStatus:

    STATUS_REGEX = re.compile(ur'(?P<name>[\w-]+)\t(?P<queued>\d+)\t(?P<doing>\d+)\t(?P<workers>\d+)\n')
    DEFAULT_HOST = 'localhost'
    DEFAULT_PORT = 4730
    DEFAULT_TIMEOUT = 10

    TELNET = telnetlib.Telnet()

    def __init__(self, host='localhost', port=4730, timeout=DEFAULT_TIMEOUT):
        self.DEFAULT_HOST = host
        self.DEFAULT_PORT = port
        self.DEFAULT_TIMEOUT = timeout
        self.TELNET.open(
            self.DEFAULT_HOST,
            self.DEFAULT_PORT,
            self.DEFAULT_TIMEOUT
        )

    def __del__(self):
        self.TELNET.close()

    def get_all_status(self):
        try:
            tasks = {}.copy()
            self.TELNET.write(b'status\n')
            raw_data = self.TELNET.read_until(b'.')
            all_status = re.findall(self.STATUS_REGEX, raw_data)
            for _info in all_status:
                tasks[_info[0]] = {
                    'queued': _info[1],
                    'doing': _info[2],
                    'workers': _info[3]
                }
            return tasks
        except 'Exception':
            traceback.print_exc()
            return False

    def get_status(self, job_name):
        tasks = self.get_all_status()
        if (len(tasks) > 0) and (job_name in tasks):
            return tasks[job_name]
        else:
            return None


if '__main__' == __name__:

    sgs = SimpleGearmanStatus()

    status = sgs.get_all_status()

    try:
        import pprint
        pprint.pprint(status)
    except ImportError:
        pprint = None
        print (status)
