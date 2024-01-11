def map_value(value, range_min, range_max, m=1, c=0, dividend=1, divisor=1):
    # Ensure the value is within the specified range
    value = max(min(value, range_max), range_min)

    # Map the value based on the specified parameters
    mapped_value = (value * m + c) * dividend / divisor

    return mapped_value

def read_config_file(file_path):
    mappings = {}
    current_mac = None

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            # Check if the line contains a MAC address
            if ':' in line:
                current_mac = line
                mappings[current_mac] = {'range_1': {}, 'range_2': {}}
            else:
                parts = line.split()
                if parts and len(parts) >= 1:  # Check if the line has enough parts
                    range_name = parts[1]
                    range_min = int(parts[4])
                    range_max = int(parts[7])

                    if range_name == 'rpm_range_1':
                        mappings[current_mac]['range_1']['min'] = range_min
                        mappings[current_mac]['range_1']['max'] = range_max
                        mappings[current_mac]['range_1']['m'] = int(parts[10])
                        mappings[current_mac]['range_1']['c'] = int(parts[13])
                    elif range_name == 'rpm_range_2':
                        mappings[current_mac]['range_2']['min'] = range_min
                        mappings[current_mac]['range_2']['max'] = range_max
                        mappings[current_mac]['range_2']['dividend'] = int(parts[10])
                        mappings[current_mac]['range_2']['divisor'] = int(parts[13])
                        mappings[current_mac]['range_2']['c'] = int(parts[16])
                else:
                    print(f"Warning: Unexpected line format - {line}")
    print('####################', mappings)
    return mappings


def main():
    file_path = 'your_config_file.txt'  # Replace with your actual file path
    mac_address_to_check = 'AB:CD:EF:12:34:56'  # Replace with the MAC address you want to check

    # Read the configuration file
    mappings = read_config_file(file_path)

    # Check if the MAC address is in the mappings
    if mac_address_to_check in mappings:
        ranges_1 = mappings[mac_address_to_check]['range_1']
        ranges_2 = mappings[mac_address_to_check]['range_2']

        # Example: Map a value to ranges 1 and 2
        value_to_map = 800  # Replace with the actual value you want to map

        mapped_value_range_1 = map_value(value_to_map, ranges_1['min'], ranges_1['max'], ranges_1['m'], ranges_1['c'])
        mapped_value_range_2 = map_value(value_to_map, ranges_2['min'], ranges_2['max'], ranges_2['dividend'], ranges_2['divisor'], ranges_2['c'])

        print(f"Mapped Value (Range 1): {mapped_value_range_1}")
        print(f"Mapped Value (Range 2): {mapped_value_range_2}")
    else:
        print(f"MAC address {mac_address_to_check} not found in the mappings.")

if __name__ == "__main__":
    main()
