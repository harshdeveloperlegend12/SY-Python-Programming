print("Enter runs scored in 5 matches:")
runs_list = []
for i in range(6):
 scores=int(input("Enter the runs of 5 matches: "))
 runs_list.append(scores) 

highest_score = max(runs_list)

print("\nThe highest score in the 5 matches is: ",highest_score)
