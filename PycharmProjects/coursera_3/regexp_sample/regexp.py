def calculate(data, findall):
    matches = findall(r'[abc][+-]?=[abc]?[-+\d]*')
    for one in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]

        s = []
        s.append(one[0])
        if (one[1] != '='):
            s.append(one[1])
            if (one[3] == 'a' or one[3] == 'b' or one[3] == 'c'):
                s.append(one[3])
                c = one[4:]
                s.append(c)
            else:
                s.append('')
                c = one[3:]
                s.append(c)
        else:
            s.append('')
            if (one[2] == 'a' or one[2] == 'b' or one[2] == 'c'):
                s.append(one[2])
                c = one[3:]
                s.append(c)
            else:
                s.append('')
                c = one[2:]
                s.append(c)
        if (s[3][:1] == "+"):
            s[3] = int(s[3][1:])
        else:
            if (s[3][:1] == "-"):
                s[3] = -int(s[3][1:])
            else:
                if (s[3][:1] == ""):
                    s[3] = int(0)

        if (s[1] == "+"):
            a = data.get(s[0], 0) + (data.get(s[2], 0) + int(s[3]))

        if (s[1] == "-"):
            a = data.get(s[0], 0) - (data.get(s[2], 0) + int(s[3]))

        if (s[1] == ""):
            a = data.get(s[2], 0) + int(s[3])

        data[s[0]] = a

    return data
