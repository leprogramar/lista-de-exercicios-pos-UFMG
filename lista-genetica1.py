#lista de exerciocios 2 da materia de ambientes de computacao  do programa de pos graduacao em bioinformatica 

# 1. O TNF alfa é uma citocina pró inflamatória capaz de provocar a apoptose (morte) de células tumorais. Dada a sua sequência de aminoácidos:
# VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL
# realize as seguintes tarefas:


# a) Retorne o tamanho da sequência.

seq = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"
print(seq)

print(len(seq))

# b) Realize a contagem da ocorrência de um sequência de leucinas (LL).

print(seq.count("LL"))

# c) Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR).

print(seq.find("GG"))
print(seq.find("RR"))

# d) Retorne os 100 primeiros aminoácidos da sequência.

print(seq[0:101])

# e) Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina (SSSR) por alaninas.

print(seq.replace("SSSR","ALA"))


# f) Quebre a sequência no local onde a substituição foi realizada.

print(seq.split("ALA")) 

# 2. Utilizando o texto abaixo:
# "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos.Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."
# Realiza as seguintes tarefas:


# a) Passe todo o texto para letras maiúsculas.

texto = "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos.Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."

print(texto.upper())

# b) Passe todo o texto para letras minúsculas.

print(texto.lower())

# c) Passe cada primeira letra de palavra em maiúsculo.

print(texto.title())

# d) Transforme as letras maiúsculas em minúsculas e vice-versa. 

print(texto.swapcase())

# 3. Utilizando a sequência:
# insulin_signal = “MALWMRLLPLLALLALWGPDPAAA”
# Realize as seguintes tarefas: 


# a) Retorne o tamanho da sequência apresentada.

seq2 = "MALWMRLLPLLALLALWGPDPAAA"

print(len(seq2))

# b) Quebre a sequência no trecho “LLALLALWG".

print(seq2.split("LLALLALWG"))

# c) Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA.

nova_seq2 = "".join(seq2)
print(nova_seq2)

# d) Substitua o trecho "DPAAA" por “LLALL”. 

seq3 = nova_seq2.replace("DPAAA", "LLALL")
print(seq3)


# 4. Com base na sequência de DNA GATGGAACTTGACGTAAACCTATATT retorne a sequência de RNA
# correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU.

dna = "GATGGAACTTGACGTAAACCTATATT"

rna = dna.replace("T", "U")

print(rna)