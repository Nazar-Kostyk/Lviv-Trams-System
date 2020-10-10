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
