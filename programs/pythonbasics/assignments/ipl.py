ipl={'name':['Virat Kohli','Rahul','Bumrah','Bhuvaneshwar'],
     'team':['RCB','KXIP','MI','SRH'],
     'runs':[925,800,0,44],
     'wickets':[0,0,15,12]}

players = ipl['name']
runs = ipl['runs']
wickets = ipl['wickets']
maxruns = max(runs)
maxwickets = max(wickets)
indexmaxruns = runs.index(maxruns)
indexmaxwickets = wickets.index(maxwickets)
topscorer = players[indexmaxruns]
topwicketsgetter = players[indexmaxwickets]
print (topscorer, 'is the top scorer with ',maxruns, ' runs ')
print (topwicketsgetter, 'is the top bowler with ',maxwickets, ' wickets ')
