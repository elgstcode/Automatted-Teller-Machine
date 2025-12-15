# import library
import time
import os
import sys
import random

# fungsi membaca file eksternal
def rdFile(file):
    with open(f'{file}', 'r') as read:
        return read.readlines()

# fungsi menulis file external
def wrtFile(file, string):
    with open(f'{file}', 'w') as write:
        write.write(string)

#fungsi menambah data file eksternal
def appFile(file, string):
    with open(f'{file}', 'a') as append:
        append.write(string)

# fungsi konversi biner ke string
def biStr(biner):
    # Memastikan panjang string biner adalah kelipatan 8
    if len(biner) % 8 != 0:
        raise ValueError("Panjang string biner tidak valid.")
    return bytes([int(biner[i:i+8], 2) for i in range(0, len(biner), 8)]).decode('utf-8')

# fungsi konversi string ke biner
def strBi(string):
    return ''.join(format(byte, '08b') for byte in string.encode('utf-8'))

# deklarasi data awal
daRek = rdFile('server//rekData.txt') #bentuk biner belum di strip
cant = rdFile('server//wr.txt')
lp = 1
n = 1

# program utama
while True:
    # menu login atau buat akun
    while True:
        os.system('clear')
        i = input((f'{('='*100).center(100)}\n{('Selamat Datang di MintCherry Bank').center(100)}\n{('='*100).center(100)}\n1. log in\n2. log up\n{('-'*100).center(100)}\ninput anda: '))
        if i == '1':
            # input rekening
            while True:
                os.system('clear')
                nRek = input(f'{('='*100).center(100)}\n{('Selamat Datang di MintCherry Bank').center(100)}\n{('='*100).center(100)}\nMasukkan No Rekening Anda: ')
                if len(nRek) == 10:
                    os.system('clear')
                    if f'{nRek}-3\n' in cant:
                        slp = 3
                        while slp >= 0:
                            os.system('clear')
                            print(f'no rekening anda telah diblokir\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                            time.sleep(1)
                            slp -= 1
                        sys.exit()
                    break
                else:
                    print('panjang rekening tidak valid')
                    time.sleep(3)
                    os.system('clear')
    
            # input pin
            while True:
                print((f'{('='*100).center(100)}\n{('Selamat Datang di MintCherry Bank').center(100)}\n{('='*100).center(100)}'))
                pin = input('Masukkan No PIN Anda: ')
                if len(pin) == 6:
                    os.system('clear')
                    break
                else:
                    print('panjang pin tidak valid')
                    time.sleep(3)
                    os.system('clear')
            break
        
        if i == '2':
            # input nama
            os.system('clear')
            name = input(f'pengisian data diri\nnama anda: ')

            while True:
                # input pin
                while True:
                    os.system('clear')
                    pin1 = input('input pin baru: ')
                    if len(pin1) == 6:
                        break
                    else:
                        print('panjang pin tidak valid')
                        time.sleep(3)

                # konfirmasi pin
                while True:
                    os.system('clear')
                    pin2 = input('konfirmasi pin baru: ') 
                    if len(pin2) == 6:
                        break
                    else:
                        print('panjang pin tidak valid')
                        time.sleep(3)

                if pin1 == pin2:
                    break

                else:
                    os.system('clear')
                    print('PIN yang anda masukkan salah')
                    time.sleep(3)

            while True:
                # random untuk rekening baru
                new = ""
                for len in range(10):
                    rek = str(random.randint(0,9))
                    new = new + rek
                    get = ""
                if not strBi(new) in daRek[:(10*8)]:
                    appFile('server//rekData.txt', f'{strBi(f'{new+pin1+'0'+f'-{name.capitalize()}'}')}\n')
                    os.system('clear')
                    input(f'Selamat! akun anda telah dibuat dengan \nnomor rekening {new}\nPIN {pin1}\ntekan enter untuk melanjutkan')
                    break

        else:
            input('input anda salah')
            os.system('clear')

    # autentikasi
    for key in daRek:

        # menghapus data gagal login ketika sudah berhasil
        if f'{nRek}{pin}' == biStr((key).strip())[:16]:
            if f'{nRek}-1\n' in cant:
                cant.remove(f'{nRek}-1\n')
                wrtFile('server//wr.txt', '')
                for cantKey in cant:
                    appFile('server//wr.txt', f'{cantKey}')
            if f'{nRek}-2\n' in cant:
                cant.remove(f'{nRek}-2\n')
                wrtFile('server//wr.txt', '')
                for cantKey in cant:
                    appFile('server//wr.txt', f'{cantKey}')
            
            # data akun
            account = biStr((key).strip()).split('-') # [kondisiRekPin, Nama]

            # menu opsi transaksi
            while True:
                while True:
                    os.system('clear')
                    chc = input((f'{('='*100).center(100)}\n{(f'Halo {account[1]}').center(100)}\n{('-'*100).center(100)}\n{(f'Pilih transaksi yang akan di lakukan').center(100)}\n{('='*100).center(100)}\n1. cek saldo\n2. Tarik tunai\n3. Setor tunai\n4. Pengaturan akun\n5. Keluar\n{('-'*100).center(100)}\nPilihan Anda: '))
                    if chc == '1' or chc == '2' or chc == '3' or chc == '4' or chc == '5':
                        os.system('clear')
                        break
                    else:
                        print('pilihan tidak valid')
                        time.sleep(3)
                        os.system('clear') 

                # cek saldo
                if chc == '1':
                    input(f'{('='*100).center(100)}\n{(f'Halo {account[1]}').center(100)}\n{('-'*100).center(100)}\n{(f'Saldo anda Rp {account[0][16:]},-').center(100)}\n{('='*100).center(100)}\ntekan enter untuk melanjutkan')

                # tarik tunai
                if chc == '2':
                    while True:
                        # tampilan
                        amount = input(f'{('='*100).center(100)}\nMasukkan Jumlah Penarikan\n{('-'*100).center(100)}\nkelipatan Rp 50.000,- dan Rp 100.000,- || minimal Rp50.000,- maksimal Rp 10.000.000,-\n{('='*100).center(100)}\ninput anda: ')

                        # memastikan input benar
                        if int(amount) > int(account[0][16:]) or int(amount) > 10_000_000 or int(amount)%50_000 != 0 or int(amount)%100_000 != 0 or int(amount) < 50_000:
                            input('Jumlah penarikan tidak valid atau saldo tidak cukup')
                            os.system('clear')
                            break

                        else:
                            # mengubah data lama ke data baru
                            daRek.remove(f'{strBi(f'{account[0]}-{account[1]}')}\n')
                            daRek.append(f'{strBi(f'{account[0][:16]}{int(account[0][16:])-int(amount)}-{account[1]}')}\n')
                            account[0] = f'{account[0][:16]}{int(account[0][16:])-int(amount)}'

                            # mengahapus data lama di file eksternal
                            wrtFile('server//rekData.txt', '')

                            # upload data baru di file
                            for get in daRek:
                                appFile('server//rekData.txt', get)
                            
                            # tampilan konfirmasi
                            slp = 3
                            while slp >= 0:
                                os.system('clear')
                                print(f'Saldo telah ditarik sebanyak Rp {amount},-\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                                time.sleep(1)
                                slp -= 1
                            break
                
                # tambah saldo
                if chc == '3':
                    while True:
                        # tampilan
                        amount = input(f'{('='*100).center(100)}\nMasukkan Jumlah setoran\n{('-'*100).center(100)}\nkelipatan Rp 50.000,- dan Rp 100.000,- || minimal Rp50.000,- maksimal Rp 10.000.000,-\n{('='*100).center(100)}\ninput anda: ')

                        # memastikan input benar
                        if int(amount) > 10_000_000 or int(amount)%50_000 != 0 or int(amount)%100_000 != 0 or int(amount) < 50_000:
                            input('Jumlah setoran tidak valid')
                            os.system('clear')
                            break

                        else:
                            # mengubah data lama ke data baru
                            daRek.remove(f'{strBi(f'{account[0]}-{account[1]}')}\n')
                            daRek.append(f'{strBi(f'{account[0][:16]}{int(account[0][16:])+int(amount)}-{account[1]}')}\n')
                            account[0] = f'{account[0][:16]}{int(account[0][16:])+int(amount)}'

                            # mengahapus data lama di file eksternal
                            wrtFile('server//rekData.txt', '')

                            # upload data baru di file
                            for get in daRek:
                                appFile('server//rekData.txt', get)
                            
                            # tampilan konfirmasi
                            slp = 3
                            while slp >= 0:
                                os.system('clear')
                                print(f'Saldo telah ditambahkan sebanyak Rp {amount},-\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                                time.sleep(1)
                                slp -= 1
                            break
                
                # pengaturan akun
                if chc == '4':
                    while True:
                        chc = input(f'{('='*100).center(100)}\n1. Ubah pin\n2. hapus akun\n3. kembali\n{('='*100).center(100)}\nInput anda: ')
                        if chc == '1' or chc == '2' or chc == '3':
                            os.system('clear')
                            break
                        else:
                            input('input anda salah')
                            os.system('clear')
                    
                    # pembaruan PIN
                    if chc == '1':
                        while True:
                            old = input(f'{('='*100).center(100)}\nMasukkan PIN lama: ')
                            if int(old) == int(account[0][10:16]):
                                while True:

                                    # input pin pertama
                                    while True:
                                        new1 = input(f'{('='*100).center(100)}\nMasukkan PIN baru: ')
                                        if len(new1) == 6:
                                            break
                                        else:
                                            print('panjang pin salah')
                                            time.sleep(3)
                                            os.system('clear')

                                    # input konfirmasi
                                    while True:
                                        new2 = input(f'{('-'*100).center(100)}\nKonfirmasi PIN baru: ')
                                        if len(new1) == 6:
                                            break
                                        else:
                                            print('panjang pin salah')
                                            time.sleep(3)
                                            os.system('clear')

                                    # jika pin dan konfirmasi beda
                                    if new1 != new2:
                                        print('input PIN salah')

                                    # jika pin benar
                                    if new1 == new2:
                                        daRek.remove(f'{strBi(f'{account[0]}-{account[1]}')}\n')
                                        daRek.append(f'{strBi(f'{account[0][:10]}{new1}{int(account[0][16:])}-{account[1]}')}\n')
                                        wrtFile('server//rekData.txt', '')
                                        for get in daRek:
                                            appFile('server//rekData.txt', get)

                                        slp = 3
                                        while slp >= 0:
                                            os.system('clear')
                                            print(f'PIN telah diganti\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                                            time.sleep(1)
                                            slp -= 1
                                        break
                                break
                    
                            else:
                                print('PIN lama salah')
                                time.sleep(3)
                                os.system('clear')

                    # menghapus akun
                    if chc == '2':
                        while True:
                            con = input('apakah anda yakin akan menghapus akun? y/n')
                            if con.capitalize() == 'Y':
                                daRek.remove(f'{strBi(f'{account[0]}-{account[1]}')}\n')
                                wrtFile('server//rekData.txt', '')
                                for get in daRek:
                                    appFile('server//rekData.txt', get)
                                slp = 3
                                while slp >= 0:
                                    os.system('clear')
                                    print(f'akun telah dihapus\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                                    time.sleep(1)
                                    slp -= 1
                                sys.exit()

                            if con.capitalize() == 'N':
                                break

                            else:
                                print('input anda salah')
                                time.sleep(3)
                                os.sytem('clear')

                # keluar
                if chc == '5':
                    slp = 3
                    while slp >= 0:
                        os.system('clear')
                        print(f'terimakasih telah menggunakan layanan kami\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                        time.sleep(1)
                        slp -= 1
                    sys.exit()

        # konfirmasi data salah
        if f'{nRek}{pin}' != biStr((key).strip())[:16] and len(daRek) == lp:

            # menambah data untuk rekening yang salah sandi
            if f'{nRek}-1\n' in cant:
                cant.remove(f'{nRek}-1\n')
                cant.append(f'{nRek}-2\n')
                wrtFile('server//wr.txt', '')
                for cantKey in cant:
                    appFile('server//wr.txt', f'{cantKey}')
                slp = 3
                while slp >= 0:
                    os.system('clear')
                    print(f'no rekening atau pin salah\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                    time.sleep(1)
                    slp -= 1
                sys.exit()

            if f'{nRek}-2\n' in cant:
                cant.remove(f'{nRek}-2\n')
                cant.append(f'{nRek}-3\n')
                wrtFile('server//wr.txt', '')
                for cantKey in cant:
                    appFile('server//wr.txt', f'{cantKey}')
                slp = 3
                while slp >= 0:
                    os.system('clear')
                    print(f'no rekening atau pin salah\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                    time.sleep(1)
                    slp -= 1
                sys.exit()

            if f'{nRek}-3\n' in cant:
                slp = 3
                while slp >= 0:
                    os.system('clear')
                    print(f'akun anda diblokir karena terlalu banyak percobaan salah\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                    time.sleep(1)
                    slp -= 1
                sys.exit()

            else:
                cant.append(f'{nRek}-1')
                wrtFile('server//wr.txt', '')
                for cantKey in cant:
                    appFile('server//wr.txt', f'{cantKey}\n')
                slp = 3
                while slp >= 0:
                    os.system('clear')
                    print(f'no rekening atau pin salah\n{('='*100).center(100)}\ntunggu 3 detik untuk ATM merespon\n{'*'*slp}')
                    time.sleep(1)
                    slp -= 1
                sys.exit()

        # loading animation
        else:
            os.system('clear')
            if n == 3:
                n = 1
            print(f'mencari data{'.'*n}')
            n += 1
            lp += 1