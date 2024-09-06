from datetime import datetime

def photobox_file_to_dictionary(filename) -> dict:
    file = open(filename).read().split("\n")
    output = {}
    for line in file:
        key, value = line.split(", ")
        value = datetime.fromisoformat(value)
        output[key] = value
    return output

def list_speeders(filename_a: str, filename_b: str, speed_limit_kph=60, distance_km=5) -> dict:
    d1 = photobox_file_to_dictionary(filename_a)
    d2 = photobox_file_to_dictionary(filename_b)
    speeders = {}
    for key in d1:
        if key not in d2:
            continue
        
        passed_box1_datetime = d1[key]
        passed_box2_datetime = d2[key]
        difference = passed_box2_datetime - passed_box1_datetime
        average_speed_kph = distance_km / (difference.seconds / 3600)
        if average_speed_kph > speed_limit_kph * 1.05:
            speeders[key] = (average_speed_kph, passed_box1_datetime)
    return speeders


if __name__ == "__main__":
    BOX_A = "photobox/box_a.txt"
    BOX_B = "photobox/box_b.txt"
    speeders = list_speeders(BOX_A, BOX_B, 60, 5)
    for key in speeders:
        avg_speed, time = speeders[key]
        print(key, "\t", f"speed: {avg_speed:.3f}  ", "time:", str(time))