# 📊 ER Diagram – Collaborative Editor

USERS
- user_id (PK)

DOCUMENTS
- doc_id (PK)
- owner_id (FK)

DOCUMENT_VERSIONS
- version_id (PK)
- doc_id (FK)

Relationship:

User 1 → N Documents  
Document 1 → N Versions
