from ftplib import FTP

ftp_client = FTP('ftp.be.debian.org')
print("Serwer:", ftp_client.getwelcome())
print(ftp_client.login())
print("Pliki i katalogi które znajdują się w głównym katalogu:", ftp_client.dir())

ftp_client.cwd('mint-iso/stable/21.2')
files = ftp_client.nlst()
files.sort()
print("%d plików/katalogów w katalogu" %len(files))
for file in files:
    print(file)

