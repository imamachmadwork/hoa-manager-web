# Leasing Rental Application — Frontend bugs

- Generated: 2026-07-31 09:00 UTC
- Environment: https://roamstay.com
- Failing tests: 3

## test_list_and_detail_agree_on_unit_for_same_application[chromium]

- Status: `failed`
- Full name: `tests.e2e.test_leasing_rental_application#test_list_and_detail_agree_on_unit_for_same_application`

**Error**
```
AssertionError: Locator expected to be visible
Actual value: None
Error: element(s) not found 
Call log:
  - Expect "to_be_visible" with timeout 10000ms
  - waiting for locator("table").first.locator("tr").filter(has_text="Applicant 1785488333929")

Aria snapshot:
- paragraph: Create New
- img "Remove Icon"
- paragraph: Contacts
- img "Customer Account Icon"
- paragraph: Customer Account
- img "Tenant Icon"
- paragraph: Tenant
- img "Owner Icon"
- paragraph: Owner
- img "Vendor Icon"
- paragraph: Vendor
- img "Employee Icon"
- paragraph: Employee
- paragraph: Tasks & Maintenance
- img "Task Icon"
- paragraph: Task
- img "Work Order Icon"
- paragraph: Work Order
- paragraph: Vendor Transactions
- img "Create Invoice Icon"
- paragraph: Create Invoice
- img "Pay Invoices Icon"
- paragraph: Pay Invoices
- img "Vendor Credit Icon"
- paragraph: Vendor Credit
- paragraph: Customer Transactions
- img "Create Charge Icon"
- paragraph: Create Charge
- img "Receive Payment Icon"
- paragraph: Receive Payment
- img "Credit Memo Icon"
- paragraph: Credit Memo
- img "Quick Charge Icon"
- paragraph: Quick Charge
- paragraph: Other Transactions
- img "Journal Entry Icon"
- paragraph: Journal Entry
- img "Bank Transfer Icon"
- paragraph: Bank Transfer
- img "Bank Deposit Icon"
- paragraph: Bank Deposit
- img "Check Icon"
- paragraph: Check
- paragraph: Reporting
- img "Violation Icon"
- paragraph: Violation
- img "Modification Icon"
- paragraph: Modification
- img "Inspection Icon"
- paragraph: Inspection
- img "Motion Icon"
- paragraph: Motion
- img "Meeting Icon"
- paragraph: Meeting
- img "Election Icon"
- paragraph: Election
- paragraph: Properties
- img "Association Icon"
- paragraph: Association
- img "Unit Icon"
- paragraph: Unit
- paragraph: Communications
- img "Announcement Icon"
- paragraph: Announcement
- button "Liberty Community Management Inc":
  - img "Liberty Community Management Inc"
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- img
- heading "Leasing" [level=5]
- menuitem "Active Leases":
  - paragraph: Active Leases
- menuitem "Lease Renewals":
  - paragraph: Lease Renewals
- menuitem "Rental Applications":
  - paragraph: Rental Applications
- menuitem "Draft Leases":
  - paragraph: Draft Leases
- menuitem "Unit Sales":
  - paragraph: Unit Sales
- menuitem "Move In/Out":
  - paragraph: Move In/Out
- textbox "Search Roam"
- img "search"
- combobox "Elisa Miller":
  - text: Elisa Miller
  - img
- button
- combobox "Chattahoochee Reserve":
  - text: Chattahoochee Reserve
  - img
- button
- button "Notifications": "2"
- button "Switch to dark mode"
- img "image"
- banner:
  - heading "Rental Applications" [level=1]
- button "Undecided 114":
  - paragraph: Undecided
  - paragraph: "114"
- button "All Applications 114" [pressed]:
  - paragraph: All Applications
  - paragraph: "114"
- button "Name":
  - paragraph: Name
- button "Status":
  - paragraph: Status
- button "Units":
  - paragraph: Units
- button "Move In Date":
  - paragraph: Move In Date
- button "Contact":
  - paragraph: Contact
- button "All Filters"
- button "Reset"
- table:
  - rowgroup:
    - row "Name Association Move In Date Contact Last Updated Action Select all rows":
      - columnheader "Name":
        - button "Name"
      - columnheader "Association":
        - button "Association"
      - columnheader "Move In Date":
        - button "Move In Date"
      - columnheader "Contact":
        - button "Contact"
      - columnheader "Last Updated":
        - button "Last Updated"
      - columnheader "Action"
      - columnheader "Select all rows":
        - checkbox "Select all rows"
  - rowgroup:
    - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170527 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170527@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170527@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170944 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170944@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170944@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613207486 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613207486@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613207486@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613208441 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613208441@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613208441@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613279983 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613279983@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613279983@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
      - cell "QA API Applicant 1784699556687 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699556687@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699556687@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
      - cell "QA API Applicant 1784699557430 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699557430@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699557430@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699602883 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699602883@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699602883@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699604171 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699604171@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699604171@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699693148 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699693148@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699693148@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784786177651 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786177651@example.com 07/23/2026":
      - cell "QA API Applicant 1784786177651 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784786177651@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784786177651@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784786178641 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786178641@example.com 07/23/2026":
      - cell "QA API Applicant 1784786178641 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784786178641@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784786178641@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786226851 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786226851@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786226851 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786226851@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786226851@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786228778 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786228778@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786228778 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786228778@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786228778@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786341914 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786341914@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786341914 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786341914@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786341914@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784872304313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304313@example.com 07/24/2026":
      - cell "QA API Applicant 1784872304313 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784872304313@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784872304313@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784872304674 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304674@example.com 07/24/2026":
      - cell "QA API Applicant 1784872304674 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784872304674@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784872304674@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872334666 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872334666@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872334666 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872334666@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872334666@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872345532 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872345532@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872345532 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872345532@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872345532@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872416193 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872416193@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872416193 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872416193@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872416193@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784958264992 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958264992@example.com 07/25/2026":
      - cell "QA API Applicant 1784958264992 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784958264992@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784958264992@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784958265686 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958265686@example.com 07/25/2026":
      - cell "QA API Applicant 1784958265686 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784958265686@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784958265686@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958300566 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958300566@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958300566 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958300566@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958300566@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958311698 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958311698@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958311698 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958311698@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958311698@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958381154 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958381154@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958381154 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958381154@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958381154@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785046064823 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046064823@example.com 07/26/2026":
      - cell "QA API Applicant 1785046064823 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785046064823@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785046064823@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785046065302 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046065302@example.com 07/26/2026":
      - cell "QA API Applicant 1785046065302 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785046065302@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785046065302@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046094192 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046094192@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046094192 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046094192@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046094192@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046105062 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046105062@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046105062 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046105062@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046105062@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046178688 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046178688@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046178688 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046178688@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046178688@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785133937409 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133937409@example.com 07/27/2026":
      - cell "QA API Applicant 1785133937409 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785133937409@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785133937409@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785133938549 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133938549@example.com 07/27/2026":
      - cell "QA API Applicant 1785133938549 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785133938549@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785133938549@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785133986958 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133986958@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785133986958 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785133986958@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785133986958@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785133998546 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133998546@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785133998546 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785133998546@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785133998546@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785134075900 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785134075900@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785134075900 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785134075900@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785134075900@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785158325923 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158325923@example.com 07/27/2026":
      - cell "QA API Applicant 1785158325923 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785158325923@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785158325923@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785158335121 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158335121@example.com 07/27/2026":
      - cell "QA API Applicant 1785158335121 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785158335121@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785158335121@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785158425414 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158425414@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785158425414 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785158425414@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785158425414@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785158438554 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158438554@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785158438554 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785158438554@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785158438554@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA Repro Repro 1785160512499 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160512499@example.com 07/27/2026":
      - cell "QA Repro Repro 1785160512499 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785160512499@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785160512499@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA Repro Repro 1785160567000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160567000@example.com 07/27/2026":
      - cell "QA Repro Repro 1785160567000 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785160567000@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785160567000@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785164719979 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164719979@example.com 07/27/2026":
      - cell "QA API Applicant 1785164719979 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785164719979@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785164719979@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785164723734 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164723734@example.com 07/27/2026":
      - cell "QA API Applicant 1785164723734 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785164723734@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785164723734@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785164854132 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164854132@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785164854132 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785164854132@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785164854132@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785164867373 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164867373@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785164867373 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785164867373@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785164867373@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785165012230 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785165012230@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785165012230 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785165012230@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785165012230@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785166543175 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166543175@example.com 07/27/2026":
      - cell "QA API Applicant 1785166543175 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785166543175@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785166543175@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785166546932 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166546932@example.com 07/27/2026":
      - cell "QA API Applicant 1785166546932 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785166546932@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785166546932@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785166674683 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166674683@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785166674683 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785166674683@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785166674683@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785166687871 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166687871@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785166687871 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785166687871@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785166687871@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785174639249 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174639249@example.com 07/28/2026":
      - cell "QA API Applicant 1785174639249 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785174639249@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785174639249@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785174643052 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174643052@example.com 07/28/2026":
      - cell "QA API Applicant 1785174643052 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785174643052@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785174643052@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174923682 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174923682@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174923682 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174923682@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174923682@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174937000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174937000@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174937000 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174937000@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174937000@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174967174 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174967174@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174967174 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174967174@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174967174@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785175131036 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785175131036@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785175131036 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785175131036@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785175131036@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785176312043 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176312043@example.com 07/28/2026":
      - cell "QA API Applicant 1785176312043 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785176312043@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785176312043@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785176316755 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176316755@example.com 07/28/2026":
      - cell "QA API Applicant 1785176316755 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785176316755@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785176316755@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176590785 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176590785@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176590785 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176590785@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176590785@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176603974 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176603974@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176603974 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176603974@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176603974@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176635179 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176635179@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176635179 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176635179@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176635179@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785181251452 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785181251452@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785181251452 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785181251452@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785181251452@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181304118 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181304118@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181304118 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181304118@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181304118@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181370726 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181370726@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181370726 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181370726@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181370726@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181411009 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181411009@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181411009 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181411009@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181411009@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182151843 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182151843@example.com 07/28/2026":
      - cell "QA API Applicant 1785182151843 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182151843@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182151843@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182159475 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182159475@example.com 07/28/2026":
      - cell "QA API Applicant 1785182159475 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182159475@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182159475@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182214657 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182214657@example.com 07/28/2026":
      - cell "QA API Applicant 1785182214657 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182214657@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182214657@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182219645 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182219645@example.com 07/28/2026":
      - cell "QA API Applicant 1785182219645 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182219645@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182219645@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182492367 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182492367@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182492367 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182492367@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182492367@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182505448 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182505448@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182505448 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182505448@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182505448@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182537747 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182537747@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182537747 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182537747@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182537747@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785217653318 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217653318@example.com 07/28/2026":
      - cell "QA API Applicant 1785217653318 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785217653318@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785217653318@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785217654270 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217654270@example.com 07/28/2026":
      - cell "QA API Applicant 1785217654270 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785217654270@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785217654270@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217690764 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217690764@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217690764 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217690764@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217690764@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217702084 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217702084@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217702084 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217702084@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217702084@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217779706 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217779706@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217779706 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217779706@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217779706@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785304444431 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304444431@example.com 07/29/2026":
      - cell "QA API Applicant 1785304444431 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785304444431@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785304444431@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785304445681 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304445681@example.com 07/29/2026":
      - cell "QA API Applicant 1785304445681 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785304445681@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785304445681@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304487313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304487313@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304487313 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304487313@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304487313@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304498813 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304498813@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304498813 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304498813@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304498813@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304594738 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304594738@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304594738 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304594738@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304594738@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785390174241 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390174241@example.com 07/30/2026":
      - cell "QA API Applicant 1785390174241 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785390174241@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785390174241@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785390175454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390175454@example.com 07/30/2026":
      - cell "QA API Applicant 1785390175454 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785390175454@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785390175454@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390219454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390219454@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390219454 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390219454@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390219454@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390221758 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390221758@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390221758 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390221758@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390221758@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390292125 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390292125@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390292125 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390292125@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390292125@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785428010606 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428010606@example.com 07/30/2026":
      - cell "QA API Applicant 1785428010606 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785428010606@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785428010606@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785428014187 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428014187@example.com 07/30/2026":
      - cell "QA API Applicant 1785428014187 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785428014187@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785428014187@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428283661 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428283661@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428283661 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428283661@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428283661@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428288741 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428288741@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428288741 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428288741@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428288741@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428319604 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428319604@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428319604 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428319604@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428319604@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785478548455 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548455@example.com 07/31/2026":
      - cell "QA API Applicant 1785478548455 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785478548455@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785478548455@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785478548841 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548841@example.com 07/31/2026":
      - cell "QA API Applicant 1785478548841 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785478548841@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785478548841@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478578511 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478578511@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478578511 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478578511@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478578511@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478580023 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478580023@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478580023 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478580023@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478580023@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478669408 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478669408@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478669408 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478669408@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478669408@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785481995802 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481995802@example.com 07/31/2026":
      - cell "QA API Applicant 1785481995802 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785481995802@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785481995802@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785481999622 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481999622@example.com 07/31/2026":
      - cell "QA API Applicant 1785481999622 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785481999622@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785481999622@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785482277264 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785482277264@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785482277264 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785482277264@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785482277264@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
- group:
  - text: "Items per page:"
  - combobox "100 Items per page:": "100"
  - text: 1 – 100 of 114
  - button "Previous page" [disabled]
  - button "Next page"
- text: "> Quick Action"
- img "plus"
- text: Add Application
- complementary:
  - img
- img
```

