# try
# except
# else
# finally
# ^^this is the order of exception code, error prone code goes in try
# can add multiple excepts and define expected errors
# else block runs if no exceptions caught
# finally block runs independent of except or else blocks executing
try:
    file = open("e_missing.txt", 'r')
    sample = {"one equals" : "two"}
    print(sample["three"])

except FileNotFoundError:
    file = open("e_missing.txt", 'a')
    file.write("Something here")

except KeyError as theError:
    print(f"The key {theError} does not exist. ")

else:
    contents = file.read()
    print(contents)

finally:
    file.close()
    print("It's good practice and safer to close files.")
    #raise FileExistsError
    #the raise keyword will let you flag errors manually, with accompanying message like below

height = float(input("Height: "))
weight = int(input("Weight: "))

if height>3:
    raise ValueError("Height for humans should not exceed 3 meters.")

bmi = weight/height **2