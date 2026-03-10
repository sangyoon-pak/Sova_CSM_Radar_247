---
source: notebooklm_export
file_id: "017"
filename: "017_Appier TOMs_v1.1_20220427_EN.pdf.txt"
doc_type: "general"
product: "Appier"
content_type: "pdf"
language: "en"
guide_summary: "This document outlines Appier's comprehensive **Technical and Organizational Measures (TOMs)** designed to ensure the robust security and protection of personal data. Key principles include leveraging highly secure infrastructure from **Google Cloud Platform (GCP) and Amazon Web Services (AWS)** and enforcing strict protocols for data handling, such as **ISO 27001-compliant encryption** for both transmission and storage. The measures detail rigorous control systems for maintaining **confidential"
guide_keywords: "Service providers, Data protection, Access control, Availability recovery, Regular verification"
---

# 017 Appier TOMs v1.1 20220427 EN.pdf

TECHNICAL AND ORGANIZATIONAL MEASURES INCLUDING TECHNICAL AND ORGANIZATIONAL MEASURES TO ENSURE THE SECURITY OF THE DATA 
1. Service providers 
Infrastructure Appier uses the Google Cloud Platform (GCP) and Amazon Web Services (AWS) as its infrastructure providers. 
Both GCP and AWS meet the most stringent data protection and security requirements. 
Please refer to the following links for the security and privacy of our cloud service providers: 
GCP: https://cloud.google.com/security/compliance 
AWS: https://aws.amazon.com/tw/compliance/ 
2. Data protection and encryption 
Data handling after retention Deletion of personal data is performed by the following principles: 
 After the deletion is completed, the personal data files should not exist. 
 It is no longer possible to recover or backup personal data. 
 A designated employee is responsible for the deletion of the data. 
 The records of deletion are kept. 
Encryption Appier complies with ISO 27001 to implement compatible encryption for the transmission and the storage of personal data. 
Appier TOMs_v1.1
3. Confidentiality and integrity 
Equipment access control Measures designed to deny unauthorized person access to equipment used for processing personal data. 
Appier takes the following measures to ensure that unauthorized persons do not gain access to data processing systems in which data is processed: 
 Doors accessing the Secure Area shall be equipped with access control mechanisms, such as access cards or locks, to prevent unauthorized entry. 
 Access card to Secure Area can only be used as the application of its usage has been submitted and approved. Access cards shall be used in a manner that is consistent with the intended information processing activities. 
Clearly defined security concepts are in place for data processing and storage at AWS and GCP. 
Except for the access options provided to administrators as agreed with the client, access to the data centers in which the client's data are stored is impossible for employees. 
Access to the data centers is strictly controlled by the cloud service provider. The implemented measures include, but are not limited to: 
 Video surveillance 
 Movement sensors, intruder alarm system, and security for the premises 
 Division into safety zones / restricted areas 
 Identity check by the gatekeeper or security service 
 Full documentation and regular verification of any access granted 
User access control Appier follows strict policies to protect user access control, including the following: 
 System Administrators shall be separated into different roles based on their characteristics, such as development, testing, release, maintenance, and equipment management. 
 User accounts and passwords shall not be shared among personnel. 
 Accounts and their corresponding permissions shall be adjusted, 
disabled, or deleted when the personnel that uses them is no longer working in the same job capacity. 
 Accounts irrelevant to system operation or maintenance shall be deleted when the project or job is completed. 
 Physical access control devices other than accounts (i.e. IC card, USB key) shall be managed, restricted, and revoked in accordance with the policies established for user accounts. 
Appier TOMs_v1.1
 All accounts shall be used as authorized while appropriate audit trails are retained. 
Transfer control Measures designed to ensure that personal data cannot be read, copied, altered, or deleted without authorization during electronic transmission, transport, or storage on data carriers. These measures include: 
 Signing agreements with third parties before the third parties provide services to Appier, and ensure that the data duties of third parties are disclosed in the agreement. 
 When Appier shares data with the third parties, the contract between Appier and the third parties should include the data protection duties, data processing purposes and restrictions. 
 When transferring personal data due to business needs, encryption or other data security mechanisms should be implemented during the transfer. 
 Data sharing or transfer should comply with Appier's security policy. 
Input control Measures designed to ensure that it is subsequently possible to verify and establish whether and by whom personal data have been accessed, modified, or removed from data processing systems. 
The client’s transmitted data is recorded by the platform in an audit-proof manner. Any subsequent modification or deletion of the client's data is also recorded by the platform. These measures include: 
 When any application accessed by a user involves the collection, processing, and utilization of personal data, its additions, changes, deletions, and inquiries, regardless of the success or failure of the system's processing results, shall be recorded by the system. 
 The application system log storage location should be set up with an access authority control mechanism and read-only access for user accounts to prevent the log from being tampered with. 
Processing control Measures designed to ensure that all personal data processing is performed in compliance with Appier's fundamental personal data processing principles. These measures include: 
 Personal data processing should be legal, fair and transparent. 
 The purpose of personal data collection must be specific, explicit and legal. 
 The collection and processing of personal data must comply with the principle 
of data minimization. 
 The accuracy of personal data should be ensured. 
 The retention time of personal data should not be longer than the time 
necessary for processing purposes. 
 Personal data should be processed in a safe manner to prevent unauthorized 
or illegal processing, maintaining the integrity and confidentiality of personal data. 
Appier TOMs_v1.1
Separability Measures designed to ensure that personal data collected for different purposes can be processed separately (storage, modification, deletion, transmission). Among others, the following measures are implemented: 
 Data will be imported into the system and displayed according to their intended use. 
 Separation of data by client / customer 
 Separation of functions / production environment / test environment 
 Creation of an authorization concept 
4. Availability and recovery 
Measures designed to ensure that personal data are available and protected against accidental loss and destruction and that systems may, in the case of malfunctions, be restored. 
 Storage of data backup at a secure, external location 
 Regular checks on the functionality of the backup & recovery concept 
In addition to the measures taken by Appier, the cloud service provider also takes actions to serve the best of availability. 
Appier TOMs_v1.1
5. Data protection by default / Data 
protection by design 
With regard to privacy by default and privacy by design, Appier has established the privacy by design policy to ensure data protection. 
During the application, system, and product evaluation phase, developers should incorporate the "Privacy by Design Sheet" question into the design to ensure that relevant requirements can be met. 
During the application, system, and product testing phase, developers should test and complete the "Privacy by Design Sheet", and provide the form to Appier’s Data Protection Office after the test is completed. If there is any inapplicability in the process of filling in, the reason for inapplicability should be written. 
During the application, system, and product development, developers should ensure that application development is performed in accordance with the requirements of "Privacy by Design Sheet". 
6. Regular verification procedures 
Data protection office Appier has created a corporate data protection office whose main tasks include the development, implementation, and monitoring of a data protection management system and the regular monitoring of processing activities and data protection measures. 
Risk analysis A risk analysis is regularly carried out by the information security team to assess the current threat level and determine appropriate measures to be taken. 
Appier TOMs_v1.1
