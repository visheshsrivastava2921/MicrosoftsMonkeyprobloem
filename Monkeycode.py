class calc:
  def fill_table(table,table1,comp,closed_rooms):
    z=0
        # filling the table withe the table numbers
        for i in range(1,11):
            for j in range(1,11):
                f=i*j
                table.append(f)
        #sorting the table 1
        n=len(table)
        for i in range(n):
            for j in range(0,n-i-1):
                if table[j]>table[j+1]:
                    table[j],table[j+1]=table[j+1],table[j]
        #removingt the repeating elements from the table and adding it to the now table 
        for i in table:
            if i not in table1:
                table1.append(i)
        # creating a new table to compare the existing table 
        for i in range(1,101):
            comp.append(i)
        #inserting 0 in the missing elements
        for i in range(len(comp)):
            if table1[i]!=i:
                table1.insert(i,0)
        #calculating the number of 0 to get the number of rooms which are closed 
        for i in range(1,99):
            if table1[i]==0:
                z=z+1
                closed_rooms.append(i)
        print(table,"\n",table1,"\n",comp,"\n",closed_rooms)
c=calc
table=[]
table1=[]
comp=[]
closed_rooms=[]
c.fill_table(table,table1,comp,closed_rooms)
