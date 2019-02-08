from statistics import mean

def extractDatas():
    i = 1
    datas = []
    while (i <= 10):
        text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
        lines = text_file.read().split('{\n')[i]
        data = lines.split(' ')[2]
        datas.append(data)
        print(data)
        i += 1
    print(datas)

def extractHora():
    i = 1
    horas = []
    while (i <= 10):
        text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
        lines = text_file.read().split('{\n')[i]
        data = lines.split(' ')[3]
        horas.append(data)
        i += 1


def extractValue():

        textos = []
        text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
        lines = text_file.read().split('{\n')[1]
        data = lines.split('\n')

        len_data = len(data) - 5
        for i in range (len_data):
            textos.append(data[i+1])

        print(textos[0])
        print(textos[0][45:])

i = 1
datas = []
horas = []
while (i <= 10):
    text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
    lines = text_file.read().split('{\n')[i]
    data = lines.split(' ')[2]
    datas.insert(i - 1, data)

    text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
    lines = text_file.read().split('{\n')[i]
    data = lines.split(' ')[3]
    horas.insert(i - 1, data)

    i += 1

###################################################################################################
###################################################################################################
textos1 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[1]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos1.append(data[i + 1])
len_textos1 = len(textos1)

float_texto1 = []
for i in range(len(textos1)):
    try:
        float_texto1.append(abs(float((textos1[i][37:-11]))))
    except:
        print('Exception no texto 1')
        pass
max1 = str(max(float_texto1))
min1 = str(min(float_texto1))
med1 = str(mean(float_texto1))


textos2 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[2]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos2.append(data[i + 1])
len_textos2 = len(textos2)

float_texto2 = []
for i in range(len(textos2)):
    try:
        float_texto2.append(abs(float((textos2[i][37:-11]))))
    except:
        print('Exception no texto 2')
        pass
max2 = str(max(float_texto2))
min2 = str(min(float_texto2))
med2 = str(mean(float_texto2))

textos3 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[3]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos3.append(data[i + 1])
len_textos3 = len(textos3)

float_texto3 = []
for i in range(len(textos3)):
    try:
        float_texto3.append(abs(float((textos3[i][37:-11]))))
    except:
        print('Exception no texto 3')
        pass
max3 = str(max(float_texto3))
min3 = str(min(float_texto3))
med3 = str(mean(float_texto3))

textos4 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[4]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos4.append(data[i + 1])
len_textos4 = len(textos4)

float_texto4 = []
for i in range(len(textos4)):
    try:
        float_texto4.append(abs(float((textos4[i][37:-11]))))
    except:
        print('Exception no texto 4')
        pass
max4 = str(max(float_texto4))
min4 = str(min(float_texto4))
med4 = str(mean(float_texto4))

textos5 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[5]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos5.append(data[i + 1])
len_textos5 = len(textos5)

float_texto5 = []
for i in range(len(textos5)):
    try:
        float_texto5.append(abs(float((textos5[i][37:-11]))))
    except:
        print('Exception no texto 5')
        pass

max5 = str(max(float_texto5))
min5 = str(min(float_texto5))
med5 = str(mean(float_texto5))

textos6 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[6]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos6.append(data[i + 1])
len_textos6 = len(textos6)

float_texto6 = []
for i in range(len(textos6)):
    try:
        float_texto6.append(abs(float((textos6[i][37:-11]))))
    except:
        print('Exception no texto 6')
        pass
max6 = str(max(float_texto6))
min6 = str(min(float_texto6))
med6 = str(mean(float_texto6))

textos7 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[7]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos7.append(data[i + 1])

float_texto7 = []
for i in range(len(textos7)):
    try:
        float_texto7.append(abs(float((textos7[i][37:-11]))))
    except:
        print('Exception no texto 7')
        pass
max7 = str(max(float_texto7))
min7 = str(min(float_texto7))
med7 = str(mean(float_texto7))

textos8 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[8]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos8.append(data[i + 1])

