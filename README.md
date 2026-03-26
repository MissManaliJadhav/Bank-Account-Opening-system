# Banking Account Opening System

This project is a multi-module banking application designed to automate the **Bank Account Opening Process**.  
The system integrates **Frontend UI, Python-based automation services, and Java-based core banking integration**.

---

## System Architecture

The system is divided into three major modules:

1. Frontend Module (User Interface & Data Capture)
2. Python Module (Verification, Processing & Automation)
3. Java Module (Core Business Logic & CBS Integration)

---

# 1. Frontend Module (User Interface & Data Capture)

This module handles the interaction between the **Bank Executive** and the **Customer**.

### Steps

**Step 1:**  
Customer visits the branch and requests to open a **Savings or Current Account**.  
(UI screen allows account type selection)

**Step 2:**  
Bank Executive asks the customer to fill the **Account Opening Form**.  
(UI renders the digital form)

**Step 3:**  
Customer fills the form with details such as:

- Nominee Details
- Mode of Operation
- Netbanking / Mobile / SMS Banking Registration
- Initial Funding Amount (cash, cheque, fund transfer)

**Step 4:**  
Customer uploads supporting documents:

- Aadhar Card
- PAN Card
- Driving License
- Ration Card

(File upload functionality with form submission)

---

# 2. Python Module (Verification, Processing & Automation)

This module handles **document processing, verification, and automation scripts**.

**Step 4a:**  
Uploaded documents are processed using **Optical Character Recognition (OCR)** to extract text automatically.

**Step 5:**  
Bank performs **KYC verification** using:

- Aadhar verification
- PAN verification
- AML Screening
- Negative List Screening

**Step 5a:**  
A **rules-based risk scoring system** checks the **initial funding amount and source** before account creation.

**Step 9a:**  
The system generates a **Personalized Digital Welcome Kit** as a secure PDF document.

**Step 10:**  
An **End-of-Day (EOD) batch process** verifies newly opened accounts and funding amounts against the **CBS database**.

---

# 3. Java Module (Core Business Logic & CBS Integration)

This module manages **database operations, transactions, and integration with the Core Banking System (CBS).**

**Step 6:**  
After successful verification, the system sends data to **CBS for account creation**.

**Step 7:**  
CBS generates:

- Customer ID
- Account ID
- Nominee Registration

**Step 8:**  
Initial funding amount is credited securely.

**Step 9:**  
Customer receives:

- Welcome Kit
- Passbook
- Cheque Book
- Debit Card
- Netbanking / Mobile Banking activation

---

## Technologies Used

Frontend  
- HTML  
- CSS  
- JavaScript  

Backend  
- Python (OCR, Automation)  
- Java (Core Banking Integration)

Database  
- MySQL / CBS Database

---

# Banking Account Opening System - Python Module

## Features
- OCR Document Processing
- KYC Verification
- AML Screening
- Risk Scoring Engine
- PostgreSQL Integration
- JWT Authentication

## APIs
POST /login  
POST /api/process-account  
GET /transactions  

## Run
pip install -r requirements.txt  
python app.py  
