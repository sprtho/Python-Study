wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
    }


print(wintable['바위'])
print(wintable)


words = ['a','b','c']

print(words)

#print(words[2])

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp('가위','가위')

#print(result)

messages = {
    'win':'이겼다',
    'draw':'비겼다',
    'lose':'졌다'
}

print(messages[result])