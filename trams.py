import os

# To store information about tram in system
class Tram:
    def __init__(self, name, forward, backward):
        self.name = name
        self.forward = forward
        self.backward = backward
        self.all = set(forward + backward)

    def print_tram(self):
        print(f'--- Tram №{self.name} ---')
        print(f'Forward ({len(self.forward)}):')
        for f in self.forward:
            print("\t", f)
        print()
        print(f'Backward ({len(self.backward)}):')
        for b in self.backward:
            print("\t", b)
        print()
        print(f'All stations ({len(self.all)}):')
        for a in self.all:
            print("\t", a)

        print()
        difference = set(self.forward) - set(self.backward)
        print(f'Forward - Backward ({len(difference)}):')
        for d in difference:
            print("\t", d)

        print()
        difference = set(self.backward) - set(self.forward)
        print(f'Backward - Forward ({len(difference)}):')
        for d in difference:
            print("\t", d)
# Read trams from files in data folder
def read_trams():
    trams = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.split('.')[1] == 'txt':
                with open(os.path.join(root, file)) as f:
                    tram_name = file.split('_')[0]
                    forward = []
                    backward = []
                    forward_direction = True
                    for line in f:
                        if("Зворотний" in line):
                            forward_direction = False
                            continue
                        if forward_direction:
                            forward.append(line.strip("\n"))
                        else:
                            backward.append(line.strip("\n"))

                    trams.append(Tram(tram_name, forward, backward))

    return trams

# Find direct route between start_stop and end_stop
# If not found return None
def direct_tram_route_between_stops(start_stop, end_stop, trams):
    for tram in trams:
        # find if start_stop and end_stop are present in a forward list
        if start_stop in tram.forward and end_stop in tram.forward:
            # check if start_stop is before end_stop
            if tram.forward.index(start_stop) < tram.forward.index(end_stop):
                result_dict = {}
                result_dict["start_stop"] = start_stop
                result_dict["tram_name"] = tram.name
                result_dict["tram_stops"] = tram.forward
                result_dict["end_stop"] = end_stop
                return result_dict

        # find if start_stop and end_stop are present in a backward list
        if start_stop in tram.backward and end_stop in tram.backward:
            # check if start_stop is before end_stop
            if tram.backward.index(start_stop) < tram.backward.index(end_stop):
                result_dict = {}
                result_dict["start_stop"] = start_stop
                result_dict["tram_name"] = tram.name
                result_dict["tram_stops"] = tram.backward
                result_dict["end_stop"] = end_stop
                return result_dict

    return None

# Print result of the function direct_tram_route_between_stops()
def print_for_direct_tram(dict):
    result = 'Tram №' + dict["tram_name"] + f' [{dict["tram_stops"][-1]}]' + '\n'
    result += f'Start from {dict["start_stop"]} '
    start_stop_index = dict["tram_stops"].index(dict["start_stop"])
    end_stop_index = dict["tram_stops"].index(dict["end_stop"])
    number_of_stops = end_stop_index - start_stop_index
    result += f'drive {number_of_stops} stops and get of on {dict["end_stop"]}'
    print(result)

# Find if there is a tram route with hop off
def need_change_tram_route(start_stop, end_stop, trams):
    for tram in trams:
        if start_stop in tram.all:
            if start_stop in tram.forward:
                start_stop_index = tram.forward.index(start_stop)
                possible_change_stops = tram.forward[start_stop_index+1:len(tram.forward)]
                result_dict = change_route_success(start_stop, end_stop, tram, "forward", possible_change_stops, trams)
                if result_dict:
                    return result_dict

            if start_stop in tram.backward:
                start_stop_index = tram.backward.index(start_stop)
                possible_change_stops = tram.backward[start_stop_index+1:len(tram.backward)]
                result_dict = change_route_success(start_stop, end_stop, tram, "backward", possible_change_stops, trams)
                if result_dict:
                    return result_dict

    return None