<details><summary>Trace</summary>

```
signed_in_rental_applications_page = <pages.rental_application_page.RentalApplicationPage object at 0x107daa550>
seeded_rental_application = {'application': {'propertyId': '12613aac-76b8-4d64-a6ca-c388ff1cd438', 'userId': '8e2328b0-0611-4ffe-afd9-84abd0b1eb35...d': '1954dea7-2fbf-492d-82e5-a74e2118cc3e', ...}, 'unit_name': '3505 Adams Road', 'assigned_user_name': 'Jane Manager'}

    @pytest.mark.known_bug
    @allure.tag("known-bug")
    def test_list_and_detail_agree_on_unit_for_same_application(
        signed_in_rental_applications_page, seeded_rental_application
    ):
        """Known bug: the list row and detail page for the same application can
        show different units. Observed for one application: detail page said
        "Lot 14" while the list row for that identical application (matched by
        unique applicant name/email) showed "3738 Reserve Overlook". This
        asserts both views should agree on the unit, using the detail page's
        value (from GET /pms/applications/{id}) as the source of truth.
        """
        rental_page = signed_in_rental_applications_page
        application = seeded_rental_application["application"]
        unit_name = seeded_rental_application["unit_name"]
    
        rental_page.all_applications_tab.click()
        rental_page.page.get_by_role("combobox", name="Items per page:").click()
        rental_page.page.get_by_role("option", name="100", exact=True).click()
    
        row = rental_page.table.locator("tr", has_text=application["lastName"])
>       expect(row).to_be_visible(timeout=10000)
E       AssertionError: Locator expected to be visible
E       Actual value: None
E       Error: element(s) not found 
E       Call log:
E         - Expect "to_be_visible" with timeout 10000ms
E         - waiting for locator("table").first.locator("tr").filter(has_text="Applicant 1785488333929")
E       
E       Aria snapshot:
E       - paragraph: Create New
E       - img "Remove Icon"
E       - paragraph: Contacts
E       - img "Customer Account Icon"
E       - paragraph: Customer Account
E       - img "Tenant Icon"
E       - paragraph: Tenant
E       - img "Owner Icon"
E       - paragraph: Owner
E       - img "Vendor Icon"
E       - paragraph: Vendor
E       - img "Employee Icon"
E       - paragraph: Employee
E       - paragraph: Tasks & Maintenance
E       - img "Task Icon"
E       - paragraph: Task
E       - img "Work Order Icon"
E       - paragraph: Work Order
E       - paragraph: Vendor Transactions
E       - img "Create Invoice Icon"
E       - paragraph: Create Invoice
E       - img "Pay Invoices Icon"
E       - paragraph: Pay Invoices
E       - img "Vendor Credit Icon"
E       - paragraph: Vendor Credit
E       - paragraph: Customer Transactions
E       - img "Create Charge Icon"
E       - paragraph: Create Charge
E       - img "Receive Payment Icon"
E       - paragraph: Receive Payment
E       - img "Credit Memo Icon"
E       - paragraph: Credit Memo
E       - img "Quick Charge Icon"
E       - paragraph: Quick Charge
E       - paragraph: Other Transactions
E       - img "Journal Entry Icon"
E       - paragraph: Journal Entry
E       - img "Bank Transfer Icon"
E       - paragraph: Bank Transfer
E       - img "Bank Deposit Icon"
E       - paragraph: Bank Deposit
E       - img "Check Icon"
E       - paragraph: Check
E       - paragraph: Reporting
E       - img "Violation Icon"
E       - paragraph: Violation
E       - img "Modification Icon"
E       - paragraph: Modification
E       - img "Inspection Icon"
E       - paragraph: Inspection
E       - img "Motion Icon"
E       - paragraph: Motion
E       - img "Meeting Icon"
E       - paragraph: Meeting
E       - img "Election Icon"
E       - paragraph: Election
E       - paragraph: Properties
E       - img "Association Icon"
E       - paragraph: Association
E       - img "Unit Icon"
E       - paragraph: Unit
E       - paragraph: Communications
E       - img "Announcement Icon"
E       - paragraph: Announcement
E       - button "Liberty Community Management Inc":
E         - img "Liberty Community Management Inc"
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - img
E       - heading "Leasing" [level=5]
E       - menuitem "Active Leases":
E         - paragraph: Active Leases
E       - menuitem "Lease Renewals":
E         - paragraph: Lease Renewals
E       - menuitem "Rental Applications":
E         - paragraph: Rental Applications
E       - menuitem "Draft Leases":
E         - paragraph: Draft Leases
E       - menuitem "Unit Sales":
E         - paragraph: Unit Sales
E       - menuitem "Move In/Out":
E         - paragraph: Move In/Out
E       - textbox "Search Roam"
E       - img "search"
E       - combobox "Elisa Miller":
E         - text: Elisa Miller
E         - img
E       - button
E       - combobox "Chattahoochee Reserve":
E         - text: Chattahoochee Reserve
E         - img
E       - button
E       - button "Notifications": "2"
E       - button "Switch to dark mode"
E       - img "image"
E       - banner:
E         - heading "Rental Applications" [level=1]
E       - button "Undecided 114":
E         - paragraph: Undecided
E         - paragraph: "114"
E       - button "All Applications 114" [pressed]:
E         - paragraph: All Applications
E         - paragraph: "114"
E       - button "Name":
E         - paragraph: Name
E       - button "Status":
E         - paragraph: Status
E       - button "Units":
E         - paragraph: Units
E       - button "Move In Date":
E         - paragraph: Move In Date
E       - button "Contact":
E         - paragraph: Contact
E       - button "All Filters"
E       - button "Reset"
E       - table:
E         - rowgroup:
E           - row "Name Association Move In Date Contact Last Updated Action Select all rows":
E             - columnheader "Name":
E               - button "Name"
E             - columnheader "Association":
E               - button "Association"
E             - columnheader "Move In Date":
E               - button "Move In Date"
E             - columnheader "Contact":
E               - button "Contact"
E             - columnheader "Last Updated":
E               - button "Last Updated"
E             - columnheader "Action"
E             - columnheader "Select all rows":
E               - checkbox "Select all rows"
E         - rowgroup:
E           - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170527 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170527@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170527@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170944 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170944@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170944@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613207486 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613207486@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613207486@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613208441 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613208441@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613208441@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613279983 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613279983@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613279983@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699556687 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699556687@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699556687@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699557430 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699557430@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699557430@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699602883 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699602883@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699602883@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699604171 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699604171@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699604171@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699693148 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699693148@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699693148@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784786177651 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786177651@example.com 07/23/2026":
E             - cell "QA API Applicant 1784786177651 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784786177651@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784786177651@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784786178641 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786178641@example.com 07/23/2026":
E             - cell "QA API Applicant 1784786178641 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784786178641@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784786178641@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786226851 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786226851@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786226851 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786226851@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786226851@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786228778 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786228778@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786228778 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786228778@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786228778@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786341914 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786341914@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786341914 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786341914@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786341914@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784872304313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304313@example.com 07/24/2026":
E             - cell "QA API Applicant 1784872304313 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784872304313@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784872304313@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784872304674 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304674@example.com 07/24/2026":
E             - cell "QA API Applicant 1784872304674 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784872304674@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784872304674@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872334666 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872334666@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872334666 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872334666@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872334666@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872345532 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872345532@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872345532 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872345532@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872345532@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872416193 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872416193@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872416193 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872416193@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872416193@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784958264992 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958264992@example.com 07/25/2026":
E             - cell "QA API Applicant 1784958264992 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784958264992@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784958264992@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784958265686 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958265686@example.com 07/25/2026":
E             - cell "QA API Applicant 1784958265686 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784958265686@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784958265686@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958300566 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958300566@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958300566 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958300566@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958300566@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958311698 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958311698@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958311698 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958311698@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958311698@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958381154 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958381154@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958381154 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958381154@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958381154@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785046064823 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046064823@example.com 07/26/2026":
E             - cell "QA API Applicant 1785046064823 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785046064823@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785046064823@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785046065302 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046065302@example.com 07/26/2026":
E             - cell "QA API Applicant 1785046065302 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785046065302@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785046065302@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046094192 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046094192@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046094192 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046094192@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046094192@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046105062 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046105062@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046105062 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046105062@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046105062@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046178688 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046178688@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046178688 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046178688@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046178688@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785133937409 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133937409@example.com 07/27/2026":
E             - cell "QA API Applicant 1785133937409 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785133937409@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785133937409@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785133938549 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133938549@example.com 07/27/2026":
E             - cell "QA API Applicant 1785133938549 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785133938549@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785133938549@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785133986958 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133986958@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785133986958 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785133986958@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785133986958@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785133998546 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133998546@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785133998546 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785133998546@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785133998546@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785134075900 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785134075900@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785134075900 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785134075900@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785134075900@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785158325923 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158325923@example.com 07/27/2026":
E             - cell "QA API Applicant 1785158325923 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785158325923@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785158325923@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785158335121 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158335121@example.com 07/27/2026":
E             - cell "QA API Applicant 1785158335121 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785158335121@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785158335121@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785158425414 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158425414@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785158425414 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785158425414@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785158425414@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785158438554 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158438554@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785158438554 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785158438554@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785158438554@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA Repro Repro 1785160512499 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160512499@example.com 07/27/2026":
E             - cell "QA Repro Repro 1785160512499 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785160512499@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785160512499@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA Repro Repro 1785160567000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160567000@example.com 07/27/2026":
E             - cell "QA Repro Repro 1785160567000 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785160567000@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785160567000@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785164719979 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164719979@example.com 07/27/2026":
E             - cell "QA API Applicant 1785164719979 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785164719979@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785164719979@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785164723734 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164723734@example.com 07/27/2026":
E             - cell "QA API Applicant 1785164723734 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785164723734@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785164723734@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785164854132 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164854132@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785164854132 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785164854132@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785164854132@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785164867373 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164867373@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785164867373 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785164867373@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785164867373@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785165012230 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785165012230@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785165012230 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785165012230@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785165012230@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785166543175 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166543175@example.com 07/27/2026":
E             - cell "QA API Applicant 1785166543175 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785166543175@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785166543175@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785166546932 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166546932@example.com 07/27/2026":
E             - cell "QA API Applicant 1785166546932 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785166546932@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785166546932@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785166674683 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166674683@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785166674683 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785166674683@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785166674683@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785166687871 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166687871@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785166687871 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785166687871@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785166687871@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785174639249 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174639249@example.com 07/28/2026":
E             - cell "QA API Applicant 1785174639249 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785174639249@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785174639249@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785174643052 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174643052@example.com 07/28/2026":
E             - cell "QA API Applicant 1785174643052 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785174643052@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785174643052@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174923682 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174923682@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174923682 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174923682@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174923682@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174937000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174937000@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174937000 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174937000@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174937000@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174967174 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174967174@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174967174 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174967174@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174967174@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785175131036 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785175131036@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785175131036 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785175131036@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785175131036@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785176312043 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176312043@example.com 07/28/2026":
E             - cell "QA API Applicant 1785176312043 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785176312043@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785176312043@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785176316755 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176316755@example.com 07/28/2026":
E             - cell "QA API Applicant 1785176316755 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785176316755@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785176316755@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176590785 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176590785@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176590785 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176590785@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176590785@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176603974 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176603974@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176603974 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176603974@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176603974@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176635179 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176635179@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176635179 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176635179@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176635179@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785181251452 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785181251452@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785181251452 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785181251452@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785181251452@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181304118 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181304118@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181304118 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181304118@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181304118@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181370726 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181370726@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181370726 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181370726@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181370726@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181411009 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181411009@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181411009 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181411009@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181411009@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182151843 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182151843@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182151843 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182151843@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182151843@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182159475 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182159475@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182159475 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182159475@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182159475@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182214657 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182214657@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182214657 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182214657@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182214657@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182219645 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182219645@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182219645 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182219645@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182219645@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182492367 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182492367@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182492367 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182492367@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182492367@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182505448 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182505448@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182505448 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182505448@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182505448@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182537747 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182537747@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182537747 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182537747@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182537747@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785217653318 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217653318@example.com 07/28/2026":
E             - cell "QA API Applicant 1785217653318 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785217653318@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785217653318@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785217654270 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217654270@example.com 07/28/2026":
E             - cell "QA API Applicant 1785217654270 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785217654270@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785217654270@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217690764 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217690764@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217690764 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217690764@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217690764@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217702084 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217702084@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217702084 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217702084@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217702084@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217779706 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217779706@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217779706 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217779706@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217779706@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785304444431 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304444431@example.com 07/29/2026":
E             - cell "QA API Applicant 1785304444431 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785304444431@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785304444431@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785304445681 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304445681@example.com 07/29/2026":
E             - cell "QA API Applicant 1785304445681 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785304445681@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785304445681@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304487313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304487313@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304487313 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304487313@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304487313@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304498813 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304498813@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304498813 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304498813@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304498813@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304594738 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304594738@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304594738 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304594738@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304594738@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785390174241 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390174241@example.com 07/30/2026":
E             - cell "QA API Applicant 1785390174241 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785390174241@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785390174241@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785390175454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390175454@example.com 07/30/2026":
E             - cell "QA API Applicant 1785390175454 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785390175454@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785390175454@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390219454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390219454@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390219454 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390219454@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390219454@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390221758 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390221758@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390221758 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390221758@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390221758@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390292125 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390292125@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390292125 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390292125@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390292125@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785428010606 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428010606@example.com 07/30/2026":
E             - cell "QA API Applicant 1785428010606 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785428010606@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785428010606@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785428014187 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428014187@example.com 07/30/2026":
E             - cell "QA API Applicant 1785428014187 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785428014187@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785428014187@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428283661 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428283661@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428283661 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428283661@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428283661@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428288741 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428288741@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428288741 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428288741@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428288741@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428319604 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428319604@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428319604 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428319604@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428319604@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785478548455 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548455@example.com 07/31/2026":
E             - cell "QA API Applicant 1785478548455 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785478548455@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785478548455@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785478548841 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548841@example.com 07/31/2026":
E             - cell "QA API Applicant 1785478548841 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785478548841@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785478548841@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478578511 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478578511@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478578511 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478578511@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478578511@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478580023 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478580023@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478580023 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478580023@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478580023@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478669408 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478669408@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478669408 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478669408@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478669408@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785481995802 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481995802@example.com 07/31/2026":
E             - cell "QA API Applicant 1785481995802 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785481995802@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785481995802@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785481999622 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481999622@example.com 07/31/2026":
E             - cell "QA API Applicant 1785481999622 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785481999622@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785481999622@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785482277264 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785482277264@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785482277264 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785482277264@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785482277264@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E       - group:
E         - text: "Items per page:"
E         - combobox "100 Items per page:": "100"
E         - text: 1 – 100 of 114
E         - button "Previous page" [disabled]
E         - button "Next page"
E       - text: "> Quick Action"
E       - img "plus"
E       - text: Add Application
E       - complementary:
E         - img
E       - img

tests/e2e/test_leasing_rental_application.py:137: AssertionError
```

