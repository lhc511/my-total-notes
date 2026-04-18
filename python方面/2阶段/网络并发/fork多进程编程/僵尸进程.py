import os, sys

"""
当子进程先于父进程退出并且父进程不退出就会产生僵尸进程
"""
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:", os.getpid())
    # sys.exit("子进程退出")
    sys.exit(2)
else:
    """处理僵尸进程 os.wait()"""
    pid, status = os.wait()
    print("pid:", pid)
    print("status:", status)  # 子进程退出状态*256
    while True:  # 父进程不退出
        pass
