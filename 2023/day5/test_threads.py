from parallelbar import progress_imap, progress_map, progress_imapu
from parallelbar.tools import cpu_bench, fibonacci


# tasks = range(10000)
# if __name__=='__main__':
#     progress_map(cpu_bench, tasks)

if __name__=='__main__':
    tasks = [20 + i for i in range(15)]
    result = progress_imap(fibonacci, tasks, chunk_size=1, core_progress=False)









# from parallelbar import progress_map
# from math import radians, sin, cos

# # toys example of computationally expensive function 
# def cpu_bench(number):
#     product = 1.0
#     for elem in range(number):
#         angle = radians(elem)
#         product *= sin(angle)**2 + cos(angle)**2
#     return product

# if __name__=='__main__':
#     tasks = [1000000 + i for i in range(100)]
#     result = progress_map(cpu_bench, tasks, n_cpu=4, chunk_size=1, core_progress=True)