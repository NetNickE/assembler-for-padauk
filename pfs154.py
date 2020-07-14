# Assembler for PFS154 microcontroller v1.0
# author: Miklos Endresz (NickE)
# contact: nickemailbox at yahoo dot com

import re

class Line:
    def __init__(self, s, ln):
        self.s = s
        self.ln = ln

# .orgxxxh
def isOrg(s):
    if re.fullmatch(r'^.org[0-7][0-9a-f][0-9a-f]h$', s):
        return True
    else:
        return False

def romparse(l):
    if re.fullmatch(r'^add a,#[0-9a-f][0-9a-f]h$',l.s):         # add a,I   (hex)
        return 0x2800 + int(l.s[7:9],16)

    if re.fullmatch(r'^add a,#[0-9]{1,3}$',l.s):                # add a,I   (dec)
        return 0x2800 + int(l.s[7:],10)

    if re.fullmatch(r'^add a,m[0-7][0-9a-f]h$',l.s):            # add a,M
        return 0xc00 + int(l.s[7:9],16)

    if re.fullmatch(r'^add m[0-7][0-9a-f]h,a$',l.s):            # add M,a
        return 0x800 + int(l.s[5:7],16)

    if l.s == 'addc a':                                         # addc a
        return 0x60

    if re.fullmatch(r'^addc m[0-7][0-9a-f]h$',l.s):             # addc M
        return 0x1000 + int(l.s[6:8],16)

    if re.fullmatch(r'^addc a,m[0-7][0-9a-f]h$',l.s):           # addc a,M
        return 0xd00 + int(l.s[8:10],16)

    if re.fullmatch(r'^addc m[0-7][0-9a-f]h,a$',l.s):           # addc M,a
        return 0x900 + int(l.s[6:8],16)

    if re.fullmatch(r'^and a,#[0-9a-f][0-9a-f]h$',l.s):         # and a,I   (hex)
        return 0x2c00 + int(l.s[7:9],16)

    if re.fullmatch(r'^and a,#[0-9]{1,3}$',l.s):                # and a,I   (dec)
        return 0x2c00 + int(l.s[7:],10)

    if re.fullmatch(r'^and a,m[0-7][0-9a-f]h$',l.s):            # and a,M
        return 0xe00 + int(l.s[7:9],16)
            
    if re.fullmatch(r'^and m[0-7][0-9a-f]h,a$',l.s):            # and M,a
        return 0xa00 + int(l.s[5:7],16)

    if re.fullmatch(r'^call \$[0-7][0-9a-f][0-9a-f]h$',l.s):    # call label
        return 0x3800 + int(l.s[6:9],16)

    if re.fullmatch(r'^ceqsn a,#[0-9a-f][0-9a-f]h$',l.s):       # ceqsn a,I   (hex)
        return 0x2a00 + int(l.s[9:11],16)

    if re.fullmatch(r'^ceqsn a,#[0-9]{1,3}$',l.s):              # ceqsn a,I   (dec)
        return 0x2a00 + int(l.s[9:],10)

    if re.fullmatch(r'^ceqsn a,M[0-7][0-9a-f]h$',l.s):          # ceqsn a,M
        return 0x1700 + int(l.s[9:11],16)

    if re.fullmatch(r'^clear m[0-7][0-9a-f]h$',l.s):            # clear M
        return 0x1300 + int(l.s[7:9],16)

    if re.fullmatch(r'^cneqsn a,#[0-9a-f][0-9a-f]h$',l.s):      # cneqsn a,I  (hex)
        return 0x2b00 + int(l.s[10:12],16)

    if re.fullmatch(r'^cneqsn a,#[0-9]{1,3}$',l.s):             # cneqsn a,I  (dec)
        return 0x2b00 + int(l.s[10:],10)

    if re.fullmatch(r'^cneqsn a,M[0-7][0-9a-f]h$',l.s):         # cneqsn a,M
        return 0x1780 + int(l.s[10:12],16)

    if re.fullmatch(r'^dec m[0-7][0-9a-f]h$',l.s):              # dec M
        return 0x1280 + int(l.s[5:7],16)

    if l.s == 'disgint':                                        # disgint
        return 0x79

    if l.s == 'dzsn a':                                         # dzsn a
        return 0x63
    
    if re.fullmatch(r'^dzsn m[0-7][0-9a-f]h$',l.s):             # dzsn M
        return 0x1180 + int(l.s[6:8],16)

    if l.s == 'engint':                                         # engint
        return 0x78
    
    if re.fullmatch(r'^goto \$[0-7][0-9a-f][0-9a-f]h$',l.s):    # goto label
        return 0x3000 + int(l.s[6:9],16)

    if re.fullmatch(r'^idxm a,m[0-7][0-9a-f]h$',l.s):           # idxm a,M
        return 0x380 + int(l.s[8:10],16) + 1

    if re.fullmatch(r'^idxm m[0-7][0-9a-f]h,a$',l.s):           # idxm M,a
        return 0x380 + int(l.s[6:8],16)

    if re.fullmatch(r'^inc m[0-7][0-9a-f]h$',l.s):              # inc M
        return 0x1200 + int(l.s[5:7],16)

    if l.s == 'izsn a':                                         # izsn a
        return 0x62
    
    if re.fullmatch(r'^izsn m[0-7][0-9a-f]h$',l.s):             # izsn M
        return 0x1100 + int(l.s[6:8],16)
    
    if re.fullmatch(r'^ldt16 m[0-7][0-9a-f]h$',l.s):            # ldt16 M
        return 0x300 + int(l.s[7:9],16) + 1

    if re.fullmatch(r'^mov a,#[0-9a-f][0-9a-f]h$',l.s):         # mov a,I   (hex)
        return 0x2f00 + int(l.s[7:9],16)

    if re.fullmatch(r'^mov a,#[0-9]{1,3}$',l.s):                # mov a,I   (dec)
        return 0x2f00 + int(l.s[7:],10)

    if re.fullmatch(r'^mov a,m[0-7][0-9a-f]h$',l.s):            # mov a,M
        return 0xf80 + int(l.s[7:9],16)

    if re.fullmatch(r'mov a,io[0-3][0-9a-f]h$',l.s):            # mov a,IO
        return 0x1c0 + int(l.s[8:10],16)

    if re.fullmatch(r'^mov m[0-7][0-9a-f]h,a$',l.s):            # mov M,a
        return 0xb80 + int(l.s[5:7],16)

    if re.fullmatch(r'^mov io[0-3][0-9a-f]h,a$',l.s):           # mov IO,a
        return 0x180 + int(l.s[6:8],16)

    if l.s == 'neg a':                                          # neg a
        return 0x69

    if re.fullmatch(r'^neg m[0-7][0-9a-f]h$',l.s):              # neg M
        return 0x1480 + int(l.s[5:7],16)

    if l.s == 'nop':                                            # nop
        return 0

    if l.s == 'not a':                                          # not a
        return 0x68

    if re.fullmatch(r'^not m[0-7][0-9a-f]h$',l.s):              # not M
        return 0x1400 + int(l.s[5:7],16)

    if re.fullmatch(r'^or a,#[0-9a-f][0-9a-f]h$',l.s):          # or a,I  (hex)
        return 0x2d00 + int(l.s[6:8],16)

    if re.fullmatch(r'^or a,#[0-9]{1,3}$',l.s):                 # or a,I  (dec)
        return 0x2d00 + int(l.s[6:],10)

    if re.fullmatch(r'^or a,m[0-7][0-9a-f]h$',l.s):             # or a,M
        return 0xe80 + int(l.s[6:8],16)

    if re.fullmatch(r'^or m[0-7][0-9a-f]h,a$',l.s):             # or M,a
        return 0xa80 + int(l.s[4:6],16)

    if l.s == 'pcadd a':                                        # pcadd a
        return 0x67

    if l.s == 'popaf':                                          # popaf
        return 0x73

    if l.s == 'pushaf':                                         # pushaf
        return 0x72

    if l.s == 'reset':                                          # reset
        return 0x75

    if l.s == 'ret':                                            # ret
        return 0x7a

    if re.fullmatch(r'^ret #[0-9a-f][0-9a-f]h$',l.s):           # ret I  (hex)
        return 0x200 + int(l.s[5:7],16)

    if re.fullmatch(r'^ret a,#[0-9]{1,3}$',l.s):                # ret I  (dec)
        return 0x200 + int(l.s[5:],10)

    if l.s == 'reti':                                           # reti
        return 0x7b

    if re.fullmatch(r'^set0 m[0-3][0-9a-f]h\.[0-7]$',l.s):      # set0 M.n
        return 0x2400 + (int(l.s[-1],16)<<6) + int(l.s[6:8],16)

    if re.fullmatch(r'^set0 io[0-3][0-9a-f]h\.[0-7]$',l.s):     # set0 IO.n
        return 0x1c00 + (int(l.s[-1],16)<<6) + int(l.s[7:9],16)

    if re.fullmatch(r'^set1 m[0-3][0-9a-f]h\.[0-7]$',l.s):      # set1 M.n
        return 0x2600 + (int(l.s[-1],16)<<6) + int(l.s[6:8],16)

    if re.fullmatch(r'^set1 io[0-3][0-9a-f]h\.[0-7]$',l.s):     # set1 IO.n
        return 0x1e00 + (int(l.s[-1],16)<<6) + int(l.s[7:9],16)

    if l.s == 'sl a':                                           # sl a
        return 0x6b

    if re.fullmatch(r'^sl m[0-7][0-9a-f]h$',l.s):               # sl M
        return 0x1580 + int(l.s[4:6],16)

    if l.s == 'slc a':                                          # slc a
        return 0x6d

    if re.fullmatch(r'^slc m[0-7][0-9a-f]h$',l.s):              # slc M
        return 0x1680 + int(l.s[5:7],16)

    if l.s == 'sr a':                                           # sr a
        return 0x6a
    
    if re.fullmatch(r'^sr m[0-7][0-9a-f]h$',l.s):               # sr M
        return 0x1500 + int(l.s[4:6],16)

    if l.s == 'src a':                                          # src a
        return 0x6c

    if re.fullmatch(r'^src m[0-7][0-9a-f]h$',l.s):              # src M
        return 0x1600 + int(l.s[5:7],16)

    if l.s == 'stopexe':                                        # stopexe
        return 0x77

    if l.s == 'stopsys':                                        # stopsys
        return 0x76

    if re.fullmatch(r'^stt16 m[0-7][0-9a-f]h$',l.s):            # stt16 M
        return 0x300 + int(l.s[7:9],16)

    if re.fullmatch(r'^sub a,#[0-9a-f][0-9a-f]h$',l.s):         # sub a,I   (hex)
        return 0x2900 + int(l.s[7:9],16)

    if re.fullmatch(r'^sub a,#[0-9]{1,3}$',l.s):                # sub a,I   (dec)
        return 0x2900 + int(l.s[7:],10)

    if re.fullmatch(r'^sub a,m[0-7][0-9a-f]h$',l.s):            # sub a,M
        return 0xc80 + int(l.s[7:9],16)

    if re.fullmatch(r'^sub m[0-7][0-9a-f]h,a$',l.s):            # sub M,a
        return 0x880 + int(l.s[5:7],16)
    
    if l.s == 'subc a':                                         # subc a
        return 0x61

    if re.fullmatch(r'^subc m[0-7][0-9a-f]h$',l.s):             # subc M
        return 0x1080 + int(l.s[6:8],16)

    if re.fullmatch(r'^subc a,m[0-7][0-9a-f]h$',l.s):           # subc a,M
        return 0xd80 + int(l.s[8:10],16)

    if re.fullmatch(r'^subc m[0-7][0-9a-f]h,a$',l.s):           # subc M,a
        return 0x980 + int(l.s[6:8],16)

    if l.s == 'swap a':                                         # swap a
        return 0x6e

    if re.fullmatch(r'^swapc io[0-3][0-9a-f]h\.[0-7]$',l.s):    # swapc IO.n
        return 0x400 + (int(l.s[-1],16)<<6) + int(l.s[8:10],16)

    if re.fullmatch(r'^t0sn m[0-3][0-9a-f]h\.[0-7]$',l.s):      # t0sn M.n
        return 0x2000 + (int(l.s[-1],16)<<6) + int(l.s[6:8],16)

    if re.fullmatch(r'^t0sn io[0-3][0-9a-f]h\.[0-7]$',l.s):     # t0sn IO.n
        return 0x1800 + (int(l.s[-1],16)<<6) + int(l.s[7:9],16)

    if re.fullmatch(r'^t1sn m[0-3][0-9a-f]h\.[0-7]$',l.s):      # t1sn M.n
        return 0x2200 + (int(l.s[-1],16)<<6) + int(l.s[6:8],16)

    if re.fullmatch(r'^t1sn io[0-3][0-9a-f]h\.[0-7]$',l.s):     # t1sn IO.n
        return 0x1a00 + (int(l.s[-1],16)<<6) + int(l.s[7:9],16)

    if l.s == 'wdreset':                                        # wdreset
        return 0x70

    if re.fullmatch(r'^xch m[0-7][0-9a-f]h$',l.s):              # xch M
        return 0x1380 + (int(l.s[5:7],16)<<1) + 1

    if re.fullmatch(r'^xor a,#[0-9a-f][0-9a-f]h$',l.s):         # xor a,I  (hex)
        return 0x2e00 + int(l.s[7:9],16)

    if re.fullmatch(r'^xor a,#[0-9]{1,3}$',l.s):                # xor a,I  (dec)
        return 0x2e00 + int(l.s[7:],10)

    if re.fullmatch(r'^xor a,m[0-7][0-9a-f]h$',l.s):            # xor a,M
        return 0xf00 + int(l.s[7:9],16)

    if re.fullmatch(r'^xor m[0-7][0-9a-f]h,a$',l.s):            # xor M,a
        return 0xb00 + int(l.s[5:7],16)

    if re.fullmatch(r'^xor io[0-3][0-9a-f]h,a$',l.s):           # xor IO,a
        return 0xc0 + int(l.s[6:8],16)    

    print(f'Error in line: {l.ln}, syntax error!')
    exit()
    