</details>

Screenshots/videos/traces for this run are in the `test-results/` or `playwright-artifacts` CI artifact.

---

## test_created_application_appears_correctly_in_list[chromium]

- Status: `failed`
- Full name: `tests.e2e.test_leasing_rental_application#test_created_application_appears_correctly_in_list`

**Error**
```
AssertionError: Locator expected to be visible
Actual value: None
Error: element(s) not found 
Call log:
  - Expect "to_be_visible" with timeout 10000ms
  - waiting for locator("table").first.locator("tr").filter(has_text="Applicant 1785488290919")

Aria snapshot:
- paragraph: Create New
- img "Remove Icon"
- paragraph: Contacts
- img "Customer Account Icon"
- paragraph: Customer Account
- img "Tenant Icon"
- paragraph: Tenant
- img "Owner Icon"
- paragraph: Owner
- img "Vendor Icon"
- paragraph: Vendor
- img "Employee Icon"
- paragraph: Employee
- paragraph: Tasks & Maintenance
- img "Task Icon"
- paragraph: Task
- img "Work Order Icon"
- paragraph: Work Order
- paragraph: Vendor Transactions
- img "Create Invoice Icon"
- paragraph: Create Invoice
- img "Pay Invoices Icon"
- paragraph: Pay Invoices
- img "Vendor Credit Icon"
- paragraph: Vendor Credit
- paragraph: Customer Transactions
- img "Create Charge Icon"
- paragraph: Create Charge
- img "Receive Payment Icon"
- paragraph: Receive Payment
- img "Credit Memo Icon"
- paragraph: Credit Memo
- img "Quick Charge Icon"
- paragraph: Quick Charge
- paragraph: Other Transactions
- img "Journal Entry Icon"
- paragraph: Journal Entry
- img "Bank Transfer Icon"
- paragraph: Bank Transfer
- img "Bank Deposit Icon"
- paragraph: Bank Deposit
- img "Check Icon"
- paragraph: Check
- paragraph: Reporting
- img "Violation Icon"
- paragraph: Violation
- img "Modification Icon"
- paragraph: Modification
- img "Inspection Icon"
- paragraph: Inspection
- img "Motion Icon"
- paragraph: Motion
- img "Meeting Icon"
- paragraph: Meeting
- img "Election Icon"
- paragraph: Election
- paragraph: Properties
- img "Association Icon"
- paragraph: Association
- img "Unit Icon"
- paragraph: Unit
- paragraph: Communications
- img "Announcement Icon"
- paragraph: Announcement
- button "Liberty Community Management Inc":
  - img "Liberty Community Management Inc"
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- img
- heading "Leasing" [level=5]
- menuitem "Active Leases":
  - paragraph: Active Leases
- menuitem "Lease Renewals":
  - paragraph: Lease Renewals
- menuitem "Rental Applications":
  - paragraph: Rental Applications
- menuitem "Draft Leases":
  - paragraph: Draft Leases
- menuitem "Unit Sales":
  - paragraph: Unit Sales
- menuitem "Move In/Out":
  - paragraph: Move In/Out
- textbox "Search Roam"
- img "search"
- combobox "Elisa Miller":
  - text: Elisa Miller
  - img
- button
- combobox "Chattahoochee Reserve":
  - text: Chattahoochee Reserve
  - img
- button
- button "Notifications": "2"
- button "Switch to dark mode"
- img "image"
- banner:
  - heading "Rental Applications" [level=1]
- button "Undecided 112":
  - paragraph: Undecided
  - paragraph: "112"
- button "All Applications 112" [pressed]:
  - paragraph: All Applications
  - paragraph: "112"
- button "Name":
  - paragraph: Name
- button "Status":
  - paragraph: Status
- button "Units":
  - paragraph: Units
- button "Move In Date":
  - paragraph: Move In Date
- button "Contact":
  - paragraph: Contact
- button "All Filters"
- button "Reset"
- table:
  - rowgroup:
    - row "Name Association Move In Date Contact Last Updated Action Select all rows":
      - columnheader "Name":
        - button "Name"
      - columnheader "Association":
        - button "Association"
      - columnheader "Move In Date":
        - button "Move In Date"
      - columnheader "Contact":
        - button "Contact"
      - columnheader "Last Updated":
        - button "Last Updated"
      - columnheader "Action"
      - columnheader "Select all rows":
        - checkbox "Select all rows"
  - rowgroup:
    - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170527 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170527@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170527@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170944 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170944@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170944@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613207486 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613207486@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613207486@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613208441 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613208441@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613208441@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613279983 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613279983@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613279983@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
      - cell "QA API Applicant 1784699556687 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699556687@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699556687@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
      - cell "QA API Applicant 1784699557430 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699557430@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699557430@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699602883 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699602883@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699602883@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699604171 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699604171@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699604171@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699693148 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699693148@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699693148@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784786177651 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786177651@example.com 07/23/2026":
      - cell "QA API Applicant 1784786177651 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784786177651@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784786177651@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784786178641 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786178641@example.com 07/23/2026":
      - cell "QA API Applicant 1784786178641 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784786178641@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784786178641@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786226851 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786226851@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786226851 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786226851@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786226851@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786228778 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786228778@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786228778 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786228778@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786228778@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784786341914 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786341914@example.com 07/23/2026":
      - cell "QA E2E Applicant 1784786341914 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784786341914@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784786341914@example.com
      - cell "07/23/2026":
        - paragraph: 07/23/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784872304313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304313@example.com 07/24/2026":
      - cell "QA API Applicant 1784872304313 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784872304313@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784872304313@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784872304674 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304674@example.com 07/24/2026":
      - cell "QA API Applicant 1784872304674 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784872304674@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784872304674@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872334666 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872334666@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872334666 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872334666@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872334666@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872345532 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872345532@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872345532 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872345532@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872345532@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784872416193 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872416193@example.com 07/24/2026":
      - cell "QA E2E Applicant 1784872416193 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784872416193@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784872416193@example.com
      - cell "07/24/2026":
        - paragraph: 07/24/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784958264992 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958264992@example.com 07/25/2026":
      - cell "QA API Applicant 1784958264992 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784958264992@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784958264992@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784958265686 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958265686@example.com 07/25/2026":
      - cell "QA API Applicant 1784958265686 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784958265686@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784958265686@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958300566 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958300566@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958300566 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958300566@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958300566@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958311698 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958311698@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958311698 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958311698@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958311698@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784958381154 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958381154@example.com 07/25/2026":
      - cell "QA E2E Applicant 1784958381154 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784958381154@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784958381154@example.com
      - cell "07/25/2026":
        - paragraph: 07/25/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785046064823 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046064823@example.com 07/26/2026":
      - cell "QA API Applicant 1785046064823 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785046064823@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785046064823@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785046065302 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046065302@example.com 07/26/2026":
      - cell "QA API Applicant 1785046065302 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785046065302@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785046065302@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046094192 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046094192@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046094192 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046094192@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046094192@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046105062 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046105062@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046105062 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046105062@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046105062@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785046178688 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046178688@example.com 07/26/2026":
      - cell "QA E2E Applicant 1785046178688 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785046178688@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785046178688@example.com
      - cell "07/26/2026":
        - paragraph: 07/26/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785133937409 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133937409@example.com 07/27/2026":
      - cell "QA API Applicant 1785133937409 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785133937409@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785133937409@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785133938549 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133938549@example.com 07/27/2026":
      - cell "QA API Applicant 1785133938549 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785133938549@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785133938549@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785133986958 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133986958@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785133986958 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785133986958@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785133986958@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785133998546 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133998546@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785133998546 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785133998546@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785133998546@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785134075900 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785134075900@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785134075900 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785134075900@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785134075900@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785158325923 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158325923@example.com 07/27/2026":
      - cell "QA API Applicant 1785158325923 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785158325923@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785158325923@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785158335121 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158335121@example.com 07/27/2026":
      - cell "QA API Applicant 1785158335121 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785158335121@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785158335121@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785158425414 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158425414@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785158425414 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785158425414@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785158425414@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785158438554 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158438554@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785158438554 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785158438554@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785158438554@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA Repro Repro 1785160512499 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160512499@example.com 07/27/2026":
      - cell "QA Repro Repro 1785160512499 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785160512499@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785160512499@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA Repro Repro 1785160567000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160567000@example.com 07/27/2026":
      - cell "QA Repro Repro 1785160567000 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785160567000@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785160567000@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785164719979 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164719979@example.com 07/27/2026":
      - cell "QA API Applicant 1785164719979 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785164719979@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785164719979@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785164723734 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164723734@example.com 07/27/2026":
      - cell "QA API Applicant 1785164723734 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785164723734@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785164723734@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785164854132 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164854132@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785164854132 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785164854132@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785164854132@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785164867373 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164867373@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785164867373 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785164867373@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785164867373@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785165012230 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785165012230@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785165012230 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785165012230@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785165012230@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785166543175 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166543175@example.com 07/27/2026":
      - cell "QA API Applicant 1785166543175 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785166543175@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785166543175@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785166546932 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166546932@example.com 07/27/2026":
      - cell "QA API Applicant 1785166546932 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785166546932@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785166546932@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785166674683 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166674683@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785166674683 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785166674683@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785166674683@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785166687871 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166687871@example.com 07/27/2026":
      - cell "QA E2E Applicant 1785166687871 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785166687871@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785166687871@example.com
      - cell "07/27/2026":
        - paragraph: 07/27/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785174639249 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174639249@example.com 07/28/2026":
      - cell "QA API Applicant 1785174639249 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785174639249@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785174639249@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785174643052 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174643052@example.com 07/28/2026":
      - cell "QA API Applicant 1785174643052 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785174643052@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785174643052@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174923682 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174923682@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174923682 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174923682@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174923682@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174937000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174937000@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174937000 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174937000@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174937000@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785174967174 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174967174@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785174967174 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785174967174@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785174967174@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785175131036 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785175131036@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785175131036 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785175131036@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785175131036@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785176312043 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176312043@example.com 07/28/2026":
      - cell "QA API Applicant 1785176312043 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785176312043@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785176312043@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785176316755 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176316755@example.com 07/28/2026":
      - cell "QA API Applicant 1785176316755 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785176316755@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785176316755@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176590785 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176590785@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176590785 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176590785@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176590785@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176603974 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176603974@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176603974 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176603974@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176603974@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785176635179 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176635179@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785176635179 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785176635179@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785176635179@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785181251452 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785181251452@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785181251452 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785181251452@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785181251452@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181304118 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181304118@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181304118 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181304118@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181304118@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181370726 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181370726@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181370726 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181370726@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181370726@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA REPRO Applicant 1785181411009 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181411009@example.com 07/28/2026":
      - cell "QA REPRO Applicant 1785181411009 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.repro.rental+1785181411009@example.com":
        - paragraph
        - paragraph: qa.repro.rental+1785181411009@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182151843 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182151843@example.com 07/28/2026":
      - cell "QA API Applicant 1785182151843 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182151843@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182151843@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182159475 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182159475@example.com 07/28/2026":
      - cell "QA API Applicant 1785182159475 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182159475@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182159475@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182214657 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182214657@example.com 07/28/2026":
      - cell "QA API Applicant 1785182214657 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182214657@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182214657@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785182219645 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182219645@example.com 07/28/2026":
      - cell "QA API Applicant 1785182219645 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785182219645@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785182219645@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182492367 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182492367@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182492367 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182492367@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182492367@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182505448 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182505448@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182505448 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182505448@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182505448@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785182537747 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182537747@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785182537747 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785182537747@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785182537747@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785217653318 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217653318@example.com 07/28/2026":
      - cell "QA API Applicant 1785217653318 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785217653318@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785217653318@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785217654270 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217654270@example.com 07/28/2026":
      - cell "QA API Applicant 1785217654270 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785217654270@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785217654270@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217690764 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217690764@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217690764 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217690764@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217690764@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217702084 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217702084@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217702084 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217702084@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217702084@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785217779706 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217779706@example.com 07/28/2026":
      - cell "QA E2E Applicant 1785217779706 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785217779706@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785217779706@example.com
      - cell "07/28/2026":
        - paragraph: 07/28/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785304444431 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304444431@example.com 07/29/2026":
      - cell "QA API Applicant 1785304444431 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785304444431@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785304444431@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785304445681 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304445681@example.com 07/29/2026":
      - cell "QA API Applicant 1785304445681 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785304445681@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785304445681@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304487313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304487313@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304487313 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304487313@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304487313@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304498813 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304498813@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304498813 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304498813@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304498813@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785304594738 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304594738@example.com 07/29/2026":
      - cell "QA E2E Applicant 1785304594738 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785304594738@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785304594738@example.com
      - cell "07/29/2026":
        - paragraph: 07/29/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785390174241 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390174241@example.com 07/30/2026":
      - cell "QA API Applicant 1785390174241 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785390174241@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785390174241@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785390175454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390175454@example.com 07/30/2026":
      - cell "QA API Applicant 1785390175454 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785390175454@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785390175454@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390219454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390219454@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390219454 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390219454@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390219454@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390221758 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390221758@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390221758 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390221758@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390221758@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785390292125 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390292125@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785390292125 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785390292125@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785390292125@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785428010606 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428010606@example.com 07/30/2026":
      - cell "QA API Applicant 1785428010606 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785428010606@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785428010606@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785428014187 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428014187@example.com 07/30/2026":
      - cell "QA API Applicant 1785428014187 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785428014187@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785428014187@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428283661 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428283661@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428283661 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428283661@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428283661@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428288741 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428288741@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428288741 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428288741@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428288741@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785428319604 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428319604@example.com 07/30/2026":
      - cell "QA E2E Applicant 1785428319604 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785428319604@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785428319604@example.com
      - cell "07/30/2026":
        - paragraph: 07/30/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785478548455 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548455@example.com 07/31/2026":
      - cell "QA API Applicant 1785478548455 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785478548455@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785478548455@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785478548841 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548841@example.com 07/31/2026":
      - cell "QA API Applicant 1785478548841 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785478548841@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785478548841@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478578511 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478578511@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478578511 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478578511@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478578511@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478580023 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478580023@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478580023 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478580023@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478580023@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785478669408 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478669408@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785478669408 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785478669408@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785478669408@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785481995802 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481995802@example.com 07/31/2026":
      - cell "QA API Applicant 1785481995802 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785481995802@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785481995802@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1785481999622 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481999622@example.com 07/31/2026":
      - cell "QA API Applicant 1785481999622 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1785481999622@example.com":
        - paragraph
        - paragraph: qa.api.rental+1785481999622@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1785482277264 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785482277264@example.com 07/31/2026":
      - cell "QA E2E Applicant 1785482277264 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1785482277264@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1785482277264@example.com
      - cell "07/31/2026":
        - paragraph: 07/31/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
- group:
  - text: "Items per page:"
  - combobox "100 Items per page:": "100"
  - text: 1 – 100 of 112
  - button "Previous page" [disabled]
  - button "Next page"
- text: "> Quick Action"
- img "plus"
- text: Add Application
- complementary:
  - img
- img
```

