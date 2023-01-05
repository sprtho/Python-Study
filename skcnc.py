
'''grade_list = [['AAAAA','A'],['BBBBB','B'],['CCCCC','C'],['AAAAA','B'],['DDDDD','A'],['AAAAA','D']]

print(grade_list)

grade_dict = {'A':100, 'B':90, 'C':80, 'D':70}

stack_list = []'''


'''for i in range(len(grade_list)):
    
    if len(stack_list) == 0:
        stack_list.append(grade_list[i])
    else:

        stack_len = len(stack_list)

        cnt = 0
        check = True
        while cnt < stack_len:

            if stack_list[cnt][0] == grade_list[i][0]:

                if grade_dict[stack_list[cnt][1]] >= grade_dict[grade_list[i][1]]:
                    check = False
                    break
                else:
                    check = False
                    stack_list.pop(cnt)
                    stack_list.append(grade_list[i])
                    break

            cnt += 1

    if check == True:
        stack_list.append(grade_list[i])'''

print("hi")            