import re
def validate_academic_email(email):
    m = re.search(r"^([a-z0-9._]+)@([a-z]+).([a-z.]+)$",email)
    if m and (m.groups()[-1] in ("res.in","edu")):
        # print(m.groups())
        return True
    else:
        return False

print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
print(validate_academic_email("vinod@gmail.com"))          # Output: False (invalid suffix)
print(validate_academic_email("ALICE@college.edu"))        # Output: False (contains uppercase letters)
print(validate_academic_email("bob@mit.edu.com"))          # Output: False (does not end in .edu or .res.in)
