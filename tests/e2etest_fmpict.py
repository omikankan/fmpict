# coding: utf-8

import unittest
import sys
import os
import subprocess
import shutil

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_path)
import fmpict


class TestFMPict(unittest.TestCase):
    def setUp(self):
        self._target_dir_path = root_path +  '\\fmpict\\'
        self._work_dir_path = root_path +  '\\tests\worktmp\\'
        self._test_dir_path = root_path +  '\\tests\\fm_sample\\'
        if os.path.exists(self._work_dir_path):
            shutil.rmtree(self._work_dir_path)
        os.mkdir(self._work_dir_path)
    
    def testRunningPict(self):
        self.assertEqual(True, True)
        os.chdir(self._work_dir_path)
        command = r'python %sfmpict.py %ssimple.mm' % (self._target_dir_path, self._test_dir_path)
        out_proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout_data, stderr_data = out_proc.communicate()
        out_proc.wait()

        self.assertFalse(stderr_data)
        expected_output = b'A\tB\r\n3\tx\r\n3\tz\r\n1\tx\r\n1\ty\r\n2\tx\r\n3\ty\r\n1\tz\r\n2\tz\r\n2\ty\r\n'
        self.assertEqual(expected_output, stdout_data)

if __name__ == '__main__':
    unittest.main()