# 📝 Real-Time Collaborative Document Editor

> Day 14 – Distributed Real-Time Systems

---

# 📌 Problem Statement

Design a collaborative document editor similar to Google Docs.

The system should allow:

- Multiple users editing the same document
- Real-time updates
- Version history
- Conflict resolution

---

# 🎯 Functional Requirements

- Create document
- Edit document
- Real-time collaboration
- View edit history
- Save document versions

---

# ⚙️ Non Functional Requirements

- Low latency updates
- High availability
- Conflict resolution
- Horizontal scalability

---

# 🧠 Core Concepts

✔ Operational Transformations (OT)  
✔ WebSocket communication  
✔ Event-driven updates  
✔ Document versioning  
✔ Distributed state management  

---

# 📊 High Level Architecture

Client Editor
 ↓
WebSocket Server
 ↓
Collaboration Service
 ↓
Document Storage
