members = ["민수", "철수", "영희", "민철"]
ages = [30, 32, 31, 29]
years = [1, 3, 5, 4]

for member, age, year in zip(members, ages, years):
	print(f"{member}: 나이 {age} 구력 {year}년")
