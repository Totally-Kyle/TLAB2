#Import Statistics Library
import statistics
def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    for heart in range(0, len(data), n):
        rates = data[heart: heart + n]
        maximums.append(max(rates))

    return maximums

    ...


def window_average(data: list, n: int) -> list:
    heart_averages = []
    for x in range (0, len(data), n):
        heart_beats = data[x:x + n]
        averages = sum(heart_beats) / len(heart_beats)
        heart_averages.append(averages)

    return heart_averages
    pass


def window_stddev(data: list, n: int) -> list:
 New_window = []
 for x in range(0,len(data), n):
        window = data[x:x+n]
        if len(window) == 1:
            continue

#calculate standard deviation for the window
        average = sum(window) / len(window)
        variance = sum((x- average)** 2 for x in window) / (len(window) -1)
        stddev = variance ** 0.5
        New_window.append(round(stddev,2))
 return New_window

    
pass