# Help function for need_change_tram_route()
# Check if it is possible to drive to end_stop after changing tram
def change_route_success(start_stop, end_stop, tram, start_tram_direction, possible_change_stops, trams):
    for possible_change_tram in trams:
        if tram.name != possible_change_tram.name:
            change_stops = set(possible_change_stops) & possible_change_tram.all
            if change_stops:
                change_stops_list = list(change_stops)
                for change_stop in change_stops_list:
                    if change_stop in possible_change_tram.forward:
                        change_stop_index = possible_change_tram.forward.index(change_stop)
                        remaining_forward_stops = possible_change_tram.forward[change_stop_index+1:len(possible_change_tram.forward)]
                        if end_stop in remaining_forward_stops:
                            result_dict = {}
                            result_dict["start_stop"] = start_stop
                            result_dict["start_tram"] = tram.name
                            if start_tram_direction == "forward":
                                result_dict["start_tram_stops_list"] = tram.forward
                            else:
                                result_dict["start_tram_stops_list"] = tram.backward
                            result_dict["change_stop"] = change_stop
                            result_dict["change_tram"] = possible_change_tram.name
                            result_dict["change_tram_stops_list"] = possible_change_tram.forward
                            result_dict["end_stop"] = end_stop
                            return result_dict
                            # return f"Tram №{tram.name} - Tram №{possible_change_tram.name}"
                    else:
                        continue

                for change_stop in change_stops_list:
                    if change_stop in possible_change_tram.backward:
                        change_stop_index = possible_change_tram.backward.index(change_stop)
                        remaining_backward_stops = possible_change_tram.backward[change_stop_index+1:len(possible_change_tram.backward)]
                        if end_stop in remaining_backward_stops:
                            result_dict = {}
                            result_dict["start_stop"] = start_stop
                            result_dict["start_tram"] = tram.name
                            if start_tram_direction == "forward":
                                result_dict["start_tram_stops_list"] = tram.forward
                            else:
                                result_dict["start_tram_stops_list"] = tram.backward
                            result_dict["change_stop"] = change_stop
                            result_dict["change_tram"] = possible_change_tram.name
                            result_dict["change_tram_stops_list"] = possible_change_tram.backward
                            result_dict["end_stop"] = end_stop
                            return result_dict
                            # return f"Tram №{tram.name} - Tram №{possible_change_tram.name}"
                    else:
                        continue

    return None

# Print result of the function need_change_tram_route()
def print_for_need_change_tram_route(dict):
    output = f'Start from {dict["start_stop"]} - '
    output += f'tram №{dict["start_tram"]} '
    output += f'[{dict["start_tram_stops_list"][-1]}].\n'
    start_stop_index = dict["start_tram_stops_list"].index(dict["start_stop"])
    change_stop_index = dict["start_tram_stops_list"].index(dict["change_stop"])
    number_of_stops = change_stop_index - start_stop_index
    output += f'Drive {number_of_stops} stops and hop off on {dict["change_stop"]}.\n'

    output += f'Change tram to №{dict["change_tram"]} '
    output += f'[{dict["change_tram_stops_list"][-1]}].\n'
    change_stop_index = dict["change_tram_stops_list"].index(dict["change_stop"])
    end_stop_index = dict["change_tram_stops_list"].index(dict["end_stop"])
    number_of_stops = end_stop_index - change_stop_index
    output += f'Drive {number_of_stops} stops and hop off on {dict["end_stop"]}.\n'
    print(output, end="")

def find_route(start_stop, end_stop, trams):
    solution = direct_tram_route_between_stops(start_stop, end_stop, trams)
    if solution:
        print('Direct route')
        print_for_direct_tram(solution)
        return

    res = need_change_tram_route(start_stop, end_stop, trams)
    if res:
        print('Need change tram route')
        print_for_need_change_tram_route(res)
        return

# find trams which have stop X
def trams_have_stop(stop_name, trams):
    res = []
    for tram in trams:
        if stop_name in tram.all:
            res.append(tram.name)

    return res

# check if stop_name is present in trams stops
def stop_in_trams(stop_name, trams):
    for tram in trams:
        if stop_name in tram.all:
            return True

    return False

trams = read_trams()
trams.sort(key=lambda x:x.name)

while (True):
    print("1) find route between start_stop and end_stop")
    print("2) find if there is direct tram between start_stop and end_stop")
    print("3) find trams which has stop X")
    print("4) close program")
    choice = input()
    if (choice == "1"):
        start_stop = input('Enter start stop: ')
        end_stop = input('Enter end stop: ')
        if stop_in_trams(start_stop, trams) and stop_in_trams(end_stop, trams):
            find_route(start_stop, end_stop, trams)
        else:
            if not stop_in_trams(start_stop, trams):
                print(f'{start_stop} is not found in trams.')
            if not stop_in_trams(end_stop, trams):
                print(f'{end_stop} is not found in trams.')
    elif (choice == "2"):
        start_stop = input('Enter start stop: ')
        end_stop = input('Enter end stop: ')
        if stop_in_trams(start_stop, trams) and stop_in_trams(end_stop, trams):
            print(f'Is there a direct route between {start_stop} and {end_stop}?')
            solution = direct_tram_route_between_stops(start_stop, end_stop, trams)
            if solution:
                print('Yes')
                print_for_direct_tram(solution)
            else:
                print('No')
        else:
            if not stop_in_trams(start_stop, trams):
                print(f'{start_stop} is not found in trams.')
            if not stop_in_trams(end_stop, trams):
                print(f'{end_stop} is not found in trams.')
    elif (choice == "3"):
        stop_name = input('Enter stop: ')
        if stop_in_trams(stop_name, trams):
            res = trams_have_stop(stop_name, trams)
            print("Tram № ", end="")
            string = ""
            for r in res[0:len(res)-1]:
                string += r + ', '
            print(string + res[-1])
        else:
            print(f'{stop_name} is not found in trams.')
    elif (choice == "4"):
        print("Goodbye")
        break
    else:
        print("Wrong number entered, try again")
    print()
