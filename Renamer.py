
import argparse
import random

parser = argparse.ArgumentParser() #simplifys the wording of using argparse as stated in the python tutorial
parser.add_argument("-i", type=str, action='store',  dest='input', help="input the read file") # allows input of the forward read
parser.add_argument("-o", type=str, action='store',  dest='output', help="output the read file") # allows input of the forward read
args = parser.parse_args()

INPUT = str(args.input)
OUTPUT = str(args.output)

outputting = open(OUTPUT,'w')

number = 0

let_and_num = ['0','1','2','3','4','5','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for line in open(INPUT,'r'):
  if line.startswith('>'):
    uid = []
    for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
      uid.append(random.choice(let_and_num))
    number +=1
    new_name = '>SEQUENCE' + str(number) + ':FILE=' + INPUT.replace('/','...') + ':UID=' + ''.join(uid) + '\n'
    outputting.write(new_name)
  else:
    outputting.write(line)
    
    
    
outputting.close()

