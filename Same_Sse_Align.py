import argparse,re,os
parser = argparse.ArgumentParser(description = 'it can select the same sequence')
parser.add_argument('-i', '--name',help = 'Please input  in_put directory path default cwd')
args = parser.parse_args()
def jixing(dct):
        b=list(dct.values())
        c=[re.sub("[GSTYCQN]","1",k) for k in b]
        new_dct=dict(zip(list(dct.keys()),c))
        return new_dct
def suanxing(dct):
        b=list(dct.values())
        c=[re.sub("[DE]","2",k) for k in b]
        new_dct=dict(zip(list(dct.keys()),c))
        return new_dct
def jianxing(dct):
        b=list(dct.values())
        c=[re.sub("[RKH]","3",k) for k in b]
        new_dct=dict(zip(list(dct.keys()),c))
        return new_dct
def shushuixing(dct):
        b=list(dct.values())
        c=[re.sub("[AVLIPWFM]","4",k) for k in b]
        new_dct=dict(zip(list(dct.keys()),c))
        return new_dct
def quchong(seq_dct):
	func = lambda z: dict([(x, y) for y, x in z.items()])
	return func(func(seq_dct))
def huoqu(dct1,dct2):
    for key1,val1 in dct1.items():#xinzidian
        key_lst=[]
        for key2,val2 in dct2.items():
            if val2==val1:
                key_lst.append(key2)
        print("和%s相等的序列ID是:"%key1,key_lst)
sequence = ' '
fasta = {}
val_lst=[]
args.name=os.path.abspath(args.name)
with open(args.name,'r') as file_one:
    file_one_content = file_one.read()
    for line in file_one_content.split("\n"):
        if not line.strip():
            continue
        if line.startswith(">"):
            sequence_name = line.strip('\n').replace(">", "").split('|')[1]
        else:
            sequence = line.strip('\n')
        if sequence_name not in fasta:
            fasta[sequence_name] = []
        fasta[sequence_name].append(sequence)
for val in fasta.values():
    val_lst.append("".join(val[1:]))
new_fasta=dict(zip(list(fasta.keys()),val_lst))
new_dct=quchong(shushuixing(jianxing(suanxing(jixing(new_fasta)))))
old_dct=shushuixing(jianxing(suanxing(jixing(new_fasta))))
huoqu(new_dct,old_dct)

