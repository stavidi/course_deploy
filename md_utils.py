"""
Utils for markdown -> html conversion.
"""

import markdown

def html(text_md):
    if not isinstance(text_md, str):               # list of strings
        print('LIST', text_md)
        text_md = '\n'.join(text_md)
    return markdown.markdown(text_md, extensions=['extra', 'codehilite'])