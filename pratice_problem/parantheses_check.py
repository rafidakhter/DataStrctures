
import sys
sys.path.insert(0,r'C:\Users\rafid\Desktop\DataStructures')

from stacked_list import *

def check_paranthesis(string):
    "takes in a string and checks if the brackets are places properly or not"
    bracket_list=stackedlist()
    reverse={
            ")":"(",
            "]":"[",
            "}":"{"
            }
    for counter in range(0,len(string)):

        if string[counter]=="(" or string[counter]=="[" or string[counter]=="{":
        #if the string is an open bracket then push into the stacked list
            bracket_list.push(string[counter])

        elif string[counter]==")" or string[counter]=="]" or string[counter]=="}":
                    
        #if the string is a closing bracket checks :
                # if it the list empty then invalid
                # if the last element in the list != the reverse of the closing bracket then invalid

            rev=reverse[string[counter]]
            last_elm=bracket_list.peek()
            if bracket_list.length()==0:
                print('invalid')
                return
            elif rev!=last_elm:
                print('invalid')
                return
            else:
                bracket_list.pop()
        else:
            pass
    if bracket_list.length()==0:
        print('valid')
    else:
        print('invalid')
    return
