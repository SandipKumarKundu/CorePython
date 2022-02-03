set1st={1,2,3,34,4}
set2nd={2,44,5,6,78}
print(set1st|set2nd)
print(set1st&set2nd)
print(set1st-set2nd)
evenSet=list(filter(lambda i:i%2==0,set1st))
print(evenSet)
