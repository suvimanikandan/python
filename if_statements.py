is_male=True
is_tall=False

#is_male=False

#if is_male or is_tall:
if is_male and is_tall:
    print("You are a Male or a tall or both")

elif is_male and not(is_tall):
    print("you're are a short male")

elif not (is_male) and not is_tall:
    print("you're are a not a male but tall")

else:
    #print("you neither  Male nor tall")
 print("you  are either  not Male not tall")