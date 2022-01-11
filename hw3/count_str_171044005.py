
def count_string(str, start, end):
    l = len(str)
    count=0
    for i in range(0,l):
        if(str[i]==start):
            for j in range(i,l):
                if(str[j]==end):
                    count=count+1
    return count       
    
string="TXZXXJZWX"
char_first="X"
char_second="Z"

print(count_string(string,char_first,char_second))