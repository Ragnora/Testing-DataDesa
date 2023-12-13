import os,csv

data = [{'NIK': 3525015201880002, 'Nama': 'Ragnora', 'Jenis Kelamin': 'Perempuan', 'Umur': 20,'Alamat': 'Banyuwangi','No HP': '081'},
        {'NIK': 3123456789123456, 'Nama': 'Blurryface', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '082'},
        {'NIK': 3525016005650004, 'Nama': 'Nycto', 'Jenis Kelamin': 'Perempuan', 'Umur': 17, 'Alamat': 'Situbondo','No HP': '083'},
        {'NIK': 3525015306780002, 'Nama': 'Ananda', 'Jenis Kelamin': 'Perempuan', 'Umur': 18, 'Alamat': 'Banyuwangi','No HP': '084'},
        {'NIK': 3525015306780002, 'Nama': 'Lintang', 'Jenis Kelamin': 'Perempuan', 'Umur': 21, 'Alamat': 'Jember','No HP': '085'},
        {'NIK': 3525017006730060, 'Nama': 'Ari', 'Jenis Kelamin': 'Laki-Laki', 'Umur': 21, 'Alamat': 'Kediri','No HP': '086'},
        {'NIK': 3525016401830001, 'Nama': 'Dika', 'Jenis Kelamin': 'Laki-laki', 'Umur': 21, 'Alamat': 'Jember','No HP': '087'},
        {'NIK': 3314076404720003, 'Nama': 'Hans', 'Jenis Kelamin': 'Laki-laki', 'Umur': 21, 'Alamat': 'Jember','No HP': '088'},
        {'NIK': 3525016401830001, 'Nama': 'Astrophille', 'Jenis Kelamin': 'Perempuan', 'Umur': 18, 'Alamat': 'Surabaya','No HP': '089'}]

def clean():
    os.system('cls')

def login():
    user = []
    with open ('user.csv') as usr:
        username = csv.reader(usr)
        for i in username:
            user.append(i)

    un = input('Username: ')
    pw = input('Password: ')
    print('')

    if [un, pw] in user:
        halamanUtama()
    else:
        print('\t\t      Username atau Password Salah!')

def menu():
    clean()

    print('='*73)
    print('\t\t\t     SELAMAT DATANG')
    print('='*73)

    print('\t\t Silahkan Masukan Username dan Password!')
    print(' ')

    login()
    
    print('-'*73)

    print('')
    input('Ketik Apapun Untuk Memuat Ulang: ')

    clean()
    menu()

def halamanUtama():
    clean()

    print('='*73)
    print('\t\t\t  DATA PENDUDUK')
    print('='*73)
    print(' ')
    print('Pilih menu: ')
    print('1. Cari Data')
    print('2. Tampilkan Data')
    print('3. Tambah Data')
    print('4. Perbarui Data')
    print('5. Hapus Data')
    print('6. Keluar Program')

    print(' ')
    user_input = input('Pilih Nomor: ')
    print(' ')

    if user_input == '1':
        dataFilter()
    elif user_input == '2':
        dataSort()
    elif user_input == '3':
        tambahData()
        print('-'*73)
        print('')
        input('Ketik Apapun Untuk Memuat Ulang: ')
        halamanUtama()
    elif user_input == '4':
        updateData()
        print('-'*73)
        print('')
        input('Ketik Apapun Untuk Memuat Ulang: ')
        halamanUtama()
    elif user_input == '5':
        hapusData()
        print('-'*73)
        print('')
        input('Ketik Apapun Untuk Memuat Ulang: ')
        halamanUtama()
    elif user_input == '6':
        clean()
        exit()
    else:
        print('\t\t    Pilih Sesuai Nomor Yang Tersedia!')
    print('-'*73)

    print(' ')
    input('Ketik Apapun Untuk Memuat Ulang: ')
    halamanUtama()

def tambahData():
    clean()

    print('='*73)
    print('\t\t\t    Tambah Data Penduduk')
    print('='*73)

    nik = input('NIK: ')
    nama = input('Nama: ')
    jenis_kelamin = input('Jenis Kelamin: ')
    umur = input('Umur: ')
    alamat = input('Alamat: ')
    no_hp = input('No HP: ')

    if (nik == '') or (nama == '') or (jenis_kelamin == '') or (umur == '') or (alamat == '') or (no_hp == ''):
        print('\n\t\t\t      Masukkan Data dengan Benar!')
        return

    data_baru = {
        'NIK': int(nik),
        'Nama': nama,
        'Jenis Kelamin': jenis_kelamin,
        'Umur': int(umur),
        'Alamat': alamat,
        'No HP': no_hp
    }
    data.append(data_baru)

    print('\n\t\t\t      Data telah ditambahkan')