<details><summary>Trace</summary>

```
signed_in_rental_applications_page = <pages.rental_application_page.RentalApplicationPage object at 0x10794a790>
seeded_rental_application = {'application': {'propertyId': '12613aac-76b8-4d64-a6ca-c388ff1cd438', 'userId': '037fbfa2-0d4c-432a-b14c-537531e6f87c...d': '1954dea7-2fbf-492d-82e5-a74e2118cc3e', ...}, 'unit_name': '3505 Adams Road', 'assigned_user_name': 'Jane Manager'}

    @pytest.mark.smoke
    def test_created_application_appears_correctly_in_list(signed_in_rental_applications_page, seeded_rental_application):
        rental_page = signed_in_rental_applications_page
        application = seeded_rental_application["application"]
    
        rental_page.all_applications_tab.click()
    
        # The list defaults to 10 rows/page and this org has accumulated more
        # than that from prior test runs, so a freshly created row can land on
        # page 2+ regardless of sort order. Widen the page size so the new row
        # is guaranteed to be on the (only) page, rather than depending on sort.
        rental_page.page.get_by_role("combobox", name="Items per page:").click()
        rental_page.page.get_by_role("option", name="100", exact=True).click()
    
        row = rental_page.table.locator("tr", has_text=application["lastName"])
>       expect(row).to_be_visible(timeout=10000)
E       AssertionError: Locator expected to be visible
E       Actual value: None
E       Error: element(s) not found 
E       Call log:
E         - Expect "to_be_visible" with timeout 10000ms
E         - waiting for locator("table").first.locator("tr").filter(has_text="Applicant 1785488290919")
E       
E       Aria snapshot:
E       - paragraph: Create New
E       - img "Remove Icon"
E       - paragraph: Contacts
E       - img "Customer Account Icon"
E       - paragraph: Customer Account
E       - img "Tenant Icon"
E       - paragraph: Tenant
E       - img "Owner Icon"
E       - paragraph: Owner
E       - img "Vendor Icon"
E       - paragraph: Vendor
E       - img "Employee Icon"
E       - paragraph: Employee
E       - paragraph: Tasks & Maintenance
E       - img "Task Icon"
E       - paragraph: Task
E       - img "Work Order Icon"
E       - paragraph: Work Order
E       - paragraph: Vendor Transactions
E       - img "Create Invoice Icon"
E       - paragraph: Create Invoice
E       - img "Pay Invoices Icon"
E       - paragraph: Pay Invoices
E       - img "Vendor Credit Icon"
E       - paragraph: Vendor Credit
E       - paragraph: Customer Transactions
E       - img "Create Charge Icon"
E       - paragraph: Create Charge
E       - img "Receive Payment Icon"
E       - paragraph: Receive Payment
E       - img "Credit Memo Icon"
E       - paragraph: Credit Memo
E       - img "Quick Charge Icon"
E       - paragraph: Quick Charge
E       - paragraph: Other Transactions
E       - img "Journal Entry Icon"
E       - paragraph: Journal Entry
E       - img "Bank Transfer Icon"
E       - paragraph: Bank Transfer
E       - img "Bank Deposit Icon"
E       - paragraph: Bank Deposit
E       - img "Check Icon"
E       - paragraph: Check
E       - paragraph: Reporting
E       - img "Violation Icon"
E       - paragraph: Violation
E       - img "Modification Icon"
E       - paragraph: Modification
E       - img "Inspection Icon"
E       - paragraph: Inspection
E       - img "Motion Icon"
E       - paragraph: Motion
E       - img "Meeting Icon"
E       - paragraph: Meeting
E       - img "Election Icon"
E       - paragraph: Election
E       - paragraph: Properties
E       - img "Association Icon"
E       - paragraph: Association
E       - img "Unit Icon"
E       - paragraph: Unit
E       - paragraph: Communications
E       - img "Announcement Icon"
E       - paragraph: Announcement
E       - button "Liberty Community Management Inc":
E         - img "Liberty Community Management Inc"
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - img
E       - heading "Leasing" [level=5]
E       - menuitem "Active Leases":
E         - paragraph: Active Leases
E       - menuitem "Lease Renewals":
E         - paragraph: Lease Renewals
E       - menuitem "Rental Applications":
E         - paragraph: Rental Applications
E       - menuitem "Draft Leases":
E         - paragraph: Draft Leases
E       - menuitem "Unit Sales":
E         - paragraph: Unit Sales
E       - menuitem "Move In/Out":
E         - paragraph: Move In/Out
E       - textbox "Search Roam"
E       - img "search"
E       - combobox "Elisa Miller":
E         - text: Elisa Miller
E         - img
E       - button
E       - combobox "Chattahoochee Reserve":
E         - text: Chattahoochee Reserve
E         - img
E       - button
E       - button "Notifications": "2"
E       - button "Switch to dark mode"
E       - img "image"
E       - banner:
E         - heading "Rental Applications" [level=1]
E       - button "Undecided 112":
E         - paragraph: Undecided
E         - paragraph: "112"
E       - button "All Applications 112" [pressed]:
E         - paragraph: All Applications
E         - paragraph: "112"
E       - button "Name":
E         - paragraph: Name
E       - button "Status":
E         - paragraph: Status
E       - button "Units":
E         - paragraph: Units
E       - button "Move In Date":
E         - paragraph: Move In Date
E       - button "Contact":
E         - paragraph: Contact
E       - button "All Filters"
E       - button "Reset"
E       - table:
E         - rowgroup:
E           - row "Name Association Move In Date Contact Last Updated Action Select all rows":
E             - columnheader "Name":
E               - button "Name"
E             - columnheader "Association":
E               - button "Association"
E             - columnheader "Move In Date":
E               - button "Move In Date"
E             - columnheader "Contact":
E               - button "Contact"
E             - columnheader "Last Updated":
E               - button "Last Updated"
E             - columnheader "Action"
E             - columnheader "Select all rows":
E               - checkbox "Select all rows"
E         - rowgroup:
E           - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170527 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170527@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170527@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170944 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170944@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170944@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613207486 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613207486@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613207486@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613208441 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613208441@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613208441@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613279983 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613279983@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613279983@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699556687 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699556687@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699556687@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699557430 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699557430@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699557430@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699602883 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699602883@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699602883@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699604171 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699604171@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699604171@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699693148 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699693148@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699693148@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784786177651 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786177651@example.com 07/23/2026":
E             - cell "QA API Applicant 1784786177651 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784786177651@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784786177651@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784786178641 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784786178641@example.com 07/23/2026":
E             - cell "QA API Applicant 1784786178641 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784786178641@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784786178641@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786226851 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786226851@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786226851 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786226851@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786226851@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786228778 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786228778@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786228778 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786228778@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786228778@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784786341914 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784786341914@example.com 07/23/2026":
E             - cell "QA E2E Applicant 1784786341914 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784786341914@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784786341914@example.com
E             - cell "07/23/2026":
E               - paragraph: 07/23/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784872304313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304313@example.com 07/24/2026":
E             - cell "QA API Applicant 1784872304313 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784872304313@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784872304313@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784872304674 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784872304674@example.com 07/24/2026":
E             - cell "QA API Applicant 1784872304674 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784872304674@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784872304674@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872334666 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872334666@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872334666 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872334666@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872334666@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872345532 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872345532@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872345532 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872345532@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872345532@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784872416193 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784872416193@example.com 07/24/2026":
E             - cell "QA E2E Applicant 1784872416193 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784872416193@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784872416193@example.com
E             - cell "07/24/2026":
E               - paragraph: 07/24/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784958264992 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958264992@example.com 07/25/2026":
E             - cell "QA API Applicant 1784958264992 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784958264992@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784958264992@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784958265686 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784958265686@example.com 07/25/2026":
E             - cell "QA API Applicant 1784958265686 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784958265686@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784958265686@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958300566 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958300566@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958300566 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958300566@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958300566@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958311698 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958311698@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958311698 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958311698@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958311698@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784958381154 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784958381154@example.com 07/25/2026":
E             - cell "QA E2E Applicant 1784958381154 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784958381154@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784958381154@example.com
E             - cell "07/25/2026":
E               - paragraph: 07/25/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785046064823 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046064823@example.com 07/26/2026":
E             - cell "QA API Applicant 1785046064823 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785046064823@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785046064823@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785046065302 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785046065302@example.com 07/26/2026":
E             - cell "QA API Applicant 1785046065302 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785046065302@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785046065302@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046094192 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046094192@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046094192 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046094192@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046094192@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046105062 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046105062@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046105062 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046105062@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046105062@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785046178688 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785046178688@example.com 07/26/2026":
E             - cell "QA E2E Applicant 1785046178688 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785046178688@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785046178688@example.com
E             - cell "07/26/2026":
E               - paragraph: 07/26/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785133937409 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133937409@example.com 07/27/2026":
E             - cell "QA API Applicant 1785133937409 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785133937409@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785133937409@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785133938549 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785133938549@example.com 07/27/2026":
E             - cell "QA API Applicant 1785133938549 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785133938549@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785133938549@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785133986958 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133986958@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785133986958 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785133986958@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785133986958@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785133998546 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785133998546@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785133998546 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785133998546@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785133998546@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785134075900 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785134075900@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785134075900 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785134075900@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785134075900@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785158325923 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158325923@example.com 07/27/2026":
E             - cell "QA API Applicant 1785158325923 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785158325923@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785158325923@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785158335121 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785158335121@example.com 07/27/2026":
E             - cell "QA API Applicant 1785158335121 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785158335121@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785158335121@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785158425414 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158425414@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785158425414 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785158425414@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785158425414@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785158438554 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785158438554@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785158438554 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785158438554@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785158438554@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA Repro Repro 1785160512499 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160512499@example.com 07/27/2026":
E             - cell "QA Repro Repro 1785160512499 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785160512499@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785160512499@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA Repro Repro 1785160567000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785160567000@example.com 07/27/2026":
E             - cell "QA Repro Repro 1785160567000 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785160567000@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785160567000@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785164719979 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164719979@example.com 07/27/2026":
E             - cell "QA API Applicant 1785164719979 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785164719979@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785164719979@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785164723734 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785164723734@example.com 07/27/2026":
E             - cell "QA API Applicant 1785164723734 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785164723734@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785164723734@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785164854132 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164854132@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785164854132 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785164854132@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785164854132@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785164867373 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785164867373@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785164867373 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785164867373@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785164867373@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785165012230 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785165012230@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785165012230 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785165012230@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785165012230@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785166543175 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166543175@example.com 07/27/2026":
E             - cell "QA API Applicant 1785166543175 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785166543175@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785166543175@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785166546932 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785166546932@example.com 07/27/2026":
E             - cell "QA API Applicant 1785166546932 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785166546932@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785166546932@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785166674683 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166674683@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785166674683 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785166674683@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785166674683@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785166687871 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785166687871@example.com 07/27/2026":
E             - cell "QA E2E Applicant 1785166687871 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785166687871@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785166687871@example.com
E             - cell "07/27/2026":
E               - paragraph: 07/27/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785174639249 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174639249@example.com 07/28/2026":
E             - cell "QA API Applicant 1785174639249 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785174639249@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785174639249@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785174643052 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785174643052@example.com 07/28/2026":
E             - cell "QA API Applicant 1785174643052 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785174643052@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785174643052@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174923682 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174923682@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174923682 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174923682@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174923682@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174937000 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174937000@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174937000 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174937000@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174937000@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785174967174 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785174967174@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785174967174 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785174967174@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785174967174@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785175131036 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785175131036@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785175131036 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785175131036@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785175131036@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785176312043 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176312043@example.com 07/28/2026":
E             - cell "QA API Applicant 1785176312043 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785176312043@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785176312043@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785176316755 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785176316755@example.com 07/28/2026":
E             - cell "QA API Applicant 1785176316755 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785176316755@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785176316755@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176590785 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176590785@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176590785 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176590785@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176590785@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176603974 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176603974@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176603974 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176603974@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176603974@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785176635179 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785176635179@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785176635179 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785176635179@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785176635179@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785181251452 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785181251452@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785181251452 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785181251452@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785181251452@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181304118 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181304118@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181304118 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181304118@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181304118@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181370726 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181370726@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181370726 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181370726@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181370726@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA REPRO Applicant 1785181411009 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.repro.rental+1785181411009@example.com 07/28/2026":
E             - cell "QA REPRO Applicant 1785181411009 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.repro.rental+1785181411009@example.com":
E               - paragraph
E               - paragraph: qa.repro.rental+1785181411009@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182151843 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182151843@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182151843 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182151843@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182151843@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182159475 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182159475@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182159475 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182159475@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182159475@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182214657 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182214657@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182214657 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182214657@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182214657@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785182219645 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785182219645@example.com 07/28/2026":
E             - cell "QA API Applicant 1785182219645 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785182219645@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785182219645@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182492367 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182492367@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182492367 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182492367@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182492367@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182505448 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182505448@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182505448 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182505448@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182505448@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785182537747 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785182537747@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785182537747 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785182537747@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785182537747@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785217653318 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217653318@example.com 07/28/2026":
E             - cell "QA API Applicant 1785217653318 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785217653318@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785217653318@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785217654270 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785217654270@example.com 07/28/2026":
E             - cell "QA API Applicant 1785217654270 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785217654270@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785217654270@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217690764 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217690764@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217690764 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217690764@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217690764@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217702084 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217702084@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217702084 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217702084@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217702084@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785217779706 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785217779706@example.com 07/28/2026":
E             - cell "QA E2E Applicant 1785217779706 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785217779706@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785217779706@example.com
E             - cell "07/28/2026":
E               - paragraph: 07/28/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785304444431 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304444431@example.com 07/29/2026":
E             - cell "QA API Applicant 1785304444431 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785304444431@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785304444431@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785304445681 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785304445681@example.com 07/29/2026":
E             - cell "QA API Applicant 1785304445681 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785304445681@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785304445681@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304487313 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304487313@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304487313 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304487313@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304487313@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304498813 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304498813@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304498813 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304498813@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304498813@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785304594738 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785304594738@example.com 07/29/2026":
E             - cell "QA E2E Applicant 1785304594738 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785304594738@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785304594738@example.com
E             - cell "07/29/2026":
E               - paragraph: 07/29/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785390174241 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390174241@example.com 07/30/2026":
E             - cell "QA API Applicant 1785390174241 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785390174241@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785390174241@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785390175454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785390175454@example.com 07/30/2026":
E             - cell "QA API Applicant 1785390175454 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785390175454@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785390175454@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390219454 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390219454@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390219454 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390219454@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390219454@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390221758 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390221758@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390221758 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390221758@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390221758@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785390292125 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785390292125@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785390292125 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785390292125@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785390292125@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785428010606 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428010606@example.com 07/30/2026":
E             - cell "QA API Applicant 1785428010606 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785428010606@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785428010606@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785428014187 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785428014187@example.com 07/30/2026":
E             - cell "QA API Applicant 1785428014187 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785428014187@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785428014187@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428283661 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428283661@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428283661 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428283661@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428283661@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428288741 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428288741@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428288741 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428288741@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428288741@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785428319604 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785428319604@example.com 07/30/2026":
E             - cell "QA E2E Applicant 1785428319604 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785428319604@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785428319604@example.com
E             - cell "07/30/2026":
E               - paragraph: 07/30/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785478548455 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548455@example.com 07/31/2026":
E             - cell "QA API Applicant 1785478548455 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785478548455@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785478548455@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785478548841 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785478548841@example.com 07/31/2026":
E             - cell "QA API Applicant 1785478548841 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785478548841@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785478548841@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478578511 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478578511@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478578511 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478578511@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478578511@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478580023 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478580023@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478580023 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478580023@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478580023@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785478669408 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785478669408@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785478669408 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785478669408@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785478669408@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785481995802 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481995802@example.com 07/31/2026":
E             - cell "QA API Applicant 1785481995802 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785481995802@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785481995802@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1785481999622 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1785481999622@example.com 07/31/2026":
E             - cell "QA API Applicant 1785481999622 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1785481999622@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1785481999622@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1785482277264 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1785482277264@example.com 07/31/2026":
E             - cell "QA E2E Applicant 1785482277264 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1785482277264@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1785482277264@example.com
E             - cell "07/31/2026":
E               - paragraph: 07/31/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E       - group:
E         - text: "Items per page:"
E         - combobox "100 Items per page:": "100"
E         - text: 1 – 100 of 112
E         - button "Previous page" [disabled]
E         - button "Next page"
E       - text: "> Quick Action"
E       - img "plus"
E       - text: Add Application
E       - complementary:
E         - img
E       - img

tests/e2e/test_leasing_rental_application.py:53: AssertionError
```

