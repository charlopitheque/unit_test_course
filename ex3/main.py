from functools import reduce


class Exercice3:
    def __init__(self):
        pass

    def split_string_by_len(self, str, length):
        lines = []
        for i in range(0, len(str), length):
            if str[i] == " ":
                lines.append(str[i:i + length] + '\n')
            else:
                lines.append(str[i:i + length])
        print(''.join(lines))
        return ''.join(lines)

    def split_string_by_len2(self, str, length):
        list = str.split(" ")
        print(len(list))
        for idx, elem in enumerate(list):
            print(idx)
            if idx+1 <= len(list)-1:
                if len(elem) + len(list[idx + 1]) > length:
                    elem += '\n'

        print(list)


if __name__ == '__main__':
    ex3 = Exercice3()
    ex3.split_string_by_len2('My string is so long, i have to add carriage returns', 10)
