

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplemented("to_html method not Implemented")
  
  def props_to_html(self):
    if self.props is None:
        return ""
    props_html = ""
    for prop in self.props:
        props_html += f' {prop}="{self.props[prop]}"'
    return props_html
  
  def __repr__(self):
    return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
  
class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
      if self.value is None:
        raise ValueError("Leaf Node requires a value")
      if self.tag is None:
        return self.value
      
      return f'<{self.tag} {self.props_to_html()}>{self.value}<{self.tag}>'
  
  def __repr__(self):
     return f"LeafNode({self.tag}, {self.value}, {self.props})'"
  
class ParentNode(HTMLNode):
   def __init__(self, tag=None, children=None, props=None):
      if self.children is None:
         raise ValueError("Parent Node requires children")
      super().__init__(tag, value, children, props)
    