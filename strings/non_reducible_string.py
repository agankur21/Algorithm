# Enter your code here. Read input from STDIN. Print output to STDOUT
given_string = raw_input()
index=0

while index < len(given_string)-1 :
    if given_string[index] == given_string[index+1]:
        given_string = given_string[0:index] + given_string[index+2:]
        if index > 0:
            index -=1
    else:
        index +=1
print given_string


