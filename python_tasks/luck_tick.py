def luck_check(string):
    if string.isdigit():
        ticket = list(map(int, string))
        half_t = len(ticket) // 2
        if len(ticket) % 2 != 0:
            ticket.pop(half_t // 2)
        return sum(ticket[:half_t]) == sum(ticket[half_t:])
    else:
        return False