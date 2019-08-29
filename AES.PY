S = [
            [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
            [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
            [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
            [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
            [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
            [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
            [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
            [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
            [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
            [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
            [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
            [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
            [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
            [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
            [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
            [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ]   
INVS = [
            [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb], 
            [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb], 
            [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e], 
            [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25], 
            [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92], 
            [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84], 
            [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06], 
            [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b], 
            [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73], 
            [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e], 
            [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
            [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4], 
            [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f], 
            [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef], 
            [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61], 
            [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
        ]
rcon=[[0x01,00,00,00],[0x02,00,00,00],[0x04,00,00,00],[0x08,00,00,00],[0x10,00,00,00],[0x20,00,00,00],[0x40,00,00,00],[0x80,00,00,00],[0x1b,00,00,00],[0x36,00,00,00]]
mixcolumn=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
invmixcolumn=[['e','b','d','9'],['9','e','b','d'],['d','9','e','b'],['b','d','9','e']]
def rowmul2(r1):
    r3=0
    res=[0,0,0,0]
    for i in range(4):
        r3=0
        for j in range(4):
            if invmixcolumn[i][j]=='e':
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
            elif invmixcolumn[i][j]=='d':
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
            elif invmixcolumn[i][j]=='b':
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
            elif invmixcolumn[i][j]=='9':
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                a=bin(r2)[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
            r3=r3^r2
            # if r3>283:
            #     while(r3>283):
            #         r3=r3^283
        res[i]=hex(r3)[2:]
    return res
def rowmul(r1):
    r3=0
    res=[0,0,0,0]
    for i in range(4):
        r3=0
        for j in range(4):
            if mixcolumn[i][j]==2:
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
            elif mixcolumn[i][j]==1:
                r2=int(r1[j],16)
            elif mixcolumn[i][j]==3:
                a=bin(int(r1[j],16))[2:]
                p=list(a)
                if len(p)<8:
                    h=8-len(p)
                    p.reverse()
                    for b in range(h):
                        p.append('0')
                    p.reverse()
                    a=''.join(p)
                r2=int(ls(a),2)
                r=list(a)
                if r[0]=='1':
                    r2=r2^int('00011011',2)
                r2=r2^int(r1[j],16)
            r3=r3^r2
            # if r3>283:
            #     while(r3>283):
            #         r3=r3^283
        res[i]=hex(r3)[2:]
    return res
def ls(str1):
    list1=list(str1)
    c=list1[0]
    for i in range(len(list1)-1):
        list1[i]=list1[i+1]
    list1[len(list1)-1]='0'
    list2="".join(list1)
    return list2
def ls4(list1):
    c=list1[0]
    for i in range(0,3):
        list1[i]=list1[i+1]
    list1[3]=c
    return list1
def rs4(list1):
    c=list1[3]
    list2=[0,0,0,0]
    for i in range(1,4):
        list2[i]=list1[i-1]
    list2[0]=c
    return list2
def sbox(b):
    l=list(b)
    e=bin(int(l[0],16))[2:]
    f=bin(int(l[1],16))[2:]
    if len(e)<4:
        d=list(e)
        d.reverse()
        l=4-len(e)
        for t in range(l):
            d.append('0')
        d.reverse()
        e=''.join(d)
    if len(f)<4:
        d=list(f)
        d.reverse()
        l=4-len(f)
        for t in range(l):
            d.append('0')
        d.reverse()
        f=''.join(d) 
    e=int(e,2)
    f=int(f,2)
    s=(S[e][f])
    return s
def revsbox(b):
    l=list(b)
    e=bin(int(l[0],16))[2:]
    f=bin(int(l[1],16))[2:]
    if len(e)<4:
        d=list(e)
        d.reverse()
        l=4-len(e)
        for t in range(l):
            d.append('0')
        d.reverse()
        e=''.join(d)
    if len(f)<4:
        d=list(f)
        d.reverse()
        l=4-len(f)
        for t in range(l):
            d.append('0')
        d.reverse()
        f=''.join(d) 
    e=int(e,2)
    f=int(f,2)
    s=(INVS[e][f])
    return s
key=list(input("ENTER PRIVATE KEY >> ").split())
keys=[[],[],[],[]]
for i in range(0,4):
    a=key[i]
    keys[0].append(a)
for i in range(4,8):
    a=key[i]
    keys[1].append(a)
for i in range(8,12):
    a=key[i]
    keys[2].append(a)    
for i in range(12,16):
    a=key[i]
    keys[3].append(a)
for i in range(10):
    c=[0,1,1,1]
    for j in range(0,4):
        c[j]=keys[(i+1)*4-1][j]
    b=[]
    a=ls4(c)
    for j in range(4):
        a[j]=sbox(a[j])
        a[j]=a[j]^rcon[i][j]
        a[j]=a[j]^int(keys[4*i][j],16)
        a[j]=bin(a[j])[2:]
        if len(a[j])<8:
            d=list(a[j])
            d.reverse()
            l=8-len(a[j])
            for t in range(l):
                d.append('0')
            d.reverse()
            a[j]=''.join(d)
        a[j]=int(a[j],2)
    b.append(a)
    w=a.copy()
    for j in range(4):
        w[j]=w[j]^int(keys[4*i+1][j],16)
        w[j]=bin(w[j])[2:]
        if len(w[j])<8:
            d=list(w[j])
            d.reverse()
            l=8-len(w[j])
            for t in range(l):
                d.append('0')
            d.reverse()
            w[j]=''.join(d)
        w[j]=int(w[j],2)
    b.append(w)
    v=w.copy()
    for j in range(4):
        v[j]=v[j]^int(keys[4*i+2][j],16)
        v[j]=bin(v[j])[2:]
        if len(v[j])<8:
            d=list(v[j])
            d.reverse()
            l=8-len(v[j])
            for t in range(l):
                d.append('0')
            d.reverse()
            v[j]=''.join(d)
        v[j]=int(v[j],2)
    b.append(v)
    z=v.copy()
    for j in range(4):
        z[j]=z[j]^int(keys[4*i+3][j],16)
        z[j]=bin(z[j])[2:]
        if len(z[j])<8:
            d=list(z[j])
            d.reverse()
            l=8-len(z[j])
            for t in range(l):
                d.append('0')
            d.reverse()
            z[j]=''.join(d)
        z[j]=int(z[j],2)
    b.append(z)
    p=[[],[],[],[]]
    for j in range(4):
        for k in range(0,4):
            p[j].append(str(hex(b[j][k]))[2:])
            if len(p[j][k])<2:
                d=list(p[j][k])
                d.reverse()
                d.append('0')
                d.reverse()
                p[j][k]=''.join(d)
    keys=keys+p
keylist=[]
a=[]
for i in range(0,4):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(4,8):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(8,12):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(12,16):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(16,20):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(20,24):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(24,28):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(28,32):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(32,36):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(36,40):
    a.append(keys[i])
keylist.append(a)
a=[]
for i in range(40,44):
    a.append(keys[i])
keylist.append(a)
print("KEY 0 >> ",end=" ")
for i in range(0,4):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 1 >> ",end=" ")
for i in range(4,8):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 2 >> ",end=" ")
for i in range(8,12):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 3 >> ",end=" ")
for i in range(12,16):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 4 >> ",end=" ")
for i in range(16,20):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 5 >> ",end=" ")
for i in range(20,24):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 6 >> ",end=" ")
for i in range(24,28):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 7 >> ",end=" ")
for i in range(28,32):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 8 >> ",end=" ")
for i in range(32,36):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 9 >> ",end=" ")
for i in range(36,40):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
print("KEY 10 >> ",end=" ")
for i in range(40,44):
    for j in range(0,4):
        print(keys[i][j],end=" ")
print()
keylist2=list(reversed(keylist))
choice=input("ENTER YOUR CHOICE 1.ENCRYPT 2.DECRYPT >>  ")
if choice=='1':
    text=list(input("ENTER PLAIN TEXT >> ").split())
    plain=[[],[],[],[]]
    for i in range(0,4):
        a=text[i]
        plain[0].append(a)
    for i in range(4,8):
        a=text[i]
        plain[1].append(a)
    for i in range(8,12):
        a=text[i]
        plain[2].append(a)    
    for i in range(12,16):
        a=text[i]
        plain[3].append(a)
    for i in plain:
        print(i)
    for i in range(4):
        for j in range(4):
            plain[i][j]=int(plain[i][j],16)^int(keylist[0][i][j],16)
            if plain[i][j]>283:
                    while(plain[i][j]>283):
                        plain[i][j]=plain[i][j]^283
            plain[i][j]=hex(plain[i][j])[2:]
            p=list(plain[i][j])
            if len(p)<2:
                    p.append('0')
                    p.reverse()
            plain[i][j]=''.join(p)
    for m in range(10):
        for i in range(4):
            for j in range(4):
                plain[i][j]=hex(sbox(plain[i][j]))[2:]
        p=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            for j in range(4):
                p[i][j]=plain[j][i]
        for i in range(4):
            for k in range(i):
                p[i]=ls4(p[i])
        for i in range(4):
            for j in range(4):
                plain[i][j]=p[j][i]
        for i in range(4):
            for j in range(4):
                p=list(plain[i][j])
                if len(p)<2:
                    p.append('0')
                    p.reverse()
                plain[i][j]=''.join(p)
        if(m!=9):
            for i in range(4):
                plain[i]=rowmul(plain[i])
        for i in range(4):
            for j in range(4):
                plain[i][j]=int(plain[i][j],16)^int(keylist[m+1][i][j],16)
                if plain[i][j]>283:
                    while(plain[i][j]>283):
                        plain[i][j]=plain[i][j]^283
                plain[i][j]=hex(plain[i][j])[2:]
                p=list(plain[i][j])
                if len(p)<2:
                    p.append('0')
                    p.reverse()
                plain[i][j]=''.join(p)
    result=[]
    for i in range(4):
        result.append(' '.join(plain[i]))
    print(' '.join(result))
if choice=='2':
    text=list(input("ENTER CIPHER TEXT >> ").split())
    plain=[[],[],[],[]]
    for i in range(0,4):
        a=text[i]
        plain[0].append(a)
    for i in range(4,8):
        a=text[i]
        plain[1].append(a)
    for i in range(8,12):
        a=text[i]
        plain[2].append(a)    
    for i in range(12,16):
        a=text[i]
        plain[3].append(a)
    for i in plain:
        print(i)
    for i in range(4):
        for j in range(4):
            plain[i][j]=int(plain[i][j],16)^int(keylist2[0][i][j],16)
            if plain[i][j]>283:
                    while(plain[i][j]>283):
                        plain[i][j]=plain[i][j]^283
            plain[i][j]=hex(plain[i][j])[2:]
            p=list(plain[i][j])
            if len(p)<2:
                    p.append('0')
                    p.reverse()
            plain[i][j]=''.join(p)
    for m in range(10):
        p=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            for j in range(4):
                p[i][j]=plain[j][i]
        for i in range(4):
            for k in range(i):
                p[i]=rs4(p[i])
        for i in range(4):
            for j in range(4):
                plain[i][j]=p[j][i]
        for i in range(4):
            for j in range(4):
                p=list(plain[i][j])
                if len(p)<2:
                    p.append('0')
                    p.reverse()
                plain[i][j]=''.join(p)
        for i in range(4):
            for j in range(4):
                plain[i][j]=hex(revsbox(plain[i][j]))[2:]
        for i in range(4):
            for j in range(4):
                plain[i][j]=int(plain[i][j],16)^int(keylist2[m+1][i][j],16)
                if plain[i][j]>283:
                    while(plain[i][j]>283):
                        plain[i][j]=plain[i][j]^283
                plain[i][j]=hex(plain[i][j])[2:]
                p=list(plain[i][j])
                if len(p)<2:
                    p.append('0')
                    p.reverse()
                plain[i][j]=''.join(p)
        if(m!=9):
            for i in range(4):
                plain[i]=rowmul2(plain[i])
    result=[]
    for i in range(4):
        result.append(' '.join(plain[i]))
    print(' '.join(result))
