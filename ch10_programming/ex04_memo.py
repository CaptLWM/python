# -*- coding: utf-8 -*-
import sys
if len(sys.argv) not in [2, 3]:
    print("사용법: python 파일명.py -a/v/h [message]")
    sys.exit()
option = sys.argv[1]
if option == '-a':
    memo = sys.argv[2]
    f = open("memo.txt", 'a')
    f.write(memo)
    f.write('\n')
    f.close()
if option == '-v':
    f = open("memo.txt", 'r')
    memo = f.read()
    print(memo)
    f.close()
if option == '-h':
    print("사용법: python 파일명.py -a/v/h [message]")
