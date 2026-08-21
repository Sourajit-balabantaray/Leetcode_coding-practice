m=[[1,0,0],
   [0,2,0],
   [0,3,4]]
values=[]
colidx=[]
rowptr=[0]
count=0
for i in m:
  for j in range(len(i)):
    if i[j]!=0:
      values.append(i[j])
      colidx.append(j)
      count=count+1
  rowptr.append(count)
print("values:",values)
print("colidx:",colidx)
print("rowptr:",rowptr)
