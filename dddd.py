
grade_list = [['AAAAA','B'],['BBBBB','B'],['CCCCC','C'],['AAAAA','B'],['DDDDD','A'],['AAAAA','A'],
             ['BBBBB','A'], ['DDDDD','C'], ['CCCCC','A']]

grade_dict = {'A':100, 'B':90, 'C':80, 'D':70}

stack_list = []

check = False

for i in range(len(grade_list)):
    
    if len(stack_list) == 0:
        stack_list.append(grade_list[i])
    else:
        stack_len = len(stack_list)

        cnt = 0
        check = True
        while cnt < stack_len:

            print("{},{}".format(stack_list[cnt][0],grade_list[i][0] ))

            if stack_list[cnt][0] == grade_list[i][0]:

                if grade_dict[stack_list[cnt][1]] >= grade_dict[grade_list[i][1]]:
                    print("{},{}".format(grade_dict[stack_list[cnt][1]],grade_dict[grade_list[i][1]] ))
                    check = False
                    break
                else:
                    print("{},{}".format(grade_dict[stack_list[cnt][1]],grade_dict[grade_list[i][1]] ))
                    check = False
                    stack_list.pop(cnt)
                    stack_list.append(grade_list[i])
                    break

            cnt += 1

    if check == True:
        stack_list.append(grade_list[i])

for i in stack_list:
    print(i)
