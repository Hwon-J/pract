def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        tm = phone_book[i]
        if phone_book[i+1][:len(tm)]==tm:
            answer = False
            break
    return answer