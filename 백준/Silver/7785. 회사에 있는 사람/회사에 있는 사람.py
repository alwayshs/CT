line = input().strip()
n = int(line)
    
in_office = set()

for _ in range(n):
    record = input().split()
    if not record:
        continue
            
    name, status = record
        
    if status == "enter":
        in_office.add(name)
    else:
        in_office.discard(name)
            
result = sorted(in_office, reverse=True)
    
print('\n'.join(result) + '\n')