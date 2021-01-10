import re
from collections import Counter 

def max_occurred_world(strs):
    world_dict = {}
    words = re.split(' |, |\*|\n ',strs.lower())

    for i in words:
        if i not in world_dict:
            world_dict[i] = 1
        else:
            world_dict[i] += 1

    max_key = max(world_dict.values())
    lst_max = [k for k,v in world_dict.items() if v == max_key]
    print(lst_max)
    return lst_max[0]




if __name__ == "__main__":
    str_1 = 'Once upon a time, there was a brave princess who...'
    str_2 = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
    str_3 = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
    
    print(max_occurred_world(str_1))
    print(max_occurred_world(str_2))
    print(max_occurred_world(str_3))

    