# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Input to the function is guaranteed to be a single string.

#! Examples

#* Valid inputs:
#* 1.2.3.4
#* 123.45.67.89

#* Invalid inputs:
#* 1.2.3
#* 1.2.3.4.5
#* 123.456.78.90
#* 123.045.067.089

#TODO Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

#TODO THis one was my first solution
# def is_valid_IP(ip):
#     octt = ip.split('.')
#     if len(octt) != 4: return False
#     for octet in octt:
#         if not is_valid_octet(octet):
#             return False
#     return True

# def is_valid_octet(octet):
#     if not octet.isdigit():
#         return False
#     if len(octet) > 1 and octet[0] == '0':
#         return False
#     octet = int(octet)
#     if octet >= 0 and octet <= 255:
#         return True
#     else:
#         return False



#TODO Solution 2 (optimized)
def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4