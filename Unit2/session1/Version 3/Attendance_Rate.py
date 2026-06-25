def attendance_rate(attendance_list):
	present = 0
	absent = 0
	for key in attendance_list:
		if attendance_list[key] == "Present":
			present += 1
	return present / len(attendance_list) * 100

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}

print(attendance_rate(attendance_list))