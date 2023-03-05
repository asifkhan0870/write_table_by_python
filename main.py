

for i in range(2,21):

    with open(f"tables/table-{i}.txt",'w') as f:

        f.write(f"The Table of {i} is:  ")

        for j in range(1,11):

            f.write(f"{i}X{j}={i*j}\n")
     

    
