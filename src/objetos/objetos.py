from copy import copy

def make_time(hour, minute, second):
	return {"hour": hour, "minute": minute, "second": second}

start = make_time(9,20,0)

end = copy(start)

print(start)
print(end)
print(start is end)
print(start == end)