def updateData():
    clean()

    print('='*73)
    print('\t\t\t    Perbarui Data Penduduk')
    print('='*73)
    print('(Lihat index data dari tampilan data default)')
    index = int(input('Index data: '))

    if index < 0 or index >= len(data):
        print('\t\t\t    Masukkan index data dengan benar')
        return
    print(' ')

    nik = input('NIK: ')
    nama = input('Nama: ')
    jenis_kelamin = input('Jenis Kelamin: ')
    umur = input('Umur: ')
    alamat = input('Alamat: ')
    no_hp = input('No HP: ')

    if (nik == '') or (nama == '') or (jenis_kelamin == '') or (umur == '') or (alamat == '') or (no_hp == ''):
        print('\n\t\t\t      Masukkan Data dengan Benar!')
        return

    data_baru = {
        'NIK': int(nik),
        'Nama': nama,
        'Jenis Kelamin': jenis_kelamin,
        'Umur': int(umur),
        'Alamat': alamat,
        'No HP': no_hp
    }
    data[index] = data_baru

    print('\n\t\t\t      Data telah diupdate')

def hapusData():
    clean()

    print('='*73)
    print('\t\t\t    Hapus Data Penduduk')
    print('='*73)

    print('(Lihat index data dari tampilan data default)')
    index = int(input('Index data: '))

    if index < 0 or index >= len(data):
        print('\n\t\t\t    Masukkan index data dengan benar')
        return

    data.pop(index)

    print('\n\t\t\t      Data berhasil dihapus')

#--------------------------------------------------FILTER---------------------------------------------------#
def dataFilter():
    clean()

    print('='*73)
    print('\t\t\t  CARI DATA')
    print('='*73)

    print(' ')
    print('Cari data berdasarkan: ')
    print('1. NIK')
    print('2. Nama')
    print('3. Umur')
    print('4. Alamat')
    print('5. No HP')
    print('6. Kembali')
    print(' ')

    user = input('Pilih Nomor: ')
    print(' ')

    if user=='1':
        dataFilterNIK()
    elif user=='2':
        dataFilterNama()
    elif user=='3':
        dataFilterUmur()
    elif user=='4':
        dataFilterAlamat()
    elif user=='5':
        dataFilterNoHP()
    elif user=='6':
        halamanUtama()
    else:
        print('\t\t    Pilih Sesuai Nomor Yang Tersedia!')
    print('-'*73)

    print(' ')
    input('Ketik Apapun Untuk Memuat Ulang: ') 
    dataFilter()

def dataFilterNIK():
    clean()
    user = input('Masukan NIK: ')
    nik = [dataNIK for dataNIK in data if dataNIK['NIK']==int(user)] 
    clean()
    if nik :
        for i in nik:
            print(f"\nNIK : {i['NIK']}")
            print(f"Nama : {i['Nama']}")
            print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
            print(f"Umur : {i['Umur']}")
            print(f"Alamat : {i['Alamat']}")
            print(f"No HP : {i['No HP']}")
    else :
        print("Data tidak ditemukan")

def dataFilterNama():
    clean()
    user = input('Masukan Nama: ')
    nama = [dataNama for dataNama in data if dataNama['Nama']==user] 
    clean()
    if nama :
        for i in nama:
            print(f"\nNIK : {i['NIK']}")
            print(f"Nama : {i['Nama']}")
            print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
            print(f"Umur : {i['Umur']}")
            print(f"Alamat : {i['Alamat']}")
            print(f"No HP : {i['No HP']}")
    else :
        print("Data tidak ditemukan")

def dataFilterUmur():
    clean()
    user = input('Masukan Umur: ')
    umur = [dataUmur for dataUmur in data if dataUmur['Umur']==int(user)] 
    clean()
    if umur :
        for i in umur:
            print(f"\nNIK : {i['NIK']}")
            print(f"Nama : {i['Nama']}")
            print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
            print(f"Umur : {i['Umur']}")
            print(f"Alamat : {i['Alamat']}")
            print(f"No HP : {i['No HP']}")
    else :
        print("Data tidak ditemukan")

