def formatMsg(msg):
    return f"input was: {msg}"

def dict_to_text(**kwargs):
    out_txt = []
    for key in kwargs.keys():
        out_txt.append(f"{key} : {kwargs[key]}")
    out_txt = "\n".join(out_txt)
    return out_txt



out_txt = dict_to_text(a=1,b=2)
print(out_txt)

out_txt = formatMsg("hello")
print(out_txt)



def save_output(func):
    def inner(*args, **kwargs):
        out = func(*args, **kwargs)
        with open("out.txt", 'a') as file:
            file.write(out + "\n")
        return out
    return inner


@save_output
def formatMsg(msg):
    return f"input was: {msg}"

@save_output
def dict_to_text(**kwargs):
    out_txt = []
    for key in kwargs.keys():
        out_txt.append(f"{key} : {kwargs[key]}")
    out_txt = "\n".join(out_txt)
    return out_txt

out_txt = dict_to_text(a=1,b=2)
print(out_txt)

out_txt = formatMsg("hello")
print(out_txt)

def save_output2(loc):
    def middle(func):
        def inner(*args, **kwargs):

            out = func(*args, **kwargs)
            import os
            if not os.path.exists(loc):
                os.mkdir(loc)
            path = os.path.join(loc, "out.txt")
            with open(path, 'a') as file:
                file.write(out + "\n")
            return out
        return inner
    return middle

@save_output2("./home")
def formatMsg(msg):
    return f"input was: {msg}"

@save_output2("./logs")
def dict_to_text(**kwargs):
    out_txt = []
    for key in kwargs.keys():
        out_txt.append(f"{key} : {kwargs[key]}")
    out_txt = "\n".join(out_txt)
    return out_txt

out_txt = dict_to_text(a=1,b=2)
print(out_txt)

out_txt = formatMsg("hello")
print(out_txt)


import time

def timeit(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        out = func(*args, **kwargs)
        print(f"elapsed time: {time.time() - start_time}")
        return out
    return inner


@timeit
def formatMsg(msg):
    return f"input was: {msg}"

@timeit
def long_loop(n : int):
    out = 0
    for i in range(n):
        for j in range(n):
            out += i*j




out_txt = formatMsg("hello")
print(out_txt)


out_int = long_loop(1000)

