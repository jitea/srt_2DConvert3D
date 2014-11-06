#coding:utf8

#srt格式 2d字幕转3d左右

import re,sys

re_index = re.compile(r"^\d+$")#1
re_time = re.compile(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$")#00:02:50,545 --> 00:02:52,752


def textType(text):
    '''
    text 是序号 返回 1
    text 是时间 返回 2
    text 是空行 返回 3
    其它返回 4
    '''
    match = re_index.findall(text)
    if match:
        return 1
    match = re_time.findall(text)
    if match:
        return 2
    if text == '\n' or text == '\r\n':
        return 3
    return 4
def right(MaxIndex):
    if len(sys.argv) != 2:
        print sys.argv[0] + ' ' + '*.srt'
    fp_2d = open(sys.argv[1], "r")
    fp_3d = open(sys.argv[1] + "_3d.srt", "a+")
    flag = False
    for line in fp_2d:
        Type = textType(line)
        if Type == 1:
            flag = True
            MaxIndex += 1
            print line, MaxIndex
            fp_3d.write(str(MaxIndex) + '\n')
        if Type == 2:
            flag = True
            fp_3d.write(line)
        if Type == 3:
            fp_3d.write(line)
        if Type == 4:
            if flag == True:
                flag = False
                fp_3d.write(r"{\pos(286,255)\fscx50}" + line)
            else:
                fp_3d.write(line)
    fp_2d.close()
    fp_3d.close()

def left():
    if len(sys.argv) != 2:
        print sys.argv[0] + ' ' + '*.srt'
    fp_2d = open(sys.argv[1], "r")
    fp_3d = open(sys.argv[1] + "_3d.srt", "w")
    print sys.argv[1] + "_3d.srt"
    flag = False
    MaxIndex = 0
    for line in fp_2d:
        Type = textType(line)
        if Type == 1:
            flag = True
            match = re_index.findall(line)
            if match:
                MaxIndex = int(match[0])
            fp_3d.write(line)
        if Type == 2:
            flag = True
            fp_3d.write(line)
        if Type == 3:
            fp_3d.write(line)
        if Type == 4:
            if flag == True:
                flag = False
                fp_3d.write(r"{\pos(98,255)\fscx50}" + line)
            else:
                fp_3d.write(line)
    
    fp_2d.close()
    fp_3d.close()
    return MaxIndex
def main():
    MaxIndex = left()
    right(MaxIndex)
    print "ok!"
main()
