letter_num = [chr(i) for i in range(97, 124)]

def is_dec_sys(out_base, in_base, num):
    if in_base == 10:
        return aux_trans(out_base, num)

    else:
        return trans(out_base, in_base, num)


# letters translation
def get_digits(num):
    ds = []
    for i in range(len(num)):
        if num[i] in(str(j) for j in range(10)):
            ds.append(int(num[i]))
            continue

        for j in range(len(letter_num)):
            if num[i] == letter_num[j]:
                ds.append(j + 10)

    return ds


def get_str_num(ds_d):
    # finally num
    finally_num = ""

    for i in range(len(ds_d)):
        if 0 <= ds_d[i] < 10:
            finally_num += str(ds_d[i])
            continue

        for j in range(len(letter_num)):
            if j + 10 == ds_d[i]:
                finally_num += letter_num[j]

    return finally_num


# in 10-NS
def aux_trans(out_base, num):
    translated_num = 0
    base = out_base
    ds_up = get_digits(num)
    for i in range(len(ds_up)):
        translated_num += ds_up[i] * (base ** (len(ds_up) -i - 1))

    return translated_num


# in need NS
def trans(out_base, in_base, num):
    # in dec
    num_n = aux_trans(out_base, num)

    # array
    ds_d = []

    while num_n > 0:
        ds_d.append(num_n % in_base)
        num_n //= in_base

    finally_num = get_str_num(ds_d[::-1])

    return finally_num


out = int(input())
in_b = int(input())
n = input()

print(is_dec_sys(out, in_b, n))
