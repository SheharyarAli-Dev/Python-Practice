a=[1,2,"Apple"];

a.append(3);

print(a);

a.extend([3,4]);

print(a);

a.append([3,4]);


print(a);
a.reverse();
print(a);

print(a.pop());


a=[0]*5

b=[[[0]*4 for i in range(4)] for i in range(4)];

print(b)


person = {
    "name"  : "Alice",
    "age"   : 25,
    "city"  : "New York"
}

person["name"]=5;
print(person);