float_texto8 = []
for i in range(len(textos8)):
    try:
        float_texto8.append(abs(float((textos8[i][37:-11]))))
    except:
        print('Exception no texto 8')
        pass
max8 = str(max(float_texto8))
min8 = str(min(float_texto8))
med8 = str(mean(float_texto8))

textos9 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[9]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos9.append(data[i + 1])

float_texto9 = []
for i in range(len(textos9)):
    try:
        float_texto9.append(abs(float((textos9[i][37:-11]))))
    except:
        print('Exception no texto 9')
        pass
max9 = str(max(float_texto9))
min9 = str(min(float_texto9))
med9 = str(mean(float_texto9))

textos10 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[10]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos10.append(data[i + 1])

float_texto10 = []
for i in range(len(textos10)):
    try:
        float_texto10.append(abs(float((textos10[i][37:-11]))))
    except:
        print('Exception no texto 10')
        pass

max10 = str(max(float_texto10))
min10 = str(min(float_texto10))
med10 = str(mean(float_texto10))

textos11 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[10]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos11.append(data[i + 1])

float_texto11 = []
for i in range(len(textos11)):
    try:
        float_texto11.append(abs(float((textos11[i][37:-11]))))
    except:
        print('Exception no texto 11')
        pass

max11 = str(max(float_texto11))
min11 = str(min(float_texto11))
med11 = str(mean(float_texto11))

textos12 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[10]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos12.append(data[i + 1])

float_texto12 = []
for i in range(len(textos12)):
    try:
        float_texto12.append(abs(float((textos12[i][37:-11]))))
    except:
        print('Exception no texto 12')
        pass

max12 = str(max(float_texto12))
min12 = str(min(float_texto12))
med12 = str(mean(float_texto12))

textos13 = []
text_file = open("/Users/guilhermecarvalho/MEGAsync/MCC_PENITENCIA_1E/LOG/teste_estanqueidade.txt", "r")
lines = text_file.read().split('{\n')[10]
data = lines.split('\n')
len_data = len(data) - 9
for i in range(len_data):
    textos13.append(data[i + 1])

float_texto13 = []
for i in range(len(textos13)):
    try:
        float_texto13.append(abs(float((textos13[i][37:-11]))))
    except:
        print('Exception no texto 13')
        pass

max13 = str(max(float_texto13))
min13 = str(min(float_texto13))
med13 = str(mean(float_texto13))




########## PARAMETROS ###########

text_file = open("bd/parametros.txt", "r")
parametros = text_file.read().split(' ')
p = parametros[:10]

press_max = p[0]
press_min = p[1]
temp_max = p[2]
temp_min = p[3]
umi_max = p[4]
umi_min = p[5]
fluxo_max = p[6]
fluxo_min = p[7]


########## LISTA USUÁRIOS ##########


text_file = open("bd/listaNome.txt", "r")
listaUser = text_file.read().splitlines()

###### LISTA MATRICULA ######

text_file = open("bd/listaMatricula.txt", "r")
listaMatricula = text_file.read().splitlines()

###### LISTA CARGO ######

text_file = open("bd/listaCargo.txt", "r")
listaCargo = text_file.read().splitlines()

###### LISTA EMAIL ######

text_file = open("bd/listaEmail.txt", "r")
listaEmail = text_file.read().splitlines()

###### LISTA MATRICULA ######

text_file = open("bd/listaMatricula.txt", "r")
listaMatricula = text_file.read().splitlines()


###### LISTA RESTRITO ######

text_file = open("bd/listaCliente.txt", "r")
listaCliente = text_file.read().splitlines()

###### LISTA RELATORIO ######

text_file = open("bd/listaRelatorio.txt", "r")
listaRelatorio = text_file.read().splitlines()


###### REMOVE USER ######

# f = open("bd/listaNome.txt","r")
# lines = f.readlines()
# f.close()
# f = open("bd/listaNome.txt","w")
# for line in lines:
#   if line!="Legal Lopes"+"\n":
#     f.write(line)
# f.close()



