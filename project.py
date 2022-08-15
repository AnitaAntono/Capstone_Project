from tkinter import Y


exit = 'N'

nik = []
nama = []
gender = []
divisi = []
alamat = []

while exit != 'Y':
    print('\n Menu Manajemen Data Karyawan')
    print('1. Report Data Karyawan')
    print('2. Menambahkan Data Karyawan')
    print('3. Merubah Data Karyawan')
    print('4. Menghapus Data Karyawan')
    print('5. Exit')

    pilih = int(input('Silahkan Pilih Menu: '))

    if pilih == 1:
        print('\n Menu menampilkan data: ')
        print('1. Tampilkan semua data')
        print('2. Tampilkan data sebagian')
        print('3. Kembali ke menu utama')
        pilih1 = int(input('Pilih 1-3: '))


        if pilih1 == 1:
            print('\n')
            for i in range (len(nik)):
                print(f'{i+1} NIK:{nik[i]}, Nama: {nama[i]}, Gender: {gender[i]},Divisi: {divisi[i]}, Alamat: {alamat[i]}')
        elif pilih1 == 2:
            input_nik = input('Masukan NIK: ')
            i = nik.index(input_nik)
            print(f'\n NIK:{nik[i]}, Nama: {nama[i]}, Gender: {gender[i]}, Divisi: {divisi[i]}, Alamat: {alamat[i]}')
        elif pilih1 == 3:
            pass
        else:
            print('Inputan Salah')


    elif pilih == 2:
        print('\n Menu menambahkan data')
        print('1. Menambahkan data')
        print('2. Kembali ke menu utama')
        pilih2 = int(input('Pilih 1-2: '))
        if pilih2 == 1:
            input_nik = input('Masukan NIK: ')
            if input_nik in nik:
                print('Data sudah ada')
            else:
                input_nama = input('Masukan Nama: ')
                input_gender = input('Masukan Gender: ')
                input_divisi = input('Masukan Divisi: ')
                input_alamat = input('Masukan Alamat: ')
                simpan = input('Apakah input data disimpan? (Y/N)')
                if simpan == 'Y':
                    nik.append(input_nik)
                    nama.append(input_nama)
                    gender.append(input_gender)
                    divisi.append(input_divisi)
                    alamat.append(input_alamat)
                    print('Selamat Data Tersimpan')
                elif simpan == 'N':
                    print('Data Tidak Tersimpan')
                else:
                    print('Inputan Salah')


        elif pilih2 == 2:
            pass
        else:
            pass
            



    elif pilih == 3:
         print('\n Menu Merubah Data')
         print('1. Merubah Data Karyawan')
         print('2. Kembali ke menu utama')
         pilih3 = int(input('Pilih 1-2: '))
         if pilih3 == 1:
            input_nik = input('Masukan NIK: ')
            while input_nik not in nik:
                print('Data tidak ada')
                print('\n Menu Merubah Data')
                print('1. Merubah Data Karyawan')
                print('2. Kembali ke menu utama')
                pilih3 = int(input('Pilih 1-2: ')) 
                if pilih3 == 1:
                    input_nik = input('Masukan NIK: ')
            else:
                i = nik.index(input_nik)
                print(f'\n NIK:{nik[i]}, Nama: {nama[i]}, Gender: {gender[i]}, Divisi: {divisi[i]}, Alamat: {alamat[i]}')
                lanjut = input('Tekan Y jika ingin lanjut update data atau N jika ingin cancel update (Y/N): ')
                if lanjut == 'Y':
                    data = input('Masukan kolom / keterangan yg ingin di edit: ')
                    kolom = {'NIK': nik, 'Nama': nama, 'Gender': gender, 'Divisi': divisi, 'Alamat': alamat} 
                    if data in kolom.keys():
                        baru = input(f'Masukan {data} baru: ')
                        kolom[data][i] = baru
                        print('Data berhasil diubah')
                        print(f'\n NIK:{nik[i]}, Nama: {nama[i]}, Gender: {gender[i]}, Divisi: {divisi[i]}, Alamat: {alamat[i]}')
                    else:
                        print('Data yang ingin diubah tidak ada')
                elif lanjut == 'N':
                    pass
                else:
                    print('Inputan salah')


    elif pilih == 4:
         print('\n Menu Menghapus Data')
         print('1. Menghapus Data Karyawan')
         print('2. Kembali ke menu utama')
         pilih4 = int(input('Pilih 1-2: '))
         if pilih4 == 1:
            input_nik = input('Masukan NIK: ')
            while input_nik not in nik:
                print('Data tidak ada')
                print('\n Menu Menghapus Data')
                print('1. Menghapus Data Karyawan')
                print('2. Kembali ke menu utama')
                pilih4 = int(input('Pilih 1-2: ')) 
                if pilih4 == 1:
                    input_nik = input('Masukan NIK: ')
            else:
                lanjut = input('Yakin menghapus? (Y/N): ')
                if lanjut == 'Y':
                    i = nik.index(input_nik)
                    del nik[i]
                    del nama[i]
                    del gender[i]
                    del divisi[i]
                    del alamat[i]
                    print('Data berhasil dihapus')
                elif lanjut == 'N':
                    pass
                else:
                    print('Inputan Salah')

        
        
    elif pilih == 5:
        exit = input('Yakin keluar? (Y/N)')
        if exit == 'Y':
            print('Terima Kasih')
        elif exit == 'N':
            pass
        else:
            print('Inputan Salah')
    else:
        pass

        




