#standard imports for web fetching and sockets to connect to PM server.
import urllib2 as url
import urllib
import socket
 
#global auid placeholder.
global auid;
auid = ''
 
#global username placeholder till filled.
global username;
username = 'koda'
 
#global password placeholder untill filled.
global password;
password = 'something'
 
#global host var to hold the server address.
global host;
host = 'c1.chatango.com'
 
#global port var to hold the port number.
global port;
port = 5222;
 
#specifying the link to chatango login
link = "http://chatango.com/login"
 
#setting the params to be sent to the login.
params = urllib.urlencode({
        'user_id':username,
        'password':password,
        'storecookie':'on',
        'checkerrors':'yes'
})
 
#sending the post request
req = url.Request(link,params)
 
#opening and reading the return transfer.
resp = url.urlopen(req)
 
#retrieving the headers so we can grab the auid
headers = resp.headers
 
#now we grab the auid
for header,value in headers.items():
    if header.lower() == "set-cookie":
        a = value.split("=");
        leftover = a[9];
        auid = leftover[0:80]; #storing the auid in the global variable.
 
###########################################################################################################
#now that we have the auid from the login page, we may now proceed onwards and connect to the Pm server.
###########################################################################################################
 
#create the socket.
sock = socket.socket()
 
#connect to the host through the specified port.
sock.connect((host,port))
 
##################################################
#here is the fun part, actually logging in :)
##################################################
 
#we will send a command to log the account into chatango.
sock.send("tlogin:" + auid + ":2\x00") #tlogin:your auid here:version 2\x00
 
#################################################################################################################################
#now the account should be online, so to keep it online and not just login and logout instantly, we will make a while true loop to #print whatever we receive to the console.
#################################################################################################################################
 
while True:
        print sock.recv(1024) #prints 1024 bytes of data received from the socket.
