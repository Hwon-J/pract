def solution(fees, records):
    answer = []
    total_time = {}
    car_in = {}
    
    for record in records:
        time, number, in_out = record.split()
        if number not in car_in:
            car_in[number] = []
        car_in[number].append(time)

    for number, in_time in car_in.items():
        if len(in_time) % 2 == 1:
            in_time.append("23:59")
        total_time[number] = 0
        for i in range(0, len(in_time), 2):
            in_hour, in_minute = map(int, in_time[i].split(":"))
            out_hour, out_minute = map(int, in_time[i + 1].split(":"))
            total_time[number] += (out_hour - in_hour) * 60 + (out_minute - in_minute)

    base_time, base_fee, per_time, per_fee = fees
    for number, parking_time in sorted(total_time.items()):
        if parking_time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + ((parking_time - base_time) // per_time + ((parking_time - base_time) % per_time > 0)) * per_fee
        answer.append(fee)
    
    return answer
