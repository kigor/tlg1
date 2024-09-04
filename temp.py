

def custom_filter(some_list) -> bool:
    #out = 0
    #for i in some_list:
    #    if(isinstance(i, int)):
    #        if (i % 7 == 0):
    #            out +=i
    #out = sum([(isinstance(i, int) and i % 7 == 0) for i in some_list])
    #out = sum([num for num in some_list if isinstance(num, int) and num % 7 == 0]) #< 83 or False
    #print(out)
    #return out <= 83
    return sum([num for num in some_list if isinstance(num, int) and num % 7 == 0]) < 83 #or False


# some_list = [7, 14, 28, 32, 32, 56]
# print(custom_filter(some_list))
# some_list = [7, 14, 28, 32, 32, '56']
# print(custom_filter(some_list))



anonymous_filter = lambda x: x.lower().count('я') >= 23

print(anonymous_filter('Я - последняя буква в алфавите!'))
print(anonymous_filter('яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!'))