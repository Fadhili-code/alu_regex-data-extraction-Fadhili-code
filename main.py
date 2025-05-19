#!/bin/python3
import re
#Sample texts containing data to extract 
sample_text = """
Reach us through our email at Fadhili@greatcompany.com or fadhili.lumumba@greatcompany.co.uk
Go to our website for more information; https://www.studentportal.com and https://student.portal.org/page
You can reach our customer service through the number (182)567-3928 or 928-893-0182 or 221.038.9827
Here are some HTML tags; <p>This is a paragraph</p> 
                        <div class="example">A div element</div>
                        <img src="image.jpg" alt="description">
The currency amounts we are working with are $20.33 and $1,927.78
"""

# Extract email addresses
def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

# Extract URLs
def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

# Extract phone numbers (multiple formats)
def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
# Extract HTML tags
def extract_HTML_tags(text):
    return re.findall(r'<[^>]+>', text)
# Extract currency amounts like $20.33 or $1,927.78
def extract_currency_amount(text):
    return re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)

# Run all extractions
if __name__ == "__main__":
    print("Running Extractions")   
    print(" Emails:", extract_emails(sample_text))
    print(" URLs:", extract_urls(sample_text))
    print(" Phone Numbers:", extract_phone_numbers(sample_text))
    print(" HTML tags:", extract_HTML_tags(sample_text))
    print(" Currency amount:", extract_currency_amount(sample_text))

#Edge case data
edge_case = """
Beracah.co.ke
https://writer.ke
075907
<image serc>
9348983
"""

#Running edge case data
if __name__=="__main__":
    print("Running edge case data")   
    print(" Emails:", extract_emails(edge_case)) 
    print(" URLs:", extract_urls(edge_case))
    print(" Phone Numbers:", extract_phone_numbers(edge_case))
    print(" HTML tags:", extract_HTML_tags(edge_case))
    print(" Currency amount:", extract_currency_amount(edge_case))