f = open('a.asm','r')

i = 1
ll = []
# put lines and line numbers to ll list
while(True):
    s = f.readline()
    if (s==''):
        break
    lo = Line(s,i)          # line object
    ll.append(lo)
    i = i + 1

f.close()

# remove \n from end of line
for l in ll:
    if l.s[-1] == '\n':
        l.s=l.s[:-1]

# replace tabs with spaces
for l in ll:
    l.s=l.s.replace('\t',' ')

# remove comments
for l in ll:
    pos = l.s.find(';')
    if pos != -1:
        l.s = l.s[:pos]
        
# remove spaces from beginning of line
for l in ll:
    while len(l.s)>0 and l.s[0]==' ':
        l.s = l.s[1:]

# remove spaces from end of line
for l in ll:
    while len(l.s)>0 and l.s[-1]==' ':
        l.s = l.s[:-1]

# remove multiple spaces
for l in ll:
    while l.s.find('  ') != -1:
        l.s = l.s.replace('  ',' ')

# delete empty lines
i = 0
while i < len(ll):
  if ll[i].s == '':
    del ll[i]
  else:
    i = i + 1

# convert to lowercase
for l in ll:
    l.s = l.s.lower()

# remove space before comma
for l in ll:
    l.s = l.s.replace(' ,',',')

