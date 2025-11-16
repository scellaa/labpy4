data_mahasiswa=[]

while True:
    name=input('Nama Mahasiswa: ')
    nim=input('NIM Mahasiswa: ')
    nilai_t= float(input('Nilai Tugas: '))
    nilai_UTS=float(input('Nilai UTS: '))
    nilai_Uas=float(input('Nilai UAS: '))

    nilai_akhir= (nilai_t * 0.30) + (nilai_UTS *0.35) + (nilai_Uas * 0.35)
    data_mahasiswa.append([name, nim, nilai_t, nilai_UTS, nilai_Uas, nilai_akhir])

    masukan_data_lagi= input('masukan data lagi? (ya/tidak):')
    if masukan_data_lagi.lower() == "tidak":
        break
    
print("=" * 65)
print(f"| {'NO':^2} | {'NAMA':^10} | {'NIM':^9} | {'TUGAS':^5} | {'UTS':^4} | {'UAS':^4} | {'AKHIR':^9} |")
print("=" * 65)

no = 1
for mhs in data_mahasiswa:
    print(f"| {no:^3}| {mhs[0]:^10} | {mhs[1]:^8} | {mhs[2]:^5} | {mhs[3]:^3} | {mhs[4]:^3} | {mhs[5]:^8.1f}  |")
    no += 1
