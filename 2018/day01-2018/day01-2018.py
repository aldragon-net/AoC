freq = 0
freqs = set()
freqs.add(freq)
repfreq_found = False
while True:
    with open('input_day01-2018.txt', 'r') as inpfile:
        while True:
            line = inpfile.readline().strip()
            if line == '':
                break
            freq = freq + int(line)
            if not repfreq_found:
                if freq not in freqs:
                    freqs.add(freq)
                else:
                    repfreq_found = True
                    print('First repeating frequency is:', freq)
                    input()
    print('Resulting frequency is:', freq)
    if repfreq_found:
        break
