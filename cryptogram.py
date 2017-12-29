ALPHABET = 'abcdefghijklmopqrstuvwxyz'

def Rotate(key: int) -> str:
    """ Shifting the alphabet by the key we want to cipher """
    rotate = ""
    for letter in ALPHABET:
        rotate += ALPHABET[(ALPHABET.index(letter) + key) % (len(ALPHABET))]
    return rotate 

def Caesar_decrypt(x:str, key:int)->str:
    #global ALPHABET
    table= str.maketrans(Rotate(key), ALPHABET)
    return x.lower().translate(table)

#read the files    
infile = open('wordlist.txt', 'r')
wordlist = infile.read()
infile.close()

def Caesar_breake(s:str)->str:
    d ={}
    for key in range(1,27):
        #print(key)
        result=[]
        count = 0
        text = Caesar_decrypt(s, key)
        for i in text.split():
            if i in wordlist:
                count +=1
        d[count] = text
    return d[max(d)]

Caesar_breake("zopnr lux g copsk ghuaz ouc zu cxpzk zopy; pl eua'xk yzpss yzair, eua tge cpyo zu iunyasz zokyk opnzy (unk gz g zptk): (p) pz'y iunbknpknz zu ogbk g msuhgs iunyzgnz igsskj gsvoghkz zogz iunzgpny gss 26 suckx-igyk skzzkxy pn uxjkx. (pp) zu ju zok cuxr, eua'ss cgnz zu ayk zok zxgnysgzk() tkzouj; suur pz av zu tgrk yaxk eua anjkxyzgnj ouc zu ayk pz.")

