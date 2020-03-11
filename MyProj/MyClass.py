"""
    main class to download file from the Remote Server using SFTP connection and
    read & parse to store the data into MongoDB

"""
#from src.Files.files import Files

from RS.SFTPConnectRS import SFTPConnectRS
from File.FileImpl import FileImpl

if __name__ == "__main__":
    host = ""
    user = ""
    password = ""
    cnopts = ""
    #connect to Remote Server
    abc = SFTPConnectRS(host, user, password, cnopts)
    print "Connection Successful"


    remotePath = "C:\\Users\\USER\\Desktop\\Assignment\\SrcFile\\"
    localPath = "C:\\Users\\USER\\Desktop\\Assignment\\DestFile\\"

    filesObj = FileImpl(remotePath, localPath)
    fileObj.connect_remote_server()
    filesObj.download()
    filenames = filesObj.read_all_filename()
    db = MongoDB(uri,"mydb")
    filesObj.insert_files(filenames)
    print "Download Successful"

