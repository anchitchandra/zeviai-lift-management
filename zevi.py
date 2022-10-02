# taking input for no. of lifts and floor
no_lifts = int(input("Lifts  : "))
no_floors = int(input("Floors : "))

# state of lift
state = ["CLOSE", "OPEN"]

# storing each lists location and destination ex : {1: [0,3], ...}
hash_dict = {}
for i in range(1, no_lifts+1):
    lifts = list(map(int, input(f"Lift {i} starting,destination ex = 0,5 : ").split(",")))
    hash_dict[i] = lifts

# calculation of time, mainatining state, tracing floors 
hash_time_dict = {}
for i in hash_dict.keys():
    time = 0
    floor = 0
    if i not in hash_time_dict:
        hash_time_dict[i] = []

    hash_dict[i].insert(0, 0)
    for j in range(len(hash_dict[i]) - 1):
        if hash_dict[i][j] < hash_dict[i][j+1]:
            for f in range(hash_dict[i][j] , hash_dict[i][j+1] + 1):
                if hash_dict[i][j+1] == f and hash_dict[i].index(hash_dict[i][j+1]) != 0:
                    state_index = 1
                    hash_time_dict[i].append([time, f,state[state_index]])
                    time += 1
                
                state_index = 0
                hash_time_dict[i].append([time, f,state[state_index]])
                time += 1
               
        else:
            if hash_dict[i][j]-1 == hash_dict[i][j+1]-1:
                state_index = 1
                hash_time_dict[i].append([time, 0, state[state_index]])
                time += 1
            for f in range(hash_dict[i][j]-1 , hash_dict[i][j+1]-1 , -1):
                if hash_dict[i][j+1] == (f) and hash_dict[i][1:].index(hash_dict[i][j+1]) != 0:
                    state_index = 1
                    hash_time_dict[i].append([time, f, state[state_index]])
                    time += 1
                
                state_index = 0
                hash_time_dict[i].append([time, f, state[state_index]])
                time += 1
        

# final hsitory display 
print("# moniter values activity/unit......")
for i in hash_time_dict.keys():
    print(f"# Lift {i} history + total time taken {len(hash_time_dict[i])}")
    for vals in hash_time_dict[i]:
        print(f"# Time - {vals[0]} | Floor - {vals[1]} | State - {vals[2]}")
