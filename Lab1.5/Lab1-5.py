#
#
#
import glob
TXT = glob.glob("C:\\Users\\resu\\Desktop\\seafile\\Seafile\\p4ne_training\\config_files\\*.txt")

l = []
for x in TXT:
    f = open(x)
    lines = f.readlines()
    for s in lines:
        IPA = s.find("ip address")
        if IPA != -1:
            line = s.replace("ip address", "").strip()
            l.append(line)
            # print(IPA)
            # print(len(s.strip()))

for s in list(set(l)):
    #if
    print(s)
