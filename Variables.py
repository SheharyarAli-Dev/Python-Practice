# variables

age=5; 
print(type(age));

age=5.5; 
print(type(age));

age="Ali"; 
print(type(age));

#Local and gloabl varaiables

a=6;

def greet():
    a=5;
    print(a);
greet();
print(a);

b=6;

def greet1():
    global b;
    b+=1;
    print(b);

greet1();
print(b);



