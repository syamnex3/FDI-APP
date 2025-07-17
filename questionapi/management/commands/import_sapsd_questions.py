import json
from django.core.management.base import BaseCommand
from questionapi.models import SAPSDQuestion
QUESTIONS = [
    {
        "question_id": "sap_sd_1",
        "question_text_full": "What does SAP SD stand for?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "SAP SD Basics",
        "options": [
            "Systems Applications and Products in Sales and Development",
            "Sales and Distribution",
            "Systems Applications and Products in Sales and Distribution",
            "Service Delivery"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_2",
        "question_text_full": "Which of the following is a key component of the sales order process in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-45",
        "topic": "Sales Order Process",
        "options": [
            "Creating a purchase requisition",
            "Creating a sales order",
            "Generating a production order",
            "Performing financial closing"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_3",
        "question_text_full": "In SAP SD, what is the purpose of a customer master record?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Master Data",
        "options": [
            "To store product inventory levels",
            "To maintain vendor information",
            "To store all customer-related data",
            "To record sales employee performance"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_4",
        "question_text_full": "Which document follows the sales order in a typical SAP SD sales process flow?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-45",
        "topic": "Sales Process Flow",
        "options": [
            "Invoice",
            "Goods Receipt",
            "Delivery",
            "Purchase Order"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_5",
        "question_text_full": "What is the primary function of a pricing procedure in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Pricing",
        "options": [
            "To determine the shipping route",
            "To calculate the final price of goods and services",
            "To manage customer credit limits",
            "To track production progress"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_6",
        "question_text_full": "Which organizational element in SAP SD represents the legal entity responsible for sales?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Organizational Structure",
        "options": [
            "Sales Organization",
            "Sales Office",
            "Shipping Point",
            "Distribution Channel"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sap_sd_7",
        "question_text_full": "What is the purpose of a material master record in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Master Data",
        "options": [
            "To store customer addresses",
            "To store information about products and materials",
            "To track financial transactions",
            "To manage employee payroll"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_8",
        "question_text_full": "Which of the following is a common sales document type in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Sales Documents",
        "options": [
            "Purchase Order",
            "Sales Order",
            "Invoice Receipt",
            "Material Document"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_9",
        "question_text_full": "What is the function of a 'shipping point' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Organizational Structure",
        "options": [
            "To define customer payment terms",
            "To determine the location from which goods are shipped",
            "To manage sales quotas for employees",
            "To record customer complaints"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_10",
        "question_text_full": "Which module does SAP SD integrate most closely with for accounting purposes?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Integration",
        "options": [
            "Production Planning (PP)",
            "Materials Management (MM)",
            "Financial Accounting (FI)",
            "Human Resources (HR)"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_11",
        "question_text_full": "What is a 'condition type' used for in SAP SD pricing?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Pricing",
        "options": [
            "To define sales areas",
            "To represent specific price elements like discounts, surcharges, or freight",
            "To categorize customer groups",
            "To manage material availability"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_12",
        "question_text_full": "Which step typically occurs after 'goods issue' in the sales process?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-45",
        "topic": "Sales Process Flow",
        "options": [
            "Sales Order Creation",
            "Delivery Creation",
            "Billing/Invoice Creation",
            "Credit Check"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_13",
        "question_text_full": "What is the purpose of a 'route' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Logistics",
        "options": [
            "To define the sales hierarchy",
            "To determine the transportation path for goods",
            "To manage customer credit limits",
            "To categorize materials"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_14",
        "question_text_full": "Which of the following is an example of a 'sales area'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Organizational Structure",
        "options": [
            "A specific customer's address",
            "A combination of Sales Organization, Distribution Channel, and Division",
            "A single product group",
            "A financial reporting segment"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_15",
        "question_text_full": "What is the role of 'availability check' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Availability Check",
        "options": [
            "To check if the customer has sufficient credit",
            "To determine if the requested materials are available for delivery",
            "To verify the correctness of the sales order price",
            "To confirm the customer's address"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_16",
        "question_text_full": "Which of the following is NOT an organizational element in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Organizational Structure",
        "options": [
            "Company Code",
            "Sales Area",
            "Storage Location",
            "Profit Center"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "sap_sd_17",
        "question_text_full": "What is the primary purpose of a 'sales document header' in a sales order?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Sales Documents",
        "options": [
            "To store line item specific data",
            "To contain overall information applicable to the entire sales document",
            "To determine material availability for each item",
            "To manage individual customer payment terms"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_18",
        "question_text_full": "In the sales process, what is the 'Goods Issue' step responsible for?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-45",
        "topic": "Sales Process Flow",
        "options": [
            "Creating the customer invoice",
            "Recording the physical departure of goods from the warehouse",
            "Performing a credit check on the customer",
            "Confirming the sales order"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_19",
        "question_text_full": "What is the main function of 'Sales Group' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Organizational Structure",
        "options": [
            "To define a group of customers",
            "To group sales employees for reporting and management",
            "To categorize materials for sales",
            "To define different distribution channels"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_20",
        "question_text_full": "Which master data record contains information about payment terms, shipping conditions, and pricing procedures related to a customer?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Master Data",
        "options": [
            "Material Master",
            "Customer Master",
            "Vendor Master",
            "Condition Record"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_21",
        "question_text_full": "What is a 'Division' used for in the SAP SD organizational structure?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Organizational Structure",
        "options": [
            "To represent a geographical sales territory",
            "To group materials or services by product line",
            "To define a specific sales office location",
            "To identify a legal entity within the company"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_22",
        "question_text_full": "When an invoice is created in SAP SD, which module is primarily updated with the revenue and accounts receivable postings?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SAP SD",
        "points": "5",
        "time": "0-30",
        "topic": "Integration",
        "options": [
            "Materials Management (MM)",
            "Production Planning (PP)",
            "Financial Accounting (FI)",
            "Controlling (CO)"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_23",
        "question_text_full": "What is the significance of a 'Shipping Type' in a delivery document?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Delivery Processing",
        "options": [
            "It determines the material's packaging",
            "It defines how the shipment is processed (e.g., standard, collective)",
            "It specifies the exact delivery date for each item",
            "It manages the picking process in the warehouse"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_24",
        "question_text_full": "Which of these is typically NOT a part of the standard 'Order-to-Cash' (OTC) cycle in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Order-to-Cash Cycle",
        "options": [
            "Sales Order Creation",
            "Production Order Creation",
            "Delivery Processing",
            "Billing"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_25",
        "question_text_full": "What is the purpose of a 'Sales BOM' (Bill of Material) in its simplest form in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "7",
        "time": "1-00",
        "topic": "Bill of Material (BOM)",
        "options": [
            "To list all the components required for manufacturing a product.",
            "To group materials together for sale as a single unit or kit.",
            "To calculate the total value of all sales orders.",
            "To track the status of customer complaints."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_26",
        "question_text_full": "Explain the concept of 'item categories' in SAP SD and provide an example.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Item Categories",
        "options": [
            "Item categories determine the type of customer in a sales order, e.g., domestic or international.",
            "Item categories control the processing of each item in a sales document, influencing pricing, billing relevance, and delivery. An example is 'TAN' for standard items.",
            "Item categories define the storage location of materials in the warehouse, e.g., 'FG' for finished goods.",
            "Item categories specify the payment terms for an item, e.g., 'Net 30'."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_27",
        "question_text_full": "Describe the purpose of 'schedule line categories' in SAP SD and their relationship with item categories.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Schedule Line Categories",
        "options": [
            "Schedule line categories define the credit limit for each customer, linked to the customer's risk profile.",
            "Schedule line categories determine when and how material is to be delivered, influencing requirements transfer and availability check. They are proposed based on the item category and MRP type.",
            "Schedule line categories define the sales employee responsible for an item, based on the item's profitability.",
            "Schedule line categories specify the pricing conditions applied to an item, overriding the pricing procedure."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_28",
        "question_text_full": "How does 'copy control' function in SAP SD, and why is it important?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Copy Control",
        "options": [
            "Copy control allows copying entire sales orders from one customer to another, simplifying order entry for repeat customers.",
            "Copy control defines which data is copied from a source document to a target document in the sales process, ensuring data consistency and process flow. For example, copying order data to delivery.",
            "Copy control manages the replication of master data records across different company codes, ensuring data synchronization.",
            "Copy control enables users to copy pricing conditions from one material to another, speeding up pricing setup."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_29",
        "question_text_full": "Explain the role of 'account determination' in SAP SD and its integration with FI.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Account Determination",
        "options": [
            "Account determination defines the customer's bank account details for incoming payments.",
            "Account determination is the process of automatically finding the correct G/L accounts in Financial Accounting (FI) to post revenues, discounts, and surcharges from sales transactions, based on various criteria.",
            "Account determination sets up the credit limits for customers based on their payment history.",
            "Account determination specifies the sales organization responsible for a particular region."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_30",
        "question_text_full": "What is the significance of 'condition technique' in SAP SD pricing?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Condition Technique",
        "options": [
            "It is a method to manage customer master data, ensuring data quality.",
            "It is a flexible and powerful tool used to determine prices, discounts, and surcharges based on various criteria, allowing for complex pricing scenarios through access sequences and condition records.",
            "It is a technique for checking material availability during order creation.",
            "It is used to control the flow of documents in the sales process."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_31",
        "question_text_full": "Differentiate between 'sales order type' and 'delivery type' in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Sales Document Types",
        "options": [
            "Sales order type defines the customer's preferred delivery method, while delivery type defines the payment terms.",
            "Sales order type categorizes the nature of a sales transaction (e.g., standard, return, cash sales) and controls its processing, while delivery type defines the characteristics and processes of an outbound delivery document (e.g., standard delivery, returns delivery).",
            "Sales order type specifies the product category being sold, while delivery type indicates the shipping carrier.",
            "Sales order type determines the sales organization, while delivery type determines the shipping point."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_32",
        "question_text_full": "Explain the concept of 'text determination' in SAP SD and its benefits.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Text Determination",
        "options": [
            "Text determination defines the font and style of text displayed in sales documents for better readability.",
            "Text determination allows for automatic inclusion of relevant texts (e.g., delivery instructions, terms and conditions) into sales documents from various master data or custom texts, improving communication and reducing manual effort.",
            "Text determination is used to translate sales document texts into different languages for international customers.",
            "Text determination checks the grammar and spelling of text entered in sales documents."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_33",
        "question_text_full": "What is the purpose of 'partner determination' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Partner Determination",
        "options": [
            "To determine the appropriate shipping carrier for a delivery.",
            "To automatically identify and assign relevant business partners (e.g., sold-to, ship-to, bill-to, payer) to sales documents based on master data settings, ensuring proper roles in the sales process.",
            "To determine the pricing procedure for a sales order.",
            "To identify the material's manufacturing plant."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_34",
        "question_text_full": "How does 'route determination' work in SAP SD, and what factors influence it?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Route Determination",
        "options": [
            "Route determination calculates the optimal pricing for a sales order based on the customer's location.",
            "Route determination automatically proposes the most suitable transportation route for a delivery based on factors like shipping point, destination country/region, transportation group of material, and shipping conditions.",
            "Route determination identifies the shortest path for a sales employee to visit customers.",
            "Route determination verifies the material's availability in different warehouses."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_35",
        "question_text_full": "Explain the concept of 'credit management' in SAP SD and its purpose.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Credit Management",
        "options": [
            "Credit management tracks customer loyalty points and rewards.",
            "Credit management is the process of controlling and monitoring customer credit exposure to mitigate financial risks, preventing sales to customers who exceed their credit limits or have poor payment history.",
            "Credit management is used to grant discounts to customers based on their purchase volume.",
            "Credit management determines the delivery schedule for an order."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_36",
        "question_text_full": "What is the difference between a 'customer inquiry' and a 'customer quotation' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Sales Documents",
        "options": [
            "An inquiry is a formal offer to sell, while a quotation is a customer's request for information.",
            "An inquiry is a customer's request for information about products or services, not legally binding. A quotation is a legally binding offer from the seller to the customer for specific goods/services at defined prices and conditions.",
            "An inquiry is used for internal communication, while a quotation is for external communication.",
            "An inquiry records a customer complaint, while a quotation records a return request."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_37",
        "question_text_full": "Describe the purpose of 'billing documents' in SAP SD and their impact.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Billing Documents",
        "options": [
            "Billing documents initiate the production process for goods.",
            "Billing documents are used to create invoices for customers, debit/credit memos, or proforma invoices. They are crucial for revenue recognition and posting to Financial Accounting (FI).",
            "Billing documents track the physical movement of goods from the warehouse.",
            "Billing documents manage customer master data updates."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_38",
        "question_text_full": "Explain the concept of 'rebate processing' in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Rebate Processing",
        "options": [
            "Rebate processing manages discounts offered to customers at the time of sale.",
            "Rebate processing involves the calculation and settlement of retrospective payments to customers or customer groups based on agreed sales volumes or purchase values over a specific period, typically after sales have occurred.",
            "Rebate processing handles customer returns and refunds.",
            "Rebate processing controls the availability of materials for sale."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_39",
        "question_text_full": "What is the purpose of 'customer hierarchy' in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Customer Hierarchy",
        "options": [
            "To define the hierarchy of products within a material group.",
            "To structure customers into a hierarchical tree based on their relationships (e.g., head office, subsidiaries), enabling aggregated reporting, pricing, and partner determination based on the hierarchy.",
            "To prioritize customer orders based on urgency.",
            "To manage the credit limits of individual customers."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_40",
        "question_text_full": "How does 'output determination' function in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Output Determination",
        "options": [
            "Output determination calculates the net value of the sales order.",
            "Output determination is the process of identifying and generating various outputs (e.g., order confirmations, invoices, shipping notifications) automatically for sales and distribution documents, based on condition records and output types.",
            "Output determination specifies the production output of a manufacturing plant.",
            "Output determination manages the inventory levels of finished goods."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_41",
        "question_text_full": "Explain the impact of 'sales document pricing procedure determination' on pricing in a sales order.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Pricing Procedure Determination",
        "options": [
            "It directly assigns fixed prices to all materials in the order.",
            "It defines the sequence of condition types that the system will search for to calculate the price.",
            "It determines which sales organization is responsible for the pricing.",
            "It sets the default currency for the sales order."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_42",
        "question_text_full": "How does 'incompletion log' functionality in SAP SD assist users?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Incompletion Log",
        "options": [
            "It provides a list of all completed sales orders for reporting.",
            "It identifies missing or incomplete data in sales documents, preventing further processing until corrected.",
            "It records customer payment failures for credit management.",
            "It logs system errors during sales order creation."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_43",
        "question_text_full": "What is the role of 'delivery blocks' and 'billing blocks' in SAP SD, and when are they typically used?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Blocks (Delivery/Billing)",
        "options": [
            "They prevent material availability checks and are used for old, archived documents.",
            "They stop deliveries or billing from being processed for a sales document, often used for credit hold, incomplete data, or quality issues.",
            "They mark documents for immediate processing regardless of other checks.",
            "They are used to block certain customers from receiving marketing communications."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_44",
        "question_text_full": "Describe the standard 'document flow' functionality in SAP SD and its importance.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Document Flow",
        "options": [
            "It is a graphical representation of the physical path goods take during delivery.",
            "It shows the sequence of linked documents (e.g., inquiry, quotation, order, delivery, invoice) and their processing status, ensuring traceability and transparency.",
            "It controls the data transfer between different SAP modules.",
            "It defines the authorization levels for users to access sales documents."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_45",
        "question_text_full": "When setting up pricing, differentiate between 'condition records' and 'condition tables'.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Pricing",
        "options": [
            "Condition records define the structure of pricing data, while condition tables store the actual price values.",
            "Condition records store the actual price values, discounts, or surcharges for specific criteria (e.g., material, customer), while condition tables define the combination of fields (access key) used to store and retrieve these records.",
            "Condition records are for gross prices, and condition tables are for net prices.",
            "Condition records are for sales orders, and condition tables are for billing documents."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_46",
        "question_text_full": "Explain the 'splitting criteria' in delivery and billing documents and why it's used.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Document Splitting",
        "options": [
            "It allows a single sales order to be split into multiple items.",
            "It determines when one sales order creates multiple deliveries or one delivery creates multiple invoices, based on differing criteria like shipping point, route, or payment terms.",
            "It splits the workload evenly among sales employees.",
            "It divides a large customer into smaller sub-customers."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_47",
        "question_text_full": "What is the purpose of 'release strategies' in SAP SD, particularly for sales documents?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Release Strategies",
        "options": [
            "To release materials from production for sales.",
            "To implement an approval workflow for sales documents (e.g., orders, quotations) that exceed certain value limits or meet specific criteria, ensuring managerial oversight.",
            "To release customer credit limits for higher sales volumes.",
            "To release blocked customers for new sales orders."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_48",
        "question_text_full": "How do 'pricing scales' function within the condition technique, and what are their types?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Pricing Scales",
        "options": [
            "They adjust prices based on the customer's loyalty points.",
            "They allow for different prices or discounts based on quantity, value, or weight. Types include 'To' scales (up to a certain quantity) and 'From' scales (from a certain quantity).",
            "They measure the effectiveness of a sales promotion.",
            "They determine the sales area for a specific material."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_49",
        "question_text_full": "Describe the significance of 'Consignment Processing' in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Consignment Processing",
        "options": [
            "It refers to selling goods directly to end consumers.",
            "It involves the vendor (your company) providing goods to the customer, who stores them but only takes ownership (and is billed) when the goods are consumed or sold to their end-customer.",
            "It is a process for returning defective goods from a customer.",
            "It manages the production and delivery of customized products."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_50",
        "question_text_full": "What are 'Customer Exits' or 'BAdIs' in the context of SAP SD, and why are they important for customization?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "10",
        "time": "1-30",
        "topic": "Customization",
        "options": [
            "Predefined reports that users can run to analyze customer data.",
            "Standard SAP functions that allow users to exit a transaction.",
            "Specific points in SAP's standard code where customers can insert their own custom logic without modifying standard SAP programs, allowing for enhanced functionality and business-specific requirements.",
            "Automated emails sent to customers when a sales order is completed."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sap_sd_51",
        "question_text_full": "Elaborate on the complexities and configuration steps involved in 'third-party order processing' in SAP SD, including its integration points with MM and FI.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Third-Party Order Processing",
        "options": [
            "Third-party order processing involves selling goods directly from the vendor to the customer without passing through the company's stock. It requires specific sales document types, item categories (e.g., TAS), and schedule line categories (e.g., CS). Integration with MM involves automatic purchase requisition/order creation, and with FI for invoice verification and vendor payments.",
            "Third-party order processing is used when a customer pays a third-party logistics provider for delivery.",
            "Third-party order processing is a method for selling services provided by external consultants.",
            "Third-party order processing refers to sales where the customer uses a third-party credit card for payment."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sap_sd_52",
        "question_text_full": "Discuss the various 'intercompany sales' scenarios in SAP SD and the key configuration elements required for each.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Intercompany Sales",
        "options": [
            "Intercompany sales only involve selling between different divisions within the same company code.",
            "Intercompany sales occur when one company code sells goods to a customer, and another company code within the same corporate group supplies those goods. Scenarios include cross-company code sales (plant in supplying CC, sales organization in ordering CC) and intercompany stock transfer orders. Key configurations involve intercompany billing, partner functions, and pricing conditions.",
            "Intercompany sales refer to sales made to international customers with different legal entities.",
            "Intercompany sales are simplified sales processes for internal employees to purchase goods."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_53",
        "question_text_full": "Explain the concept of 'revenue recognition' in SAP SD, detailing the differences between event-based and time-based recognition.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Revenue Recognition",
        "options": [
            "Revenue recognition determines when a customer's payment is due.",
            "Revenue recognition is the process of recognizing revenue in FI based on specific criteria. Event-based recognition recognizes revenue upon a specific event (e.g., goods issue, billing). Time-based recognition distributes revenue over a period (e.g., for service contracts). It involves configuration in SD (e.g., billing plans) and FI (e.g., account determination).",
            "Revenue recognition tracks the profitability of individual sales orders.",
            "Revenue recognition is only applicable to service contracts, not product sales."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_54",
        "question_text_full": "Discuss the integration of 'Variant Configuration' with SAP SD for configurable products.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Variant Configuration",
        "options": [
            "Variant Configuration allows for defining different sales areas based on product variations.",
            "Variant Configuration (VC) enables the sale of complex, customizable products where customers choose specific features and options. In SD, this involves creating configurable materials, defining characteristics and dependencies, and using VC-specific item categories and pricing procedures to determine the correct product and price based on customer selections.",
            "Variant Configuration is used to determine the optimal shipping route for different product variants.",
            "Variant Configuration is a tool for managing customer credit limits for complex products."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_55",
        "question_text_full": "Elaborate on the functionality of 'Sales BOM (Bill of Material)' in SAP SD and its use cases.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Sales BOM",
        "options": [
            "A Sales BOM is used to define the components required to manufacture a product.",
            "A Sales BOM allows for selling a group of materials as a single sales item (header material) while individually listing and possibly pricing its components in the sales order, which can be relevant for kits or sets. It can be for sales order processing only or delivery-relevant.",
            "A Sales BOM is a list of all sales employees and their respective sales targets.",
            "A Sales BOM defines the packing materials required for a delivery."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_56",
        "question_text_full": "Discuss the integration aspects of 'SD-FI-CO (Controlling)' and how profitability analysis (CO-PA) is impacted by SD transactions.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "SD-FI-CO Integration",
        "options": [
            "SD-FI-CO integration focuses solely on transferring customer master data from SD to FI and CO.",
            "SD-FI-CO integration ensures that sales transactions generate accurate financial postings in FI (revenue, receivables) and provide detailed profitability information in CO-PA by transferring relevant characteristics (e.g., customer, product, sales organization) and value fields (e.g., revenue, cost of goods sold).",
            "SD-FI-CO integration is primarily for managing employee expenses related to sales activities.",
            "SD-FI-CO integration is only relevant for intercompany sales scenarios."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_57",
        "question_text_full": "Explain the concept of 'Special Stock Types' in SAP SD and provide examples of their use.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Special Stock Types",
        "options": [
            "Special stock types categorize materials based on their physical characteristics (e.g., hazardous materials).",
            "Special stock types define materials that are not owned by the company but are managed in its inventory, or materials that are owned by the company but held at a different location (e.g., consignment stock at customer, customer's own material provided for processing).",
            "Special stock types are used for materials that are highly valuable and require extra security measures.",
            "Special stock types determine if a material is available for sale to specific customer groups."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_58",
        "question_text_full": "Describe the 'Availability Check (ATP)' logic in SAP SD, including its various methods and configuration.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Availability Check (ATP)",
        "options": [
            "ATP only checks current physical stock levels.",
            "Availability Check (ATP) determines if a material is available for delivery on the requested date by considering current stock, planned receipts (e.g., purchase orders, production orders), and planned issues (e.g., sales orders, reservations). Methods include 'Check against Planning' (e.g., PP/DS) and 'Check against ATP logic' (e.g., standard R/3 ATP logic with checking rules and scope of check).",
            "ATP is used to automatically determine the selling price of a product.",
            "ATP checks the customer's credit score before confirming an order."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_59",
        "question_text_full": "Elaborate on the configuration and business implications of 'Returns Processing' in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Returns Processing",
        "options": [
            "Returns processing is only for defective materials.",
            "Returns processing manages the entire lifecycle of a customer return, from creating a returns order (e.g., RE document type) and goods receipt into returns stock, to quality inspection, refunds/credit memo creation, and material disposition. Key configurations include returns order types, item categories, delivery types, and billing types for credit memos.",
            "Returns processing calculates the sales commissions for returned items.",
            "Returns processing automates the repacking of returned goods for resale."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_60",
        "question_text_full": "Discuss the role of 'Sales Deals and Promotions' in SAP SD and their configuration using the condition technique.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Sales Deals and Promotions",
        "options": [
            "Sales deals and promotions are used to track sales employee performance.",
            "Sales deals and promotions allow for temporary, targeted pricing, discounts, or free goods offers to stimulate sales. They are configured using the condition technique with specific condition types (e.g., for promotions, free goods) and condition records, often linked to a sales promotion definition.",
            "Sales deals and promotions define the geographic areas for sales operations.",
            "Sales deals and promotions manage long-term customer contracts and agreements."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_61",
        "question_text_full": "Elaborate on the capabilities of 'Service Management' within SAP SD (or integration with CS/SM) for service-related processes.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Service Management",
        "options": [
            "Service Management in SD only handles material returns for service items.",
            "Service Management in SAP SD (often through integration with the Customer Service (CS) or Service Management (SM) modules) supports service requests, service contracts, service orders, resource planning, and billing for services, differing from physical goods sales.",
            "Service Management determines the optimal transportation route for service technicians.",
            "Service Management is solely for managing external vendor services."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_62",
        "question_text_full": "Describe the use of 'Bills of Exchange' and 'Letter of Credit' functionalities in SAP SD for international sales.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "International Sales",
        "options": [
            "Bills of Exchange and Letters of Credit are methods for managing customer complaints.",
            "Bills of Exchange are negotiable instruments used to facilitate payments, allowing a seller to draw on a buyer's bank. Letters of Credit are bank guarantees ensuring payment to the seller if certain conditions are met. Both reduce payment risk in international trade and require specific configuration and integration with FI/Treasury.",
            "Bills of Exchange and Letters of Credit define the terms for material availability checks.",
            "Bills of Exchange and Letters of Credit are used to define sales territories."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_63",
        "question_text_full": "How does 'Batch Management' integrate with SAP SD for materials that require traceability?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Batch Management",
        "options": [
            "Batch Management helps determine the optimal sales price for a product.",
            "Batch Management assigns unique batch numbers to materials to track their origin, characteristics, and expiration dates. In SD, this impacts material availability checks (ATP), delivery picking strategies (e.g., FIFO, LIFO), and ensures traceability for recalls or quality issues by managing batch-specific stock and assignments in sales orders and deliveries.",
            "Batch Management is used to group customers for marketing campaigns.",
            "Batch Management automates the creation of sales orders for recurring customers."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_64",
        "question_text_full": "Explain 'Sales Information System (SIS)' and its relevance for sales reporting and analysis in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Sales Information System (SIS)",
        "options": [
            "SIS is primarily used for managing sales employee travel expenses.",
            "Sales Information System (SIS) is a reporting tool within SAP Logistics Information System (LIS) that provides summarized data on sales, deliveries, and billing, enabling sales managers to analyze sales trends, customer performance, and product profitability through standard reports and flexible analyses.",
            "SIS is a system for creating sales proposals for customers.",
            "SIS helps in the creation of new sales organizational units."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_65",
        "question_text_full": "Discuss the integration of 'SD with EWM (Extended Warehouse Management)' and its benefits for complex warehouse processes.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "SD-EWM Integration",
        "options": [
            "SD-EWM integration is solely for managing vendor consignment stock.",
            "SD integrates with EWM for highly optimized and complex warehouse processes, including wave management, yard management, cross-docking, and advanced picking/putaway strategies. When a delivery is created in SD, it's distributed to EWM, which then orchestrates the detailed warehouse tasks and confirms goods issue back to SD/ECC.",
            "SD-EWM integration is used to define new pricing conditions for warehouse services.",
            "SD-EWM integration automates the creation of sales orders based on warehouse stock levels."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_66",
        "question_text_full": "Elaborate on the intricacies of 'Account Assignment Categories' in sales orders and their role in integrating SD with CO-PA and PS (Project Systems).",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Account Assignment Categories",
        "options": [
            "Account Assignment Categories only dictate the G/L account for revenue posting.",
            "They determine how costs and revenues for an item are distributed to a controlling object (e.g., cost center, WBS element, sales order cost object, profitability segment), enabling detailed financial tracking and integration with CO-PA for profitability analysis and PS for project-related sales.",
            "They define the specific bank account for customer payments.",
            "They are used to assign a sales order to a specific sales group for reporting."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_67",
        "question_text_full": "Discuss the configuration and business implications of 'Free Goods Determination' in SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Free Goods Determination",
        "options": [
            "Free goods determination only allows for giving away marketing samples.",
            "It allows offering additional quantities of a product or a different product for free based on certain conditions (e.g., buying a specific quantity). Configuration involves condition types, access sequences, and condition records, enabling inclusive (free goods form part of the main item) or exclusive (free goods are separate items) rules.",
            "Free goods determination ensures that all goods are free of defects before delivery.",
            "Free goods determination manages the return process for complimentary items."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_68",
        "question_text_full": "Explain the concept of 'Resource-Related Billing' (RRB) in SAP SD, often used in conjunction with Project Systems (PS) or Customer Service (CS).",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Resource-Related Billing (RRB)",
        "options": [
            "RRB is a simple billing process for standard product sales.",
            "RRB allows for billing based on actual costs incurred (e.g., materials, labor, travel expenses) from a project or service order, by creating dynamic item proposals from expenditure records, making it ideal for complex service scenarios or large projects.",
            "RRB optimizes the allocation of warehouse resources for deliveries.",
            "RRB focuses on billing for human resources involved in sales activities."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_69",
        "question_text_full": "How does 'SD-MM Integration for Returns' handle different stock types and subsequent processes (e.g., Blocked Stock, Quality Inspection)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "SD-MM Integration (Returns)",
        "options": [
            "It only allows returns to unrestricted stock.",
            "SD returns processing, in conjunction with MM, allows goods to be received into various stock types (e.g., returns stock, blocked stock, quality inspection stock) upon goods receipt from a customer return order. This triggers specific follow-up actions like quality inspection, material analysis, and subsequent dispositioning (e.g., scrap, put into unrestricted use, return to vendor).",
            "It solely determines the financial credit memo amount for returns.",
            "It only manages returns for materials purchased from external vendors."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_70",
        "question_text_full": "Describe the functionality and benefits of 'Settlement Management (BRFplus)' in SAP S/4HANA for complex condition contracts (e.g., rebates, commissions).",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Settlement Management (BRFplus)",
        "options": [
            "Settlement Management simplifies the creation of basic sales orders.",
            "Settlement Management (leveraging BRFplus for rule determination) provides a robust framework in S/4HANA for managing and settling complex, periodic incentives and agreements (like rebates, commissions, chargebacks) through condition contracts, offering enhanced transparency, automation, and integration compared to traditional rebate processing.",
            "It is used to settle disputes between sales employees.",
            "It focuses on settling outstanding customer invoices quickly."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_71",
        "question_text_full": "Discuss the impact of 'Output Management with BRFplus' in SAP S/4HANA on output determination compared to the traditional NAST-based method.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Output Management (BRFplus)",
        "options": [
            "BRFplus only generates simple printouts.",
            "BRFplus in S/4HANA provides a more flexible, rule-based framework for output determination, replacing the traditional NAST table. It allows for more complex conditions, better extensibility, and simplified maintenance of output rules, impacting generation of invoices, confirmations, etc., as emails, printouts, or EDI.",
            "It is used for managing production output in manufacturing.",
            "It determines the best sales channel for a product."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_72",
        "question_text_full": "Explain the functionality of 'Global ATP (gATP)' in SAP S/4HANA and its advantages over classic ATP for complex supply chains.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Global ATP (gATP)",
        "options": [
            "gATP only checks stock at a single plant.",
            "Global ATP (gATP) in S/4HANA (part of SAP APO/IBP integration) provides advanced availability checking capabilities across a complex supply chain, considering multiple plants, alternative products/locations, and production capacities. It offers features like Capable-to-Promise (CTP), Multi-Level ATP, and Rule-Based ATP, leading to more accurate delivery promises.",
            "gATP is a tool for managing customer master data globally.",
            "gATP automatically generates intercompany billing documents."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_73",
        "question_text_full": "How does 'Preliminary Billing Documents' (PBDs) improve the flexibility and efficiency of the billing process in SAP SD?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Preliminary Billing Documents (PBDs)",
        "options": [
            "PBDs are only used for creating proforma invoices.",
            "PBDs allow for the creation and simulation of billing documents before final posting to accounting. This enables checking prices, taxes, and other billing elements, making corrections, and getting approvals, improving efficiency and accuracy before the final invoice is generated.",
            "PBDs are used to block billing for certain customers.",
            "PBDs automatically create sales orders from external systems."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_74",
        "question_text_full": "Discuss the role of 'Sales Contracts' (Quantity, Value, Service) and 'Scheduling Agreements' in recurring business processes within SAP SD.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "Sales Contracts & Scheduling Agreements",
        "options": [
            "These documents are only used for one-time sales.",
            "Sales Contracts (Quantity, Value, Service) are long-term agreements with customers for a specific quantity, value, or period of service, leading to subsequent release orders. Scheduling Agreements are highly detailed long-term agreements for delivering quantities of a material on specific dates over a period, streamlining repetitive deliveries without individual sales orders.",
            "They are primarily for internal communication regarding sales targets.",
            "They are used to manage customer credit limits over long periods."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sap_sd_75",
        "question_text_full": "Elaborate on the significance of 'SD document category' and 'transaction group' in controlling the behavior and processing of sales documents.",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SAP SD",
        "points": "15",
        "time": "2-00",
        "topic": "SD Document Category & Transaction Group",
        "options": [
            "They define the physical document format for printing.",
            "The 'SD document category' (e.g., C for Order, M for Invoice) broadly classifies the business transaction, influencing document flow and allowed follow-on functions. The 'transaction group' (e.g., 0 for inquiry, 1 for order) further refines control, impacting screen layout, field selection, and overall processing logic for the document type.",
            "They determine the sales organization and distribution channel.",
            "They control the authorization for users to create or change sales documents."
        ],
        "correct_answers": [1]
    }
]



class Command(BaseCommand):
    help = 'Import SAP SD questions from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        for item in QUESTIONS:
            SAPSDQuestion.objects.update_or_create(
                question_id=item['question_id'],
                defaults={
                    'question_text_full': item['question_text_full'],
                    'question_type': item['question_type'],
                    'difficulty': item['difficulty'],
                    'depth_of_knowledge': item['depth_of_knowledge'],
                    'domain': item['domain'],
                    'points': item['points'],
                    'time': item['time'],
                    'topic': item['topic'],
                    'options': item['options'],
                    'correct_answers': item['correct_answers'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported SAP SD questions'))