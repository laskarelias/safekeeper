class DocumentAttachment:
    def __init__(self, contents):
        self.contents = contents

    def save(self):
        print(f'saving {self.contents}')