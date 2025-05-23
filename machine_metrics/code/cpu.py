import psutil

def get_cpu_util_percent():
    # Returns the CPU percentage
    util_percent = psutil.cpu_percent(interval=2)
    return util_percent

def get_num_logical_cores():
    # Returns the number of SMTs
    num_logical_cores = psutil.cpu_count()
    return num_logical_cores

def get_num_physical_cores():
    # Returns the number of Physical cores
    num_physical_cores = psutil.cpu_count(logical=False)

    if num_physical_cores == None: #Case : Undetermined
        return -1
    
    return num_physical_cores

def get_cpu_freq():
    # Returns current CPU frequency
    cpu_freq = psutil.cpu_freq()
    return cpu_freq.current

def get_max_freq():
    # Returns the base CPU frequency
    cpu_freq = psutil.cpu_freq()
    return cpu_freq.max

def get_num_processes():
    # Returns the number of procceses running 
    processes = psutil.pids()
    return len(processes)


def get_num_threads():
    # Returns the total number of threads across all processes
    total_threads = sum(p.num_threads() for p in psutil.process_iter(['pid', 'name']))
    return total_threads