# remove space after comma
for l in ll:
    l.s = l.s.replace(', ',',')

var = {
    'flag':'io00h',
    'sp':'io02h',
    'clkmd':'io03h',
    'inten':'io04h',
    'intrq':'io05h',
    't16m':'io06h',
    'misc':'io08h',
    'tm2b':'io09h',
    'eoscr':'io0ah',
    'ihrcr':'io0bh',       # Internal High Speed RC Register (not listed in datasheet)
    'integs':'io0ch',
    'padier':'io0dh',
    'pbdier':'io0eh',
    'pa':'io10h',
    'pac':'io11h',
    'paph':'io12h',
    'pb':'io14h',
    'pbc':'io15h',
    'pbph':'io16h',
    'tm2s':'io17h',
    'gpcc':'io18h',
    'gpcs':'io19h',
    'bgtr':'io1ah',       # Bandgap Tuning Register (not listed in datasheet)
    'misc_lvr':'io1bh',   # Low Voltage Register (not listed in datasheet)
    'tm2c':'io1ch',
    'tm2ct':'io1dh',
    'pwmg0c':'io20h',
    'pwmg0s':'io21h',
    'pwmg0dth':'io22h',
    'pwmg0dtl':'io23h',
    'pwmg0cubh':'io24h',
    'pwmg0cubl':'io25h',
    'pwmg1c':'io26h',
    'pwmg1s':'io27h',
    'pwmg1dth':'io28h',
    'pwmg1dtl':'io29h',
    'pwmg1cubh':'io2ah',
    'pwmg1cubl':'io2bh',
    'pwmg2c':'io2ch',
    'pwmg2s':'io2dh',
    'pwmg2dth':'io2eh',
    'pwmg2dtl':'io2fh',
    'pwmg2cubh':'io30h',
    'pwmg2cubl':'io31h',
    'tm3c':'io32h',
    'tm3ct':'io33h',
    'tm3s':'io34h',
    'tm3b':'io35h',
    'Z':'io00h.0',        # flag bits
    'C':'io00h.1',
    'AC':'io00h.2',
    'OV':'io00h.3'
    }

