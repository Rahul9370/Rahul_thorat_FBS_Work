"""3. A list contains sublist with Emp information as follows :
Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
[210,”Tannu”,14000],[320,”Suresh”,35000]]"""

def sortSalary(data):
    newlist = []
    for i in range(len(data)):
        for j in range(0,len(data)-i-1):
            if(data[j][2] > data[j+1][2]):
                data[j],data[j+1] = data[j+1],data[j]
    print(data)

data = [[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]
sortSalary(data)