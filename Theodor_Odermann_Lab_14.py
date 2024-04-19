import Theodor_Odermann_Stats

def main():
	attempts = 0
	
	while True:
		print(" ")
		user_input = input("enter file name: ")
		
		try:
			with open(user_input, "r") as file:
				apple_set = []
				straw_set = []
				nana_set = []
				all_set = []
				
				for line in file:
					line = line.strip()
					if "apple" in line:
						new_line = line.split()
						apple_set.append(int(new_line[2]))
					elif "strawberry" in line:
						new_line = line.split()
						straw_set.append(int(new_line[2]))
					elif "banana" in line:
						new_line = line.split()
						nana_set.append(int(new_line[2]))
						
			all_set += apple_set
			all_set += straw_set
			all_set += nana_set
				
			apple_mean = Theodor_Odermann_Stats.Mean(apple_set)
			apple_median = Theodor_Odermann_Stats.Median(apple_set)
				
			straw_mean = Theodor_Odermann_Stats.Mean(straw_set)
			straw_median = Theodor_Odermann_Stats.Median(straw_set)
				
			nana_mean = Theodor_Odermann_Stats.Mean(nana_set)
			nana_median = Theodor_Odermann_Stats.Median(nana_set)
				
			all_mean = Theodor_Odermann_Stats.Mean(all_set)
			all_median = Theodor_Odermann_Stats.Median(all_set)
			
			print(f"file: {user_input} has successfully been processed.")
			print("See output.txt for fruit statistics.")
			
			with open("Output.txt", "w") as result_file:
				result_file.write(f"Apples Mean:{apple_mean: .2f}, Apples Median:{apple_median: .2f}\n")
				result_file.write(f"Bananas Mean:{nana_mean: .2f}, Bananas Median:{nana_median: .2f}\n")
				result_file.write(f"Strawberries Mean:{straw_mean: .2f}, Strawberries Median:{straw_median: .2f}\n")
				result_file.write(f"All Fruit Mean:{all_mean: .2f}, All Fruit Median:{all_median: .2f}\n")
			
			'''	
			print(f"The mean number of apples eaten is {apple_mean: .2f}")
			print(f"The median number of apples eaten is {apple_median: .2f}")
				
			print(f"The mean number of bananas eaten is {nana_mean: .2f}")
			print(f"The median number of bananas eaten is {nana_median: .2f}")
			
			print(f"The mean number of strawberries eaten is {straw_mean: .2f}")
			print(f"The median number of strawberries eaten is {straw_median: .2f}")
			
			print(f"The mean number of all fruit eaten is {all_mean: .2f}")
			print(f"The median number of all fruit eaten is {all_median: .2f}")
			'''
			
			break
			
		except FileNotFoundError:
			choice = input("File not found. Try another file name? (y/n): ")
			if choice.lower() != "y":
				print("No file found. Exiting program.")
				break
				
			
			
		finally:
			attempts += 1
			print(f"number of tries so far: {attempts}")
		
		

if __name__ == "__main__":
	main()
