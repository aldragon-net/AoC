with open('input_day16.txt', 'r') as f:
    inp = f.readline().strip()
    f.close()

bins = []
for char in inp:
    value = int(char, 16)
    quadra = format(value, '0>4b')
    bins.append(quadra)

inp = ''.join(bins)

def packet_scan(start):
    version = int(inp[start:start+3], 2)
    type_id = int(inp[start+3:start+6], 2)
    if type_id == 4:    # scan_literal
        pos = 6
        num_str = ''
        while int(inp[start+pos]) == 1:
            num_str = num_str + inp[(start+pos+1):(start+pos+5)]
            pos += 5
        num_str = num_str + inp[(start+pos+1):(start+pos+5)]
        pos += 5
        number = int(num_str, 2)
        length = pos
        result = (version, type_id, length, number)
        return [result]
    else:   # scan other packets
        subpackets = []
        length_type_id = int(inp[start+6:start+7])
        if length_type_id == 0:
            tot_length = int(inp[start+7:start+22], 2)
            pos = 22
            sum_length = 0
            while sum_length < tot_length:
                subpacket = packet_scan(start+pos)
                subpackets.append(subpacket)
                sublength = subpacket[0][2]
                sum_length += sublength
                pos += sublength
        elif length_type_id == 1:
            num_subpackets = int(inp[start+7:start+18], 2)
            n = 0
            pos = 18
            while n < num_subpackets:
                n += 1
                subpacket = packet_scan(start+pos)
                subpackets.append(subpacket)
                sublength = subpacket[0][2]
                pos += sublength
        length = pos
        result = [(version, type_id, length)]
        result.append(subpackets)
        return result

packet = packet_scan(0)

sum_version = []

def eval_packet(packet):
    sum_version.append(packet[0][0])
    if packet[0][1] == 4:
        return packet[0][3] # value
    else:
        subeval = [eval_packet(subpack) for subpack in packet[1]]
        if packet[0][1] == 0:
            return sum(subeval)
        if packet[0][1] == 1:
            product = 1
            for value in subeval:
                product *= value
            return product
        if packet[0][1] == 2:
            return min(subeval)
        if packet[0][1] == 3:
            return max(subeval)
        if packet[0][1] == 5:
             return int(subeval[0] > subeval[1])
        if packet[0][1] == 6:
            return int(subeval[0] < subeval[1])
        if packet[0][1] == 7:
            return int(subeval[0] == subeval[1])

print('evaluation is', eval_packet(packet))
print('sum of versions is:', sum(sum_version))
