import numpy as np
import socket
import time

def matrix2str(mtx):
    (row, col) = mtx.shape
    return_str = ''
    for i in xrange(row):
        for j in xrange(col):
            if j == 0:
                return_str = return_str + str(mtx[i][j])
                #print return_str 
            else:
                return_str = return_str + ',' + str(mtx[i][j])
                #print return_str
        return_str = return_str + '\n'
    return return_str

def str2matrix(string):
    mtx = np.array([[float(j) for j in i.split(',')] for i in string.splitlines()])
    return mtx

def tcpServer(data_to_client):
    host = socket.gethostname()
    # host = '127.0.0.1'
    # host = '172.20.40.51'
    port = 50000

    MAX_WAITING_TIME = 300
    MAX_SEQ_LENGTH = 10000

    s = socket.socket()
    s.bind((host,port))
    s.listen(MAX_WAITING_TIME) # only listen for one connection for one time
    c, addr  = s.accept()
    print "Connection from: "+ str(addr)
    while True:
        data_from_client = c.recv(MAX_SEQ_LENGTH)
        if not data_from_client:
            break
        print "Recieved from Client \n" # + str(str2matrix(data_from_client))
        # data_to_client = generate_sequential_data()
        print "Sending to Client \n"  #+str(str2matrix(data_to_client))
        c.send(data_to_client)
        return data_from_client
    c.close()
    

def tcpClient(data_to_server):
    host = '129.22.151.209'
    #host = '127.0.0.1'
    port = 50000

    s = socket.socket()
    s.connect((host,port))

    MAX_WAITING_TIME = 300
    MAX_SEQ_LENGTH = 10000
    # while True:
    #     try:
            #time.sleep(1)  # do something here
    # print 'Server Connected...\n',
    print 'data_to_server', data_to_server
    s.send(data_to_server)
    print "Sending to Server \n"#+str(str2matrix(data_to_server))
    data_from_server = s.recv(MAX_SEQ_LENGTH)
    print "Recieved from Server \n" #+ str(str2matrix(data_from_server))
    return data_from_server
    s.close()