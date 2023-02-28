import ssl
from OpenSSL import SSL
from OpenSSL import crypto
from socket import *
import csv
from collections import Counter
from datetime import datetime


setdefaulttimeout(3)

org_names = []
time_ranges = []
time_only = []
countries = []
state_or_province = []
types_of_keys = []
types_with_len = []
types_with_exp = []
signatures = []
extensions = []

with open('tranco-top-1m.csv') as file:

#    print("To test, comment out all other problems besides the problem ")
#    print("of interest. If the comments don't specify what to set as ")
#    print("x in the line if (int(row[0]) <= x), please set x as 1000.")
#    print("Remember to also comment out the corresponding print section")
#    print("found at the bottom of the code. Thank you. ")

    file_reader = csv.reader(file, delimiter=',')
    for row in file_reader:
        if (int(row[0]) <= 50):
            try:
                server_host = row[1]
                server_address = (server_host, 443)
                cert = ssl.get_server_certificate(server_address)
                x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)

                subject = x509.get_subject()
    
                # PROBLEM 1
                # organization = subject.organizationName
                # if (organization == None):
                #     continue
                # org_names.append(organization)

                # PROBLEM 2
                # organization = subject.organizationName
                # valid_time_after = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
                # valid_time_before = datetime.strptime(x509.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
                # valid_time = round(float((valid_time_after - valid_time_before).total_seconds()) / 60 / 60 / 24, 2)
                # if (valid_time == None):
                #     continue
                # time_ranges.append([organization, valid_time])
                # time_only.append(valid_time)

                # PROBLEM 3
                # country = subject.C
                # if (country == None):
                #     continue
                # countries.append(country)

                # PROBLEM 4 (Note: change 1000 to 100 for this question)
                # st_or_p_name = subject.stateOrProvinceName
                # if (st_or_p_name == None):
                #     continue
                # state_or_province.append(st_or_p_name)

                # PROBLEM 5
                # pub_key = x509.get_pubkey()
                # type_of_key = pub_key.to_cryptography_key().__class__
                # types_of_keys.append(type_of_key)

                # PROBLEM 6
                # pub_key = x509.get_pubkey()
                # key_length = pub_key.bits()
                # type_of_key = pub_key.to_cryptography_key().__class__
                # types_with_len.append([type_of_key, key_length])

                # PROBLEM 7
                # organization = subject.organizationName
                # if (organization == None):
                #     continue
                # pub_key = x509.get_pubkey()
                # if (pub_key == None):
                #     continue
                # type_of_key = pub_key.to_cryptography_key().__class__
                # pk = pub_key.to_cryptography_key().public_numbers()
                # if (pub_key.type() == crypto.TYPE_RSA):
                #     types_with_exp.append([organization, "RSA", pk.e])

                # PROBLEM 8
                # signature1 = x509.get_signature_algorithm()
                # if (signature1 == None):
                #      continue
                # signatures.append(signature1)

                # PROBLEM 9
                # organization = subject.organizationName
                # if (organization == None):
                #     continue
                # amount = x509.get_extension_count()
                # extensions.append([organization, amount])

                # PROBLEM 10 (Note: change 1000 to 50)
                organization = subject.organizationName
                if (organization == None):
                    continue
                org_names.append(organization)
                
                # Extras
                #print("")
                #print("Website", row[0], ": ", organization)
                

            except (error, timeout) as err:
                continue

                # Extras
                #print("")
                #print("Website", row[0], ":", "No connection: {0}".format(err))
                  
        else:
            break

# PROBLEM 1
# x = Counter(org_names)
# # deletes entries that were issued only once
# for key, cnts in list(x.items()): 
#     if cnts < 2:
#         del x[key]
# print("Organization | # of Cert. Issued")
# for y in x.most_common():
#     print(y)

# PROBLEM 2
# a = sorted(time_ranges)
# for b in a:
#     print(b)
# print("Max: ", max(time_only))
# print("Min: ", min(time_only))

# PROBLEM 3
# c = Counter(countries)
# print(c.most_common(3))

# PROBLEM 4
# d = Counter(state_or_province)
# for e in d.most_common():
#     print(e)

# PROBLEM 5
# f = Counter(types_of_keys)
# for g in f.most_common():
#     print(g)

# PROBLEM 6
# for h in types_with_len:
#     print(h)

# PROBLEM 7
# for i in types_with_exp:
#     print(i)

# PROBLEM 8
# j = Counter(signatures)
# for k in j.most_common():
#     print(k)

# PROBLEM 9
# for k in extensions:
#     print(k)

# PROBLEM 10
x = Counter(org_names)
# deletes entries that were issued only once
for key, cnts in list(x.items()): 
    if cnts < 2:
        del x[key]
print("Organization | # of Cert. Issued")
for y in x.most_common():
    print(y)