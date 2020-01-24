# create a mapping of state to abbreviation 创建状态到缩写的映射
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# create a basic set of states and some cities in them  创建一组基本的州和其中的一些城市
cities = {
    'CA':'Sam Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

# add some more cities  添加一些城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 打印一些城市
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by suing hte state then cities dict 根据州找到城市
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation 打印每个周的缩写
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} in abbreviated {abbrev}")

# print every city in state 打印每个州的缩写
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time 州名和缩写名同时打印
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state in abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there   按可能不存在的州安全地获取缩写
state = states.get("Texas") 

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")