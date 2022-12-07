class File:

    def __init__(self, id, name=None, ext=None, description=None, create_at=None, create_by=None):
        self.id = id
        self.name = name
        self.ext = ext
        self.description = description
        self.create_at = create_at
        self.create_by = create_by

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'ext' : self.ext,
            'description' : self.description,
            'create_at' : self.create_at,
            'create_by' : self.create_by
        }