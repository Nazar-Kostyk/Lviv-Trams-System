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
