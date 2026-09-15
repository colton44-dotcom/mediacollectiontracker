# Product Development Plan
## Media Collection Tracker

**Team:** Group 9
**Project Manager:** Gabriella
**Team Members:** Owen Roberts, Jemimah Apolinario, Alexandra Seay
**Version:** 1.0
**Date:** September 10, 2026

---

## 1. Product Overview

The **Media Collection Tracker** is a web application built with **Python** and the **Django framework** that allows users to organize and manage personal media collections — including movies, TV shows, books, music, and video games — in a single centralized platform. The product focuses on core collection management: account creation, secure login, and the ability to add, edit, delete, search, and categorize media items.

**Out of Scope:** External marketplace features and social networking capabilities.

---

## 2. Goals & Objectives

| # | Objective |
|---|-----------|
| 1 | Deliver a working Django web application for personal media collection management |
| 2 | Provide secure user authentication and personalized collections |
| 3 | Enable full CRUD (create, read, update, delete) on media items |
| 4 | Support search, filtering, and status tracking |
| 5 | Produce version-controlled source code, system documentation, and a functional UI |

---

## 3. Target Users

- **Primary:** Individuals who own and want to track personal media across multiple formats
- **User Needs:**
  - A single place to catalog owned media
  - Quick search and filtering to find items
  - Progress tracking (Not Started → In Progress → Completed)
  - Optional rating of media items

---

## 4. Key Features

| Feature | Description | Priority (MoSCoW) |
|---------|-------------|-------------------|
| User Registration & Login | Secure account creation and authentication via Django's auth system | Must |
| Media Management | Add, edit, delete, and categorize media items | Must |
| Search & Filtering | Search by title or category; filter collection | Must |
| Status Tracking | Mark media as Not Started, In Progress, or Completed | Should |
| Ratings | Rate media items within collections | Could |
| Reports | Collection summary and status reports | Should |

---

## 5. Development Approach

**Methodology:** Scrum

**Cadence:**
- Sprint planning meetings to assign tasks and define sprint goals
- Sprint reviews and retrospectives after each sprint

**Collaboration Tools:**
| Tool | Purpose |
|------|---------|
| GitHub | Source control & code change tracking |
| Microsoft Teams | Team meetings & communication |
| Google Drive | Shared documents, diagrams, and reports |

---

## 6. Sprint Roadmap

### Sprint 1 — Foundation
**Goal:** Project setup and authentication
- [ ] Project setup and repository creation
- [ ] Database design (User, MediaItem, Category entities)
- [ ] User authentication (registration, login, logout)
- [ ] Access control (users only see their own collections)

### Sprint 2 — Core Functionality
**Goal:** Media collection CRUD
- [ ] Add media items
- [ ] Edit media items
- [ ] Delete media items
- [ ] Category assignment

### Sprint 3 — Discovery & Tracking
**Goal:** Search, filtering, and status
- [ ] Search by title
- [ ] Search/filter by category
- [ ] Status tracking (Not Started / In Progress / Completed)
- [ ] Ratings (optional)

### Sprint 4 — Polish & Delivery
**Goal:** UI improvements, testing, and final prep
- [ ] User interface improvements
- [ ] Testing and debugging
- [ ] Reports (collection summary, status report)
- [ ] Final documentation and deliverable preparation

---

## 7. Requirements Summary

### Business Requirements
| ID | Description | MoSCoW |
|----|-------------|--------|
| BR1 | Users must be able to create, edit, delete, and categorize media items | M |
| BR2 | Users should be able to track media status (watched, reading, completed) | S |
| BR3 | Users could rate media items within their collections | C |

### User Requirements
| ID | Description | MoSCoW |
|----|-------------|--------|
| UR1 | Users must be able to register and log in securely | M |
| UR2 | Users must be able to add and manage media items | M |
| UR3 | Users should be able to search and filter collections | S |

### Functional Requirements
| ID | Description | MoSCoW |
|----|-------------|--------|
| FR1 | The system must allow user registration and authentication | M |
| FR2 | The system must allow users to add, edit, and delete media items | M |
| FR3 | The system must allow searching by title or category | M |

### Non-Functional Requirements
| ID | Description | MoSCoW |
|----|-------------|--------|
| NFR1 | User data must be protected using secure authentication and encryption | M |
| NFR2 | Pages should load within two seconds under normal conditions | S |

---

## 8. Use Cases

### UC1 — User Login
- **Actor:** Registered User
- **Precondition:** User has an active account
- **Main Flow:** User enters username and password → system verifies credentials → grants access
- **Alternate Flow:** Incorrect credentials display an error message
- **Postcondition:** User is authenticated and redirected to dashboard

### UC2 — Add Media Item
- **Actor:** Registered User
- **Precondition:** User must be logged in
- **Main Flow:** User selects Add Media → enters information → submits
- **Alternate Flow:** Missing required fields trigger an error message
- **Postcondition:** Media item is stored in the database

### UC3 — Search Collection
- **Actor:** Registered User
- **Precondition:** User must be logged in
- **Main Flow:** User enters search keyword → results are displayed
- **Alternate Flow:** System displays "No results found"
- **Postcondition:** User views search results

---

## 9. Architecture & Technical Design

### Architecture
- **Pattern:** Client–Server
- **Frontend:** Web browser interface communicating with backend
- **Backend:** Python Django framework (routing, business logic, auth, DB communication)
- **Database:** PostgreSQL or SQLite

### Core Entities
| Entity | Key Attributes |
|--------|----------------|
| **User** | user_id, username, email, password_hash |
| **MediaItem** | media_id, title, category, rating, status, user_id, category_id |
| **Category** | category_id, category_name |

### Data Flow
1. User submits media info via web interface
2. System validates input
3. System stores/retrieves data from database
4. Updated results are returned to the user interface

### Media Item States
`Not Started` → `In Progress` → `Completed`

### Security Requirements
- Django authentication system with hashed passwords
- Access control — users can only view/modify their own collections

### Hardware Requirements
- Server: minimum quad-core processor, 16 GB RAM
- Client: desktop, laptop, tablet, or smartphone with a modern browser
- Stable internet connection required

---

## 10. Assumptions & Dependencies

- Users have internet connectivity to access the web application
- Application depends on the Django framework
- Project relies on GitHub for version control and collaboration
- Requires a server capable of running Python and Django

---

## 11. Deliverables

- [ ] Working Django web application
- [ ] Version-controlled source code (GitHub)
- [ ] System documentation (SRS, diagrams, reports)
- [ ] Functional media collection management interface

---

## 12. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep beyond core features | Schedule slip | Enforce MoSCoW priorities; defer "Could" items |
| Team availability / coordination | Delayed sprints |  Clear task ownership |
| Learning curve on Django | Slower early progress | Front-load Sprint 1 setup; pair programming |
| Database design changes mid-project | Rework | Finalize ERD in Sprint 1; review before Sprint 2 |

---

## 13. Success Criteria

- All **Must** requirements implemented and tested
- Application deployable and accessible via modern web browser
- Users can register, log in, and fully manage their own media collections
- Page load times under two seconds under normal conditions
- All deliverables submitted and documented

---