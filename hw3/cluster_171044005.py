
def most_profitable(regions, profits ):
    max = profits[0]
    cluster=[regions[0]]
    for i in range(0,len(regions)):
            for j in range(i,len(regions)):
                profit=sum(profits[i:j])
                if(max<profit):
                    max= profit
                    cluster=regions[i:j]
    return cluster       
    
regions=['a','b','c','d','e','f','g']
profits=[3,-5,2,11,-8,9,-5]

print(most_profitable(regions,profits))