## Python Pass vs Continue Statements;
print("Case: Pass")
for x in range(0, 10):
    if x%5 != 0:
        pass
    print("Pass @ %d"%(x))

print("Case: Continue")
for x in range(0, 10):
    if x%5!=0:
        continue
    print("Continue @ %d"%(x))