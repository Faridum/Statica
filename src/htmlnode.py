class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag if tag is not None else None
        self.value = value if value is not None else None
        self.children = children if children is not None else None
        self.props = props if props is not None else None

    def to_html(self):
        raise NotImplementedError("Subclasses must implement the to_html method.")

    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"