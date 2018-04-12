import unittest
from corsera_python.module_two.assignment13 import count_mail

def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)

class assignment13(unittest.TestCase):

    def test_fail(self):
        mbox_short_file = get_file_path('mbox-short.txt')
        self.assertEqual('cwen@iupui.edu 5', count_mail(mbox_short_file))



if __name__ == '__main__':
    unittest.main()
