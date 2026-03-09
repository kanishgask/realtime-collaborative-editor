CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE documents (
    doc_id UUID PRIMARY KEY,
    owner_id UUID REFERENCES users(user_id),
    title VARCHAR(255),
    content TEXT
);

CREATE TABLE document_versions (
    version_id UUID PRIMARY KEY,
    doc_id UUID REFERENCES documents(doc_id),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
