import asyncio
import logging
from py3iperf3.iperf3_client import Iperf3Client
from py3iperf3.iperf3_api import Iperf3TestProto
from py3iperf3.utils import setup_logging

def get_vm_id():
    buf = open('/proc/self/cgroup').read().split('\n')[-3].split('/')
    vm_id, c_id = buf[1], buf[2]
    return vm_id, c_id

def get_cpuinfo():
    buf = "".join(open("/proc/cpuinfo").readlines())
    cpu_info = buf.replace("\n", ";").replace("\t", "")
    cpu_info = cpu_info.split(';')[4]
    return cpu_info

def get_log():
    log =  open("/tmp/log.out").readlines()
    buf = "".join(log)
    return log, buf

def lambda_handler(event, context):
    vm_id, c_id = get_vm_id()
    cpu_info = get_cpuinfo()

    params = {}
    params['protocol'] = Iperf3TestProto.TCP
    params['server_address'] = event['address']
    params['server-port'] = event['port']
    params['test_duration'] = event['num_test']
    params['get-server-output'] = True
    params['parallel'] = 26
    setup_logging(**params)
        
    loop = asyncio.get_event_loop()
    
    iperf3_client = Iperf3Client(loop=loop)
    iperf3_client.create_test(test_parameters=params)
    
    loop.call_soon(iperf3_client.run_all_tests)
    loop.run_forever()
    
    iperf3_client.stop_all_tests()
    
    log, buf = get_log()
    print(vm_id)
    print(c_id)
    print(context.memory_limit_in_mb)
    print(event['address'])
    print(event['port'])
    print(cpu_info)
    print(buf)
    
   