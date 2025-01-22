class Solution:
    def isValid(self, s: str) -> bool:
        workS = []
        
        for c in s:
            if workS == []:
                workS.append(c)
                continue
            #print (workS[-1], c)
            if c ==')' or c == ']' or c == '}':
                if (c == ')' and workS[-1] == '(') or (c == ']' and workS[-1] == '[') or (c == '}' and workS[-1] == '{'):
                    workS.pop(-1)
                else:
                    return False
            else:
                workS.append(c)
            
        if workS == []:
            return True
        else:
            return False
             
            