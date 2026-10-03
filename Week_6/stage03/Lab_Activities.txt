A) Requirement Review

Case Study Title: SmartCare Clinic Appointment Booking System
SmartCare is a small community clinic that provides consultations through a number of healthcare practitioners (GPs). 
The clinic currently manages <mark>patient information and appointments</mark> using a combination of spreadsheets, 
paper records and manual processes.

The clinic has experienced several operational problems, including:
    duplicate appointment bookings
    difficulty locating patient records;
    inconsistent appointment status information;
    limited visibility of practitioner availability;
    manual cancellation processes;
    lack of reliable appointment history;
    difficulty producing basic operational reports.

<mark>Management wants a simple software system that can initially support patient, practitioner and appointment
management</mark>.

<mark>The organisation does not want a complex hospital information system. The first version should be a manageable 
application suitable for a small clinic</mark>.

Problem and Scope
Problem: SmartCare's current system does not allow for a seamless and efficient system to <mark>manage records, 
appointments and general information for patients and practitioners</mark>. The new system needs to be able to handle 
the creation,deletion and editing of appointments including history and status, as well as patient and practitioner 
records and information. 

In Scope:
    <mark>Create</mark> appointment
    <mark>Edit</mark> appointments
    <mark>Delete</mark> appointments
    <mark>Set and view</mark> appointment status 
    <mark>Confirm</mark> no duplicate bookings 
    <mark>Access</mark> patient records
    <mark>Add</mark> patient records
    Edit patient records
    Access and view patient appointment history 
    View practitioner information 
    <mark>Search</mark> feature for locating patient records 

Out of Scope: 
    <mark>Creating and viewing</mark>   medical diagnosis
    Creating treatment plans 
    Accessing and viewing treatment plans 
    Patient accounts 
    Viewing medication stock
    <mark>Ordering</mark>   medication 
    <mark>Email</mark>  
    Internal communication system between front desk and practitioners 

Stakeholders

Patient
    <mark>Access</mark> practitioner information
    Patient's need access to basic information regarding practitioners in order to decide who to work with or to know 
    who they will be working with 

Practitioner
    <mark>Access</mark> patient records, appointment history 
    Practitioner's need access to patient records including their appointment history to provide care to said patient 

Administration staff
    <mark>Create/ edit</mark> practitioner information, <mark>create/edit</mark> patient records 
    Administration needs access to both the patient and practitioner's records in order to add or edit information to 
    provide clear and concise records 

Front desk staff
    <mark>Create, edit or delete</mark> appointments, <mark>access and edit</mark> patient records, <mark>access</mark>
    appointment history, <mark>view</mark> practitioner records 
    The main duty is to manage appointments, to support that task access to practitioner information and patient 
    information is given 

Management 
    <mark>View</mark> practitioner records, <mark>view</mark> number of appointments made 
    Management serves in creating reports and oversight, as such they only need access to practitioner records and 
    statistics of the system 

Functional Requirements
FR-01: <mark>Create</mark> appointments 
FR-02: <mark>Edit</mark>  appointments 
FR-03: <mark>Delete</mark>  appointments  
FR-04: Create patient record
FR-05: Edit patient record
FR-06: <mark>Search</mark>  for patient record
FR-07: Edit appointment status
FR-08: <mark>Access</mark>  appointment history per patient 
FR-09: Create practitioner record 
FR-10: Edit practitioner record 
FR-11: Delete practitioner record 
FR-12: Create statistics 

Non-Functional Requirements
NFR-01: <mark>Each action takes less than 3 clicks</mark>  
NFR-02: Each page loads under 2 seconds  
NFR-03: <mark>System interface must meet accessibility needs</mark>
NFR-04: System must support multiple appointment bookings 
NFR-05: <mark>Ensure no double booking has taken place</mark>  
NFR-06: <mark>Sensitive information must be encrypted and password protected</mark>  

User Stories
   US-01: As a patient, I want to <mark>view</mark> doctor's information, so that I can be informed on who my carer is.
   US-02: As a doctor, I want to <mark>access</mark> patient records, so that I can provide the best care possible for 
my patients.
   US-03: As a receptionist, I want to <mark>create</mark> appointments, so that patients have appointments with 
doctors.
   US-04: As a manager, I want to have <mark>access</mark> to data, so that I can make reports concerning appointment 
numbers.
   US-05: As an admin, I want to <mark>create and edit</mark> patient records, so that important information is up to 
date.
   US-06: As a receptionist, I want to <mark>delete</mark> appointments, so that there are no duplicates or double 
bookings.

Acceptance Criteria
GIVEN an appointment is duplicated
WHEN a receptionist enters information
THEN the system flags that appointment and prompts it is a duplicate
   
GIVEN a patient record is being created
WHEN an admin enters data into a form
THEN the system creates a patient record 
   
