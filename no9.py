def duplilist():
      colors=["red","blue","green","red","yellow","blue"]
      dupli_list=[]
      for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                  if colors[i]==colors[j]:
                        dupli_list.append(colors[i])

      return dupli_list
print(f"List of duplicate is {duplilist()}")
                        
