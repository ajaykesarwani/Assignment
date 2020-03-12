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
    print "Download Successful"

    filenames = filesObj.read_all_filename()
    db = MongoDB(uri,"mydb")
    print " Connection to MongoDB successful"
    filesObj.store_document(filenames)
    print " Data is successfully stored in DB"
    