def dataFilterAlamat():
    clean()
    user = input('Masukan Alamat: ')
    alamat = [dataNama for dataNama in data if dataNama['Alamat']==user] 
    clean()
    if alamat :
        for i in alamat:
            print(f"\nNIK : {i['NIK']}")
            print(f"Nama : {i['Nama']}")
            print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
            print(f"Umur : {i['Umur']}")
            print(f"Alamat : {i['Alamat']}")
            print(f"No HP : {i['No HP']}")
    else :
        print("Data tidak ditemukan")

def dataFilterNoHP():
    clean()
    user = input('Masukan No HP: ')
    noHP = [dataNoHP for dataNoHP in data if dataNoHP['No HP']==user] 
    clean()
    if noHP :
        for i in noHP:
            print(f"\nNIK : {i['NIK']}")
            print(f"Nama : {i['Nama']}")
            print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
            print(f"Umur : {i['Umur']}")
            print(f"Alamat : {i['Alamat']}")
            print(f"No HP : {i['No HP']}")
    else :
        print("Data tidak ditemukan")
#-----------------------------------------------------------------------------------------------------------#


#---------------------------------------------------SORT----------------------------------------------------#
def dataSort():
    clean()

    print('='*73)
    print('\t\t\t  TAMPILKAN DATA PENDUDUK')
    print('='*73)

    print(' ')
    print('Urutkan data berdasarkan: ')
    print('1. Default')
    print('2. Nama')
    print('3. Umur')
    print('4. Alamat')
    print('5. Kembali')

    print(' ')
    user = input('Pilih Nomor: ')
    print(' ')

    if user=='1':
        clean()
        dataWithOutSort(data)
    elif user=='2':
        clean()
        dataSortNama(data)
    elif user=='3':
        clean()
        dataSortUmur(data)
    elif user=='4':
        clean()
        dataSortAlamat(data)
    elif user=='5':
        clean()
        halamanUtama()
    else:
        print('\t\t    Pilih Sesuai Nomor Yang Tersedia!')
    print('-'*73)

    print(' ')
    input('Ketik Apapun Untuk Memuat Ulang: ')
    dataSort()

def dataWithOutSort(data):
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('='*73)

    no = 0
    for i in data:
        print(f"\nNo : {no}")
        print(f"NIK : {i['NIK']}")
        print(f"Nama : {i['Nama']}")
        print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
        print(f"Umur : {i['Umur']}")
        print(f"Alamat : {i['Alamat']}")
        print(f"No HP : {i['No HP']}")
        no += 1

    print('-'*73)

def dataSortNama(data):
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t       Menurut Nama')
    print('='*73)

    data_ = data
    data_.sort(key=lambda x:x['Nama'])

    no = 0
    for i in data_:
        print(f"\nNo : {no}")
        print(f"NIK : {i['NIK']}")
        print(f"Nama : {i['Nama']}")
        print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
        print(f"Umur : {i['Umur']}")
        print(f"Alamat : {i['Alamat']}")
        print(f"No HP : {i['No HP']}")
        no += 1

    print('-'*73)

def dataSortUmur(data):
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t       Menurut Umur')
    print('='*73)

    data_ = data
    data_.sort(key=lambda x:x['Umur'])

    no = 0
    for i in data_:
        print(f"\nNo : {no}")
        print(f"NIK : {i['NIK']}")
        print(f"Nama : {i['Nama']}")
        print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
        print(f"Umur : {i['Umur']}")
        print(f"Alamat : {i['Alamat']}")
        print(f"No HP : {i['No HP']}")
        no += 1

    print('-'*73)

def dataSortAlamat(data):
    print('='*73)
    print('\t\t\t    DATA PENDUDUK DESA')
    print('\t\t\t       Menurut Alamat')
    print('='*73)

    data_ = data
    data_.sort(key=lambda x:x['Alamat'])
    
    no = 0
    for i in data_:
        print(f"\nNo : {no}")
        print(f"NIK : {i['NIK']}")
        print(f"Nama : {i['Nama']}")
        print(f"Jenis Kelamin : {i['Jenis Kelamin']}")
        print(f"Umur : {i['Umur']}")
        print(f"Alamat : {i['Alamat']}")
        print(f"No HP : {i['No HP']}")
        no += 1

    print('-'*73)
#-----------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    menu()