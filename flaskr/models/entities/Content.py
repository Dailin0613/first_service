class Content:

    def __init__(self, id, content=None):
        self.id = id
        self.content = content

    def to_json(self):
        return {
            'id' : self.id,
            'content' : self.content
        }