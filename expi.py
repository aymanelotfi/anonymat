def tokenizer(s):
    return s.split(' ')
from dateutil.parser import parse
def is_social_number(s):
    if s.isnumeric() and len(s)==13:
        return True
    else:
        return False
def ressemble(u,v):
    if max(len(u),len(v))<=4:
        return (u==v)
    else:
        return levenshtein(u,v)<=1
def levenshtein(mot1,mot2):
	ligne_i = [ k for k in range(len(mot1)+1) ]
	for i in range(1, len(mot2) + 1):
		ligne_prec = ligne_i
		ligne_i = [i]*(len(mot1)+1)
		for k in range(1,len(ligne_i)):
			cout = int(mot1[k-1] != mot2[i-1])
			ligne_i[k] = min(ligne_i[k-1] + 1, ligne_prec[k] + 1, ligne_prec[k-1] + cout)
	return ligne_i[len(mot1)]
noms={}
prenoms={}
def add_prenoms():
    file=open("prenom.txt", "r")

    for line in file.readlines():
        if line.lower().strip() not in prenoms:
            prenoms[line.lower().strip()]=1
    #print('philibert' in prenoms)
def add_noms():
    file=open("nom.txt","r")
    for line in file.readlines():
        if line.lower().strip() not in noms:
            noms[line.lower().strip()]=1
def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
add_prenoms()
add_noms()
def is_name(word):

    word=word.strip()
    if not word[0:1].isupper():
        return False
    word=word.strip()
    if len(word) <= 4:
        return (word.lower() in noms)
    for nam in noms.keys():
        if ressemble(nam,word.lower()):
            return True
    return False
    # if len(word) <= 4:
    #     return (word.lower() in noms)
    # for dude in noms.keys():
    #     if ressemble(dude,word.lower()):
    #         print(dude)
    #         return True
    # return False
def is_prenom(word):
    word=word.strip()
    if not word[0:1].isupper():
        return False
    if len(word) <= 4:
        return (word.lower() in prenoms)
    for prenom in prenoms.keys():
        if ressemble(prenom,word.lower()):
            return True
    return False

def anonymize(s):
    liste=tokenizer(s)
    anonym=[]
    for word in liste:
        if is_date(word):
            anonym.append('D')
        elif is_social_number(word):
            anonym.append('SSN')
        elif is_prenom(word):
            anonym.append('P')
        elif is_name(word):
            anonym.append('N')
        else:
            anonym.append(word)
    return ' '.join(anonym)

# def anonym_string(s):
#     liste=tokenizer(s)
#     answer=[]
#     for word in liste:
#         check = False
#         for v in prenoms.keys():
#             if ressemble(u,v):
#                 check=True
#         if check:
#             answer.append('P')
#         else:
#             answer.append(word)
#print(is_nom("le"))
#print(is_date("**10/06/2021**."))
#print(ressemble("Philibert","philibert"))
print("Le patient s'appelle Alexandre Arrayech , il a été admis aux urgences à cause d'une blessure au genou")
print("Anonymisé : "+anonymize("Le patient s'appelle Alexandre Arrayech , il a été admis aux urgences à cause d'une blessure au genou"))
