import math
def mean(data_list):
    x = 0
    for i in data_list:
        x = x + i
    return (x/len(data_list))


def SSD(data_list):
    x = 0
    u = mean(data_list)
    for i in data_list:
        x = x + math.pow((i - u),2)

    return math.sqrt(x / (len(data_list) - 1))

def Variance(data_list):
    x = 0
    u = mean(data_list)
    for i in data_list:
        x = x + math.pow((i - u),2)

    return (x / (len(data_list) - 1))


def PSD(data_list):
    x = 0
    u = mean(data_list)
    for i in data_list:
        x = x + math.pow((i - u),2)

    return math.sqrt(x / (len(data_list)))

def median(data_list):
    data_list = sorted(data_list)
    renge = len(data_list)
    m = (renge + 1)/2
    if renge  % 2 == 1:
        return data_list[int(m)-1]
    else:
        upper = (data_list[math.ceil(m)-1])
        lower = (data_list[math.floor(m)-1])
        return ((upper + lower)/2)


if __name__ == "__main__":
    a = [1.75,1.92,2.62,2.35,3.09,3.15,2.53,1.91]
    b = [79,100,74,83,81,85,82,80,84]
    c = [79,74,83,81,85,82,80,84]
    print(mean(c))
    print(Variance(b))
    print(SSD(b))