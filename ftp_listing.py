from ftplib import FTP

ftp_server = 'ftp.be.debian.org'
# ftp_client = FTP('ftp.be.debian.org')
download_dir = 'mint-iso/stable/21.2/'
download_file = 'sha256sum.txt'


def ftp_file_download(server, username):
    ftp_client = FTP(server, username)
    ftp_client.cwd(download_dir)
    try:
        with open(download_file, 'wb') as file:
            ftp_cmd = 'RETR %s' % download_file
            ftp_client.retrbinary(ftp_cmd, file.write)
            ftp_client.quit()
    except Exception as e:
        print("Plik nie może zostać ściągnięty", e)


if __name__ == '__main__':
    ftp_file_download(server=ftp_server, username='anonymous')

# print("Serwer:", ftp_client.getwelcome())
# print(ftp_client.login())
# print("Pliki i katalogi które znajdują się w głównym katalogu:", ftp_client.dir())
#
# ftp_client.cwd('mint-iso/stable/21.2')
# files = ftp_client.nlst()
# files.sort()
# print("%d plików/katalogów w katalogu" % len(files))
# for file in files:
#     print(file)
