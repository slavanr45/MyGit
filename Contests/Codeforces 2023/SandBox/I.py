import heapq

_, num_task = map(int, input().split())
server_free = [(cpu, 0) for cpu in map(int, input().split())]
server_busy = []
heapq.heapify(server_free)  # создаём кучу
heapq.heapify(server_busy)
total_energy = 0
tasks = ((map(int, input().split())) for _ in range(num_task))

for time, cur_task in tasks:
    while server_busy and time >= server_busy[0][0]:  # проверяем кучу busy cpu на предмет освободившихся
        heapq.heappush(server_free, (heapq.heappop(server_busy)[1], 0))

    if server_free:  # если задание пришло и есть свободные cpu, то перекидываем из в busy кучу
        total_energy += server_free[0][0] * cur_task
        heapq.heappush(server_busy, (time + cur_task, heapq.heappop(server_free)[0]))

print(total_energy)