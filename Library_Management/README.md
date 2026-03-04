# 📚 Library Pro  | Enterprise Edition

A high-end, professional Library Management System developed for *Internboot Projects. This system implements **Role-Based Access Control (RBAC)* and a secure *Admin Verification* workflow to ensure data integrity and physical book security.

---

## 🚀 Professional Features
* *Dual-Portal Access*: Dedicated interfaces for Administrators and Students with different permission levels.
* *Admin Verification Desk*: A security layer where Admins must "Approve" returns before a book's status reverts to "Available."
* *Advanced Real-time Filtering*: Instant search functionality across titles and authors with zero latency.
* *Automated Financial Logic*: Built-in fine calculator that applies a $10/day penalty for overdue resources.
* *Database Versioning*: Utilizes the library_v5.db schema for robust transaction logging and persistence.

---

## 📸 System Walkthrough

### 1. The Secure Login Portal
Featuring a modern, centered "Glassmorphism" design. New students can register themselves, while Admin access remains restricted.


### 2. Live Inventory Management
A clean, card-based dashboard showing the global book list. Statuses are color-coded:
* *Green*: Available for Issue.
* *Red*: Currently Issued to a student.
* *Yellow*: Pending Admin Approval (Returned but not yet verified).


### 3. Student Self-Service Workflow
Students can browse and "Issue" books directly. When returning, the system notifies the Admin instead of instantly clearing the record.


### 4. Admin Verification Desk (Security Layer)
The exclusive "Verification Desk" where Admins confirm the physical receipt of a book. This prevents students from falsely claiming a return.


---

## 🛠️ Installation & Setup
1. *Clone the Project*: Ensure main.py is in your local directory.
2. *Database Initialization*: If upgrading from an older version, delete any existing .db files to allow the v5.0 schema to generate.
3. *Execute*:
   ```bash
   python main.py