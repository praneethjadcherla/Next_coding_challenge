import re
class Solution:

    def get_recipient(self, message, position):
        # Your code goes here
        nospaces_string=re.split("\s",message)
        count=0
        if position>=len(nospaces_string):
           return ""
        else:   
           for n in nospaces_string:
               if "@" in n:
                  count=count+1
               if count==position:
                  username = re.split(r'[@]', n)
                  recipient=re.split(r'[`!@#$%^&*()+\=\[\]{};\':"\\|,.<>\/?~]',username[1])
                  return recipient[0]
                  break      

s1=Solution()
print(s1.get_recipient("Hey @Joe_Bloggs what time are we meeting @FredBloggs?",2))
                