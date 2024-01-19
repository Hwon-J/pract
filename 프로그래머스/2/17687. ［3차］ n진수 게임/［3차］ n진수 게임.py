def solution(n, t, m, p):
    m_chars = '0123456789ABCDEF'

    def _rep(numb, to):
        j, k = divmod(numb, to)
        i = m_chars[k]
        return ('' if j == 0 else _rep(j, to)) + i

    numbers = ''
    for i in range(0, t * m):
        numbers += _rep(i, n)
        if len(numbers) >= t * m:
            break

    result = ''
    for i in range(p - 1, t * m, m):
        result += numbers[i]

    return result