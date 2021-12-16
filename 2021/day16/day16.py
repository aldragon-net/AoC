with open('input_day16.txt', 'r') as f:
    inp = f.readline().strip()
    f.close()

test1 = 'D2FE28'
test2 = '38006F45291200'
test3 = 'EE00D40C823060'
test4 = '8A004A801A8002F478'
test5 = '620080001611562C8802118E34'
test6 = 'C0015000016115A2E0802F182340'
test7 = 'A0016C880162017C3686B18A3D4780'

inp = test2

inp = int(inp, 16)
inp = format(inp, 'b')

print(inp)

start = 0

def packet_scan(start):
    version = int(inp[start:start+3], 2)
    type_id = int(inp[start+3:start+6], 2)
    if type_id == 4:    # scan_literal
        print('literal at', start)
        pos = 6
        num_str = ''
        while int(inp[start+pos]) == 1:
            num_str = num_str + inp[(start+pos+1):(start+pos+5)]
            pos += 5
        num_str = num_str + inp[(start+pos+1):(start+pos+5)]
        pos += 5
        number = int(num_str, 2)
        length = ((pos // 4) + 1) * 4
        return [(version, type_id, length, number)]
    else:   # scan other packets
        subpackets = []
        length_type_id = int(inp[start+6:start+7])
        print('length_type_id', length_type_id) 
        if length_type_id == 0:
            tot_length = int(inp[start+7:start+22], 2) # !!!!!
            print(start, inp[start+7:start+22], 'tot_length', tot_length)
            pos = start + 22
            sum_length = 0
            while sum_length < tot_length:
                print('call packet_scan at', start+pos)
                subpacket = packet_scan(pos)
                subpackets.append(subpacket)
                sublength = subpacket[0][2]
                sum_length += sublength
                pos += sublength
        elif length_type_id == 1:
            num_subpackets == int(inp[start+7:start+18])
            n = 0
            pos = start + 18
            while n < num_subpackets:
                print('call packet_scan at', start+pos)
                subpacket = packet_scan(pos)
                subpackets.append(subpacket)
                sublength = subpacket[0][2]
                n += 1
                pos += sublength
        length = 1
        return [(version, type_id, length)].extend(subpackets)

print(packet_scan(0))

