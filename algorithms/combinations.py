def get_all_combinations(list_values, list_index, temp_list, out):
    if list_index >= len(list_values) :
        out.append(list(temp_list))
        return
    else:
        for y in range(len(list_values[list_index])):
            temp_list.append(list_values[list_index][y])
            get_all_combinations(list_values, list_index + 1,temp_list, out)
            temp_list.pop()



if __name__ == '__main__':
    list_values=[[1,2,3],[21,22],[100]]
    temp_list=[]
    out=[]
    get_all_combinations(list_values,0,temp_list,out)
    print out