i = 0
for l in ll:
    if l.s == '.var':
        i = i + 1

if i > 1:
    print('Only one .var segment allowed!')
    exit()

if i == 1:
    if ll[0].s != '.var':
        print('.var segment must be the first!')
        exit()

i = 0
for l in ll:
    if l.s == '.rom':
        i = i + 1

if i > 1:
    print('Only one .rom segment allowed!')
    exit()

if i == 0:
    print('.rom segment missig!')
    exit()

# process .var segment, put values into var dictionary
startparse = False
for l in ll:
    if l.s == '.rom':
        break
    if startparse:
        pos = l.s.find(' ')
        if pos == -1:
            print(f'Error in line: {l.ln}, incorrect variable declaration!')
            exit()
        varname = l.s[:pos]
        varaddr = l.s[pos+1:]
        if varname in var:
            print(f'Error in line: {l.ln}, variable already declared!')
            exit()
        var.update({varname:varaddr})
    if l.s == '.var':
        startparse = True

# put variable defined in .var to .rom segment
startparse = False
for l in ll:
    if startparse:
        if l.s[-1] == ':' or isOrg(l.s):        # here I don't care with labels and .orgxxxh
            continue
        
        pos = l.s.find(' ')
        if pos == -1:
            continue
        opcode = l.s[:pos]
        operand = l.s[pos+1:]
        if operand.find(',') == -1:             # there is only one operand
            if operand.find('.') == -1:         # dot not included
                if operand in var:
                    l.s = opcode + ' ' + var[operand]
            else:
                pos = operand.find('.')
                if operand[:pos] in var:
                    l.s = opcode + ' ' + var[operand[:pos]] + '.' + operand[pos+1:]     # set0 pa.7 > set0 io03h.7 conversion
        else:                                   # 2 operands case
            pos = operand.find(',')
            op1 = operand[:pos]
            op2 = operand[pos+1:]
            if op1 in var:
                op1 = var[op1]
            if op2 in var:
                op2 = var[op2]
            l.s = opcode + ' ' + op1 + ',' + op2
            
    if l.s == '.rom':
        startparse = True

