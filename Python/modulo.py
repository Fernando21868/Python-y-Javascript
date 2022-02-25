def get_sev_seg_str(number, min_width=0):

    number = str(number).zfill(min_width)

    rows=['','','']
    for i,numeral in enumerate(number):
        if numeral=='.':
            rows[0]+=' '
            rows[1]+=' '
            rows[2]+=' '
            continue
        elif numeral=='-':
            rows[0]+='    '
            rows[1]+=' __ '
            rows[2]+='    '
        elif numeral=='0':
            rows[0]+=' __ '
            rows[1]+='|  |'
            rows[2]+='|__|'
        elif numeral=='1':
            rows[0]+='    '
            rows[1]+='   |'
            rows[2]+='   |'
        elif numeral=='2':
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+='|__ '
        elif numeral=='3':
            rows[0]+=' __ '
            rows[1]+=' __|'
            rows[2]+=' __|'
        elif numeral=='4':
            rows[0]+='    '
            rows[1]+='|__|'
            rows[2]+='   |'
        elif numeral=='5':
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+=' __|'
        elif numeral=='6':
            rows[0]+=' __ '
            rows[1]+='|__ '
            rows[2]+='|__|'
        elif numeral=='7':
            rows[0]+=' __'
            rows[1]+='   |'
            rows[2]+='   |'
        elif numeral=='8':
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+='|__|'
        elif numeral=='9':
            rows[0]+=' __ '
            rows[1]+='|__|'
            rows[2]+=' __|'

        if i!=len(number)-1:
            rows[0]+=' '
            rows[1]+=' '
            rows[2]+=' '
    return '\n'.join(rows)

print(get_sev_seg_str(42))
if __name__=='__main__':
    print('This module is meant to be imported rather than run.')
    print('For module, this code:')
    print('     import sevseg')
    print('     myNumber = sevseg.get_sev_Seg_str(42, 3)')
    print('     print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits:')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')