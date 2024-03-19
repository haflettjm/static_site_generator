class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def eq(self, obj2):
        if (self.text == obj2.text) and (self.text_type == obj2.text_type):
            return True
        else:
            return False
    def repr(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