# fill label dictionary with addresses
startparse = False
addr = 0
label = {}
for l in ll:
    if startparse:
        if isOrg(l.s):
            if int(l.s[4:7],16) >= addr:
                addr = int(l.s[4:7],16)
                continue
            else:
                print(f'Error in line: {l.ln}, variable already declared!')
                exit()
        if l.s[-1] == ':':
            if l.s[:-1] in label:
                print(f'Error in line: {l.ln}, label already exists!')
                exit()
            label.update({l.s[:-1]:addr})
            continue
        addr = addr + 1         # instruction counter
    if l.s == '.rom':
        startparse = True

# replace labels with address after call and goto
startparse = False
for l in ll:
    if startparse:
        if re.match(r'^call [^$]', l.s):        # call label
            pos = l.s.find(' ')
            operand = l.s[pos+1:]
            if operand in label:
                l.s = 'call $' + f'{label[operand]:03x}h'
            else:
                print(f'Error in line: {l.ln}, label not found!')
                exit()
                
        if re.match(r'^goto [^$]', l.s):        # goto label
            pos = l.s.find(' ')
            operand = l.s[pos+1:]
            if operand in label:
                l.s = 'goto $' + f'{label[operand]:03x}h'
            else:
                print(f'Error in line: {l.ln}, label not found!')
                exit()
    if l.s == '.rom':
        startparse = True

