import pandas

dataset = {

    "owners": ["Noor","Kashif","Naimuddin"] ,

    "cars": ["Fortuner","Audi","Scorpio"]
    

}

my_var = pandas.DataFrame(dataset)

print(dir(pandas))

print(my_var)