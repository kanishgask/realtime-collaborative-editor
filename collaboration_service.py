class CollaborationService:

    def __init__(self):
        self.active_sessions = {}

    def join_document(self, doc_id, user_id):

        if doc_id not in self.active_sessions:
            self.active_sessions[doc_id] = []

        self.active_sessions[doc_id].append(user_id)

    def leave_document(self, doc_id, user_id):

        if doc_id in self.active_sessions:
            self.active_sessions[doc_id].remove(user_id)

    def get_active_users(self, doc_id):

        return self.active_sessions.get(doc_id, [])
