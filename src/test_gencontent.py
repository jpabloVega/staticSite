import unittest
from gencontent import extract_title
class TestHTMLNode(unittest.TestCase):
    
    def test_extract_title(self):
        md = """
### Im not the title
##### Im not either
## Im almost a title
#     Real Title
"""
        title = extract_title(md)
        self.assertEqual("Real Title", title)
        