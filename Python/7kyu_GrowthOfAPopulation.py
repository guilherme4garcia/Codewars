# In a small town the population is p0 = 1000 at the beginning of a year. 
#The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
#How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

#More generally given parameters:
#p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
#the function nb_year should return n number of entire years needed to get a population greater or equal to p.
#aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)

def nb_year(p0, percent, aug, p):
    
    percent = percent / 100
    years = 0
    
    while p0 < p:
    
        p0 += p0 * percent + aug 
        years += 1

    return years