class DocumentService:

    def __init__(self):
        self.documents = {}
        self.doc_id = 0

    def create_document(self, owner_id, title):

        self.doc_id += 1

        document = {
            "doc_id": self.doc_id,
            "owner": owner_id,
            "title": title,
            "content": ""
        }

        self.documents[self.doc_id] = document

        return document

    def get_document(self, doc_id):

        return self.documents.get(doc_id)

    def update_content(self, doc_id, content):

        if doc_id in self.documents:
            self.documents[doc_id]["content"] = content