</details>

Screenshots/videos/traces for this run are in the `test-results/` or `playwright-artifacts` CI artifact.

---

## test_all_filters_button_opens_panel[chromium]

- Status: `failed`
- Full name: `tests.e2e.test_leasing_rental_application#test_all_filters_button_opens_panel`

**Error**
```
AssertionError: Locator expected to be visible
Actual value: None
Error: element(s) not found 
Call log:
  - Expect "to_be_visible" with timeout 5000ms
  - waiting for get_by_role("heading", name="Filters")

Aria snapshot:
- paragraph: Create New
- img "Remove Icon"
- paragraph: Contacts
- img "Customer Account Icon"
- paragraph: Customer Account
- img "Tenant Icon"
- paragraph: Tenant
- img "Owner Icon"
- paragraph: Owner
- img "Vendor Icon"
- paragraph: Vendor
- img "Employee Icon"
- paragraph: Employee
- paragraph: Tasks & Maintenance
- img "Task Icon"
- paragraph: Task
- img "Work Order Icon"
- paragraph: Work Order
- paragraph: Vendor Transactions
- img "Create Invoice Icon"
- paragraph: Create Invoice
- img "Pay Invoices Icon"
- paragraph: Pay Invoices
- img "Vendor Credit Icon"
- paragraph: Vendor Credit
- paragraph: Customer Transactions
- img "Create Charge Icon"
- paragraph: Create Charge
- img "Receive Payment Icon"
- paragraph: Receive Payment
- img "Credit Memo Icon"
- paragraph: Credit Memo
- img "Quick Charge Icon"
- paragraph: Quick Charge
- paragraph: Other Transactions
- img "Journal Entry Icon"
- paragraph: Journal Entry
- img "Bank Transfer Icon"
- paragraph: Bank Transfer
- img "Bank Deposit Icon"
- paragraph: Bank Deposit
- img "Check Icon"
- paragraph: Check
- paragraph: Reporting
- img "Violation Icon"
- paragraph: Violation
- img "Modification Icon"
- paragraph: Modification
- img "Inspection Icon"
- paragraph: Inspection
- img "Motion Icon"
- paragraph: Motion
- img "Meeting Icon"
- paragraph: Meeting
- img "Election Icon"
- paragraph: Election
- paragraph: Properties
- img "Association Icon"
- paragraph: Association
- img "Unit Icon"
- paragraph: Unit
- paragraph: Communications
- img "Announcement Icon"
- paragraph: Announcement
- button "Liberty Community Management Inc":
  - img "Liberty Community Management Inc"
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- button
- img
- heading "Leasing" [level=5]
- menuitem "Active Leases":
  - paragraph: Active Leases
- menuitem "Lease Renewals":
  - paragraph: Lease Renewals
- menuitem "Rental Applications":
  - paragraph: Rental Applications
- menuitem "Draft Leases":
  - paragraph: Draft Leases
- menuitem "Unit Sales":
  - paragraph: Unit Sales
- menuitem "Move In/Out":
  - paragraph: Move In/Out
- textbox "Search Roam"
- img "search"
- combobox "Elisa Miller":
  - text: Elisa Miller
  - img
- button
- combobox "Chattahoochee Reserve":
  - text: Chattahoochee Reserve
  - img
- button
- button "Notifications": "2"
- button "Switch to dark mode"
- img "image"
- banner:
  - heading "Rental Applications" [level=1]
- button "Undecided 113" [pressed]:
  - paragraph: Undecided
  - paragraph: "113"
- button "All Applications 113":
  - paragraph: All Applications
  - paragraph: "113"
- button "Name":
  - paragraph: Name
- button "Status":
  - paragraph: Status
- button "Units":
  - paragraph: Units
- button "Move In Date":
  - paragraph: Move In Date
- button "Contact":
  - paragraph: Contact
- button "All Filters"
- button "Reset"
- table:
  - rowgroup:
    - row "Name Association Move In Date Contact Last Updated Action Select all rows":
      - columnheader "Name":
        - button "Name"
      - columnheader "Association":
        - button "Association"
      - columnheader "Move In Date":
        - button "Move In Date"
      - columnheader "Contact":
        - button "Contact"
      - columnheader "Last Updated":
        - button "Last Updated"
      - columnheader "Action"
      - columnheader "Select all rows":
        - checkbox "Select all rows"
  - rowgroup:
    - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170944 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170944@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170944@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613207486 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613207486@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613207486@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613208441 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613208441@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613208441@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
      - cell "QA E2E Applicant 1784613279983 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784613279983@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784613279983@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
      - cell "QA API Applicant 1784699556687 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699556687@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699556687@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
      - cell "QA API Applicant 1784699557430 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784699557430@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784699557430@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699602883 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699602883@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699602883@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699604171 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699604171@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699604171@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
      - cell "QA E2E Applicant 1784699693148 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.e2e.rental+1784699693148@example.com":
        - paragraph
        - paragraph: qa.e2e.rental+1784699693148@example.com
      - cell "07/22/2026":
        - paragraph: 07/22/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
    - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
      - cell "QA API Applicant 1784613170527 Pending"
      - cell "Chattahoochee Reserve 3505 Adams Road":
        - img
        - text: Chattahoochee Reserve
        - img
        - text: 3505 Adams Road
      - cell "12/01/2026":
        - paragraph: 12/01/2026
      - cell "qa.api.rental+1784613170527@example.com":
        - paragraph
        - paragraph: qa.api.rental+1784613170527@example.com
      - cell "07/21/2026":
        - paragraph: 07/21/2026
      - cell:
        - button:
          - img
      - cell:
        - checkbox
- group:
  - text: "Items per page:"
  - combobox "10 Items per page:": "10"
  - text: 1 – 10 of 113
  - button "Previous page" [disabled]
  - button "Next page"
- text: "> Quick Action"
- img "plus"
- text: Add Application
- complementary:
  - img
- img
```

