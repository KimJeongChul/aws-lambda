import numpy as np
import time

def lambda_handler(event, context):
    A = np.random.rand(event['LR'] , event['LC'])
    B = np.random.rand(event['LC'], event['RC'])
    start_time = time.time()
    C = np.matmul(A, B)
    end_time = time.time()
    print "A shape : " + str(A.shape)
    print "B shape : " + str(B.shape)
    print "C shape : " + str(C.shape)
    print "latency : " + str(end_time - start_time)
