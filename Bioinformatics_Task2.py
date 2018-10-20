def get_codon_table():
    d = {}
    d['CAU'] = 'H'; d['CAC'] = 'H'; d['CAA'] = 'Q'; d['CAG'] = 'Q'; d['CCU'] = 'P'; d['CCC'] = 'P'; d['CCA'] = 'P'; d['CCG'] = 'P';
    d['CGU'] = 'R'; d['CGC'] = 'R'; d['CGA'] = 'R'; d['CGG'] = 'R'; d['CUU'] = 'L'; d['CUC'] = 'L'; d['CUA'] = 'L'; d['CUG'] = 'L';
    d['GAU'] = 'D'; d['GAC'] = 'D'; d['GAA'] = 'E'; d['GAG'] = 'E'; d['GCU'] = 'A'; d['GCC'] = 'A'; d['GCA'] = 'A'; d['GCG'] = 'A';
    d['GGU'] = 'G'; d['GGC'] = 'G'; d['GGA'] = 'G'; d['GGG'] = 'G'; d['GUU'] = 'V'; d['GUC'] = 'V'; d['GUA'] = 'V'; d['GUG'] = 'V';
    d['UAU'] = 'Y'; d['UAC'] = 'Y'; d['UAA'] = ''; d['UAG'] = ''; d['UCU'] = 'S'; d['UCC'] = 'S'; d['UCA'] = 'S'; d['UCG'] = 'S';
    d['UGU'] = 'C'; d['UGC'] = 'C'; d['UGA'] = ''; d['UGG'] = 'W'; d['UUU'] = 'F'; d['UUC'] = 'F'; d['UUA'] = 'L'; d['UUG'] = 'L';
    d['AAU'] = 'N'; d['AAC'] = 'N'; d['AAA'] = 'K'; d['AAG'] = 'K'; d['ACU'] = 'T'; d['ACC'] = 'T'; d['ACA'] = 'T'; d['ACG'] = 'T';
    d['AGU'] = 'S'; d['AGC'] = 'S'; d['AGA'] = 'R'; d['AGG'] = 'R'; d['AUU'] = 'I'; d['AUC'] = 'I'; d['AUA'] = 'I'; d['AUG'] = 'M';   
    return d

def get_reverse_compliment(pattern):
    tmpstr = ''
    res = ''
    for i in range (len(pattern)):
        if (pattern[i] == 'A'):
            tmpstr += 'T'
            continue
        if (pattern[i] == 'C'):
            tmpstr += 'G'
            continue
        if (pattern[i] == 'G'):
            tmpstr += 'C'
            continue
        if (pattern[i] == 'T'):
            tmpstr += 'A'
            continue
    res = tmpstr[:: -1]
    return res

def Task1():
    pattern = input()
    d = {}
    d = get_codon_table()
    peptide = ''
    for i in range(0, len(pattern), 3):
        ThreeMer = pattern[i:i+3]
        peptide += d.get(ThreeMer)
    print(peptide)



def Task2():
    dna  = input()
    peptide = input()
    d = {}
    d = get_codon_table()
    pept = ''
    for i in range(len(dna) - 3 * len(peptide) + 1):
        tmp = dna[i:i + 3 * len(peptide)]
        rev_comp = get_reverse_compliment(tmp)
        rna1 = tmp
        rna2 = rev_comp
        for j in range(len(tmp)):
            if tmp[j] == 'T':
                rna1 = rna1[:j] + 'U' + rna1[j+1:]
        for l in range(len(rev_comp)):
            if rev_comp[l] == 'T':
                rna2 = rna2[:l] + 'U' + rna2[l+1:]

        for k in range(0, len(rna1), 3):
            buf = rna1[k:k + 3]
            pept += d.get(buf)
        if pept == peptide:
            print(tmp)
            pept = ''
            continue
        pept = ''
        for k in range(0, len(rna2), 3):
            buf = rna2[k:k + 3]
            pept += d.get(buf)
        if pept == peptide:
            print(tmp)

        pept = ''


def Task3():
    len_cicl_pept = input()
    len_cicl_pept = int(len_cicl_pept)
    subpeptides = len_cicl_pept * (len_cicl_pept - 1)
    print(subpeptides)


def Task4():
    l = []
    sum = 0
    total_sum = 0
    string = ''
    dict = {}
    dict['A'] = 71; dict['I'] = 113; dict['N'] = 114; dict['D'] = 115; dict['C'] = 103; dict['Q'] = 128
    dict['E'] = 129; dict['G'] = 57; dict['H'] = 137; dict['L'] = 113; dict['K'] = 128; dict['M'] = 131
    dict['F'] = 147; dict['P'] = 97; dict['S'] = 87; dict['T'] = 101; dict['W'] = 186; dict['Y'] = 163
    dict['V'] = 99; dict['R'] = 156
    
    peptide = input()
    l.append(0)
    for i in range(len(peptide)):
        total_sum += dict.get(peptide[i:i+1])
        l.append(dict.get(peptide[i:i+1]))
    l.append(total_sum)
    for i in range(len(peptide)):
        for j in range(1, len(peptide) - 1):
            sum = 0
            if (i+j > (len(peptide) - 1)):
                tmp = peptide[i:len(peptide)] + peptide[:j - (len(peptide) - i) + 1]
            else:
                tmp = peptide[i:i+j+1]
            for k in range(len(tmp)):
                sum += dict.get(tmp[k:k+1])
            l.append(sum)
    
    l.sort()
    for i in range(len(l)):
        string += str(l[i]) + ' '
    print(string)




#Task3()
#Task2()
Task4()