<details><summary>Trace</summary>

```
signed_in_rental_applications_page = <pages.rental_application_page.RentalApplicationPage object at 0x107e46b10>

    @pytest.mark.known_bug
    @allure.tag("known-bug")
    def test_all_filters_button_opens_panel(signed_in_rental_applications_page):
        """Known bug: "All Filters" does nothing on Rental Applications.
    
        Verified live: forced clicks, bounding-box target-point checks, and 1.5s
        of DOM polling all show no overlay/heading ever appears. The equivalent
        button on Active Leases works correctly and opens a "Filters" panel
        (see LeasingActivePage.open_all_filters / test_all_filters_panel_opens_and_closes)
        - this asserts Rental Applications should behave the same way.
        """
        rental_page = signed_in_rental_applications_page
    
        rental_page.open_all_filters()
    
>       expect(rental_page.filters_panel_heading).to_be_visible()
E       AssertionError: Locator expected to be visible
E       Actual value: None
E       Error: element(s) not found 
E       Call log:
E         - Expect "to_be_visible" with timeout 5000ms
E         - waiting for get_by_role("heading", name="Filters")
E       
E       Aria snapshot:
E       - paragraph: Create New
E       - img "Remove Icon"
E       - paragraph: Contacts
E       - img "Customer Account Icon"
E       - paragraph: Customer Account
E       - img "Tenant Icon"
E       - paragraph: Tenant
E       - img "Owner Icon"
E       - paragraph: Owner
E       - img "Vendor Icon"
E       - paragraph: Vendor
E       - img "Employee Icon"
E       - paragraph: Employee
E       - paragraph: Tasks & Maintenance
E       - img "Task Icon"
E       - paragraph: Task
E       - img "Work Order Icon"
E       - paragraph: Work Order
E       - paragraph: Vendor Transactions
E       - img "Create Invoice Icon"
E       - paragraph: Create Invoice
E       - img "Pay Invoices Icon"
E       - paragraph: Pay Invoices
E       - img "Vendor Credit Icon"
E       - paragraph: Vendor Credit
E       - paragraph: Customer Transactions
E       - img "Create Charge Icon"
E       - paragraph: Create Charge
E       - img "Receive Payment Icon"
E       - paragraph: Receive Payment
E       - img "Credit Memo Icon"
E       - paragraph: Credit Memo
E       - img "Quick Charge Icon"
E       - paragraph: Quick Charge
E       - paragraph: Other Transactions
E       - img "Journal Entry Icon"
E       - paragraph: Journal Entry
E       - img "Bank Transfer Icon"
E       - paragraph: Bank Transfer
E       - img "Bank Deposit Icon"
E       - paragraph: Bank Deposit
E       - img "Check Icon"
E       - paragraph: Check
E       - paragraph: Reporting
E       - img "Violation Icon"
E       - paragraph: Violation
E       - img "Modification Icon"
E       - paragraph: Modification
E       - img "Inspection Icon"
E       - paragraph: Inspection
E       - img "Motion Icon"
E       - paragraph: Motion
E       - img "Meeting Icon"
E       - paragraph: Meeting
E       - img "Election Icon"
E       - paragraph: Election
E       - paragraph: Properties
E       - img "Association Icon"
E       - paragraph: Association
E       - img "Unit Icon"
E       - paragraph: Unit
E       - paragraph: Communications
E       - img "Announcement Icon"
E       - paragraph: Announcement
E       - button "Liberty Community Management Inc":
E         - img "Liberty Community Management Inc"
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - button
E       - img
E       - heading "Leasing" [level=5]
E       - menuitem "Active Leases":
E         - paragraph: Active Leases
E       - menuitem "Lease Renewals":
E         - paragraph: Lease Renewals
E       - menuitem "Rental Applications":
E         - paragraph: Rental Applications
E       - menuitem "Draft Leases":
E         - paragraph: Draft Leases
E       - menuitem "Unit Sales":
E         - paragraph: Unit Sales
E       - menuitem "Move In/Out":
E         - paragraph: Move In/Out
E       - textbox "Search Roam"
E       - img "search"
E       - combobox "Elisa Miller":
E         - text: Elisa Miller
E         - img
E       - button
E       - combobox "Chattahoochee Reserve":
E         - text: Chattahoochee Reserve
E         - img
E       - button
E       - button "Notifications": "2"
E       - button "Switch to dark mode"
E       - img "image"
E       - banner:
E         - heading "Rental Applications" [level=1]
E       - button "Undecided 113" [pressed]:
E         - paragraph: Undecided
E         - paragraph: "113"
E       - button "All Applications 113":
E         - paragraph: All Applications
E         - paragraph: "113"
E       - button "Name":
E         - paragraph: Name
E       - button "Status":
E         - paragraph: Status
E       - button "Units":
E         - paragraph: Units
E       - button "Move In Date":
E         - paragraph: Move In Date
E       - button "Contact":
E         - paragraph: Contact
E       - button "All Filters"
E       - button "Reset"
E       - table:
E         - rowgroup:
E           - row "Name Association Move In Date Contact Last Updated Action Select all rows":
E             - columnheader "Name":
E               - button "Name"
E             - columnheader "Association":
E               - button "Association"
E             - columnheader "Move In Date":
E               - button "Move In Date"
E             - columnheader "Contact":
E               - button "Contact"
E             - columnheader "Last Updated":
E               - button "Last Updated"
E             - columnheader "Action"
E             - columnheader "Select all rows":
E               - checkbox "Select all rows"
E         - rowgroup:
E           - row "QA API Applicant 1784613170944 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170944@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170944 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170944@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170944@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613207486 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613207486@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613207486 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613207486@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613207486@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613208441 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613208441@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613208441 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613208441@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613208441@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784613279983 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784613279983@example.com 07/21/2026":
E             - cell "QA E2E Applicant 1784613279983 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784613279983@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784613279983@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699556687 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699556687@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699556687 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699556687@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699556687@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784699557430 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784699557430@example.com 07/22/2026":
E             - cell "QA API Applicant 1784699557430 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784699557430@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784699557430@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699602883 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699602883@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699602883 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699602883@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699602883@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699604171 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699604171@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699604171 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699604171@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699604171@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA E2E Applicant 1784699693148 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.e2e.rental+1784699693148@example.com 07/22/2026":
E             - cell "QA E2E Applicant 1784699693148 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.e2e.rental+1784699693148@example.com":
E               - paragraph
E               - paragraph: qa.e2e.rental+1784699693148@example.com
E             - cell "07/22/2026":
E               - paragraph: 07/22/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E           - row "QA API Applicant 1784613170527 Pending Chattahoochee Reserve 3505 Adams Road 12/01/2026 qa.api.rental+1784613170527@example.com 07/21/2026":
E             - cell "QA API Applicant 1784613170527 Pending"
E             - cell "Chattahoochee Reserve 3505 Adams Road":
E               - img
E               - text: Chattahoochee Reserve
E               - img
E               - text: 3505 Adams Road
E             - cell "12/01/2026":
E               - paragraph: 12/01/2026
E             - cell "qa.api.rental+1784613170527@example.com":
E               - paragraph
E               - paragraph: qa.api.rental+1784613170527@example.com
E             - cell "07/21/2026":
E               - paragraph: 07/21/2026
E             - cell:
E               - button:
E                 - img
E             - cell:
E               - checkbox
E       - group:
E         - text: "Items per page:"
E         - combobox "10 Items per page:": "10"
E         - text: 1 – 10 of 113
E         - button "Previous page" [disabled]
E         - button "Next page"
E       - text: "> Quick Action"
E       - img "plus"
E       - text: Add Application
E       - complementary:
E         - img
E       - img

tests/e2e/test_leasing_rental_application.py:113: AssertionError
```

</details>

Screenshots/videos/traces for this run are in the `test-results/` or `playwright-artifacts` CI artifact.

---
