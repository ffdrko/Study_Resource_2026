"""
1. 🔒 Mask Sensitive Data (NID/ID)

Hide part of sensitive information.
"""

nid_number = input("Enter your NID/ID number: ")

masked_nid = nid_number[:3] + '*' * 5 + nid_number[-3:]
print("Masked NID/ID number:", masked_nid)