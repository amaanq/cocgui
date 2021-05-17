import pyperclip, os

def e_mail():
    email = "old.txt"
    with open(email) as f:
        z = f.read()
        first = z[0:13]
        last = z[-11:]
        zz = z.split(first)
        zzz = zz[1].split(last)
        num = zzz[0]
        letter = num[0]
        nums = num[1:]
    alpha = [chr(i) for i in range(97, 123)]
    if int(nums) < 99:
        i_num = int(nums)+1
        nums = str(i_num)
    else:
        al = alpha.index(letter)
        al += 1
        letter = alpha[al]
        nums = '1'
    newmail = first+letter+nums+last
    pyperclip.copy(newmail)
    with open(email, 'w') as f:
        f.write(newmail)
