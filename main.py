# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    processing = [0] * n 

    for i in range(m):
        min_thread_time = float('inf')
        min_thread_index = None
        for j in range(n):
            if processing[j] + data[i] < min_thread_time:
                min_thread_time = processing[j] + data[i]
                min_thread_index = j
        output.append((min_thread_index, processing[min_thread_index]))
        processing[min_thread_index] += data[i]

    return output

def main():
   n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for pair in result:
        print(pair[0], pair[1])
        
if __name__ == "__main__":
    main()