GIVEN data is being collected
WHEN a manger accesses the system's statistics 
THEN the number of appointments booked appears 

B) Candidate Classes

| Requirement                                   | Concept            | State/Behaviour | Decision  |
|-----------------------------------------------|--------------------|-----------------|-----------|
| FR-01: Create Appointment                     | Appointment        | Create          | Class     |
| FR-02: Edit Appointments                      | Appointment        | Edit            | Class     |
| FR-03: Delete Appointments                    | Appointemnt        | Delete          | Class     |
| FR-04: Create paitent record                  | Paitent            | Create          | Class     |
| FR-05: Edit paitent record                    | Paitent            | Edit            | Class     |
| FR-06: Search paitent record                  | Paitent            | Search          | Not class |
| FR-07: Edit appointment status                | Appointment status | Edit            | Not class |
| FR-08: Access appointment history per paitent | Paitent            | Access          | Class     |
| FR-09: Create practitioner record             | Practitioner       | Create          | Class     |
| FR-10: Edit practitioner record               | Practitioner       | Edit            | Class     |
| FR-11: Delete practitioner record             | Practitioner       | Delete          | Class     |
| FR-12: Create statistics                      | Statistics         | Create          | Not class |

C) CRC Cards
**Patient**

| Responsibilities                  | Collaborators |
|-----------------------------------|---------------|
| Store patient information         | Appointment   |
| Access patient history            | Practitioner  |

**Practitioner**

| Responsibilities               | Collaborators |
|--------------------------------|---------------|
| Store practitioner information | Appointment   |
| Access paitnet records         | Patinet       |

**Appointment**

| Responsibilities                  | Collaborators          |
|-----------------------------------|------------------------|
| Connect paitent with practitioner | Practitioner & Patinet |
| Store appointment status          | Practitioner           |
| Store appointment information     | Practitioner & Patinet |


D) UML Model
See ST_UML.pdf

E) AI Design Review
Suggested Classes
Patient
   Supporting Requirements:
   FR-04, FR-05, FR-06, and FR-08

Practitioner
    Supporting Requirements:
    FR-09, FR-10, FR-11, and US-01 View practitioner information 

Appointment 
    Supporting Requirements:
    FR-01, FR-02, FR-03, and FR-08

Statistics
    Supporting Requirements:
    FR-12 and US-04 Manager accesses data for reports 

Relationships:
Patient 1 --- 0..* Appointment
    Supporting Requirements and reasoning:
    FR-01 and FR-08; a patient may have many appointments, while each appointment belongs to one patient 

Practitioner 1 --- 0..* Appointment
    Supporting Requirements and reasoning:
    FR-01, FR-09, FR-10, FR-11, US-01 Practitioner information available to patients; a practitioner can have many 
appointments, while each appointment is scheduled with one practitioner

Suggested Attributes:
Appointment Status
    Supporting Requirements and reasoning:
    FR-07; the requirements only state that the status must be updated. they do not indicate that Status must be 
managed independently, so it is better represented as an attribute rather than a separate class

F) Compare and Decide
Design Review

| AI Suggestion               | Evidence                   | Decision | Reason                                                        | Model Change                        |
|-----------------------------|----------------------------|----------|---------------------------------------------------------------|-------------------------------------|
| Add Patient class           | FR-04, FR-05, FR-06, FR-08 | Accepted | Sufficient evidence                                           | Add patient class                   |
| Add Appointment class       | FR-07                      | Modified | Based upon the requirements, status chnage can be anattribute | Added status attribute to Appoitent |
| Add AppoitmentManager class | No evidence                | Rejected | Not enough evidence                                           | No change                           |

G) Python Skeletons
See Patient_class.py, Practitioner_Class.py, and Appointment_Clas.py

H) Consistency Check
They are consistent and do not implement full behaviour yet. 

Reflection 
What modelling decision was hardest?
Where did AI over-design?
What evidence supported your final choices?

Overall, the hardest part of this section of the project was just figuring out what needed to be accomplished. These 
tasks can come across so vague or use technical terminology when simple language can describe the problem just
the same. However, once I understood the problem or task I was faced with, there was no resistance. As for the 
over-designing AI, I'm not sure if I'm using the AI as intended as it never goes beyond the expectations I set for it - 
there was no over-designing. Almost everything it suggested was within reason - and while there were elements that 
did not fit the scope of this project I understood where the logic laid, as it was often an extension of what I had
foundationed; for example the management - appointment class. I had made mention that management was major element 
of this project, as are appointments - so there was the suggestion of having a management only class for appointments - 
which was vetoed. But there was no crazy beyond scope suggestions. As for the evidence I used to negotiate the final 
choices, I relied upon the case study and the expectations of the client to focus on the core of what the system needed,
and anything beyond that was considered to be useless. Using that information it was easy to negotiate AI's suggestions 
surrounding what should and should not be a class. 