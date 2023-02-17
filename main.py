def checkQC(string):
    n = 6
    no_s = '0123456789'
    zcount = 2

    if len(string) < n:
        print(1)
        return False
    if string[0] != 'Q':
        print(2)
        return False
    if 'p' not in string or 'd' not in string:
        print(3)
        return False
    no_of_tests = string[:2]
    if no_of_tests[1] == '0':
        return False

    s = string[2:]
    for i, c in enumerate(s):
        if c == 'p' or c == 'd':
            num = s[i+1]
            print(num)
            if num == '0':
                if i+2 > len(s)-1:
                    return False
                if s[i+2] in no_s:
                    return False
                else:
                    zcount -= 1
    if zcount == 0:
        return False

    return True

def isValidString(s):
  if 'Q' not in s:
    return False
  arr = s.split('Q')
  res = True
  for qc in arr[1:]:
    qc = 'Q'+qc
    res &= checkQC(qc)

  return res


print(isValidString('Q5d2p3'))