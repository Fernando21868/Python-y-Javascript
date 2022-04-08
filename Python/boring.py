import time

print('Press ENTER to begin. Afterward, press ENTER to "click the stopwatch.". Press Ctrl-C to quit.')
input()
start_time = time.time()
last_time = start_time
lap_num = 1

# TODO: Start tricking the lap times.

try:
    while True:
        input()
        lap_time = round(time.time()-last_time, 2)
        total_time = round(time.time()-start_time, 2)
        print(f'Lap {lap_num}: {total_time} ({lap_time})', end='')
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone')
