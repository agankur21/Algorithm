def count(s):
    #Better method : Choose starting point and move forward with even jumps n^2
    count =0
    i=0
    num_iterations=0
    while i < len(s)-1:
        start_char = s[i]
        start_count=1
        end_count = 0
        for j in range(i+1,len(s)):
            num_iterations +=1
            if s[j] == start_char:
                if end_count == 0:
                    start_count += 1
                else:
                    break
            else:
                if end_count < start_count:
                    end_count += 1
                else:
                    break
        if end_count > 0:
            count += end_count
        if j < len(s)-1 :
            i = j - end_count
        else:
            break
    return count,num_iterations

def check_valid(s):
    start_char = s[0]
    array1 = s[0:len(s)/2]
    array2 = start_char*(len(s)/2)
    if  array1 == array2:
        if s[len(s)/2:] == str(1-int(start_char))*(len(s)/2):
            return True
    return False


def naive_implementation(s):
    iterations=0
    count=0
    for window_length in range(2,len(s),2):
        for i in range(0,len(s)-2):
            iterations +=1
            if i+window_length <= len(s):
                if check_valid(s[i:i+window_length]):
                    count +=1
    return count,iterations


if __name__ == '__main__':
    #Check with Naive implementation
    string="100010001010101100110000011100011101010100101010111110000111111111"
    naive_count,naive_iterations = naive_implementation(string)
    print "String length: ",len(string)
    print "Naive Iterations: ",naive_iterations
    optimized_count,better_iterations = count(string)
    print "Better Iterations: ", better_iterations
    assert naive_count == optimized_count
