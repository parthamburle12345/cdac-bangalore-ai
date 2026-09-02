import re
def scrape_directory_phones(directory_text):
    phone_book=[]
    m1 = re.findall(r"([0-9-()\s]{3,})",directory_text)
    # print(m1)
    for num in sorted(m1):
        phone_record,num = dict(),num.strip()
        values = re.findall(r"[0-9]{1,3}",num)      
        phone_record["area_code"] = values[0]
        phone_record["prefix"] = values[1]
        phone_record["line_number"] = values[2]+values[3]
        phone_record["formatted"] = f"({phone_record['area_code']}) {phone_record['prefix']}-{phone_record['line_number']}"
        phone_book.append(phone_record)
    return phone_book
directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
for item in scrape_directory_phones(directory):
    print(item)