# fill rom with values
startparse = False
rom = []
for l in ll:
    if startparse:
        if isOrg(l.s):
            while int(l.s[4:7],16) > len(rom):
                rom.append(0)
            continue
        if l.s[-1] == ':':
            continue
        rom.append(romparse(l))
    if l.s == '.rom':
        startparse = True

# write parsed.temp to file
f = open('parsed.temp','w',encoding='utf8')
for l in ll:    
    f.write(l.s+'\n')
f.close()

# create a.hex file
f = open('a.hex','w')
addr = 0
while len(rom) >= 16:                           # 16 word = 32 byte
    f.write(':20' + f'{addr:04X}' + '00')
    checksum = 0x20 + (addr>>8) + (addr&0xff)
    for i in range(16):
        w = rom[i]
        wl = w & 0xff
        f.write(f'{wl:02X}')
        checksum = checksum + wl
        wh = w >> 8
        f.write(f'{wh:02X}')
        checksum = checksum + wh
    checksum = checksum & 0xff
    checksum = 0x100 - checksum
    checksum = checksum & 0xff
    f.write(f'{checksum:02X}\n')
    rom = rom[16:]
    addr = addr + 32
if len(rom)>0:
    f.write(':' + f'{len(rom)*2:02X}' + f'{addr:04X}' + '00')
    checksum = 2 * len(rom) + (addr>>8) + (addr&0xff)
    for i in range(len(rom)):
        w = rom[i]
        wl = w & 0xff
        f.write(f'{wl:02X}')
        checksum = checksum + wl
        wh = w >> 8
        f.write(f'{wh:02X}')
        checksum = checksum + wh
    checksum = checksum & 0xff
    checksum = 0x100 - checksum
    checksum = checksum & 0xff
    f.write(f'{checksum:02X}\n')
f.write(':00000001FF')
f.close()

print('a.hex created')
#for l in ll:
#    print(l.s)
