import string




#simple Chiper Text Caesar Generation
#2019 Hansrenee Willysandro


#Inisialisasi variabel public

list_alfabet_kecil = 'abcdefghijklmnopqrstuvwxyz'
list_alfabet_besar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getIndexKecil(karakter):
    indeks = 0
    while indeks < len(list_alfabet_kecil):
        if list_alfabet_kecil[indeks] == karakter:
            break
        indeks = indeks + 1
        #print(indeks)
    return indeks




def getIndexBesar(karakter):
    indeks = 0
    while indeks < len(list_alfabet_kecil):
        if list_alfabet_besar[indeks] == karakter:
            indeks = indeks + 1
            break
    return indeks

#---------------------------------------------------------

pesan = raw_input("Masukan Pesan yang ingin di chiper: ")
shift_alfabet = input("Masukan shifting alfabet untuk menghasilkan chiper: ")


pesan_chiper = ""
indeks = 0

while indeks < len(pesan):
    if pesan[indeks].islower():
        #################
        indeks_ambil = getIndexKecil(pesan[indeks])

        
    else:
        ###############
        indeks_ambil = getIndexBesar(pesan[indeks])

    if indeks_ambil + shift_alfabet < 26:
        pesan_chiper = pesan_chiper + list_alfabet_kecil[indeks_ambil + 5]
    else:
        total = indeks_ambil + shift_alfabet
        selisih = total - 26
        pesan_chiper = pesan_chiper + list_alfabet_kecil[selisih]

    indeks = indeks + 1

print(pesan_chiper)

