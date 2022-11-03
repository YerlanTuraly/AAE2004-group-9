T = 77.7 #Total Time

#A321neo
F320 = 54 #Fuel Consumption
P320 = 200 #Passenger capacity
TL320 = 10 #Cost time Low
TM320 = 15 #Cost time Medium 
TH320 = 20 #Cost time High
CA320 = 1800 #Fixed Cost

#A330-900neo
F330 = 84 #Fuel Consumption
P330 = 300 #Passenger capacity
TL330 = 15 #Cost time Low
TM330 = 21 #Cost time Medium 
TH330 = 27 #Cost time High
CA330 = 2000 #Fixed Cost

#A350-900
F350 = 90 #Fuel Consumption
P350 = 350 #Passenger capacity
TL350 = 20 #Cost time Low
TM350 = 27 #Cost time Medium 
TH350 = 34 #Cost time High
CA350 = 2500 #Fixed Cost

class Scenario1:
  #Scenario 1
  print("Scenario 1")
  TP1 = 3000 #Total passengers per week
  MF1 = 12 # Maximum number of flights per week
  CF1 = 0.76 #Cost fuel 


  N1320 = TP1 / P320 #number of flights capable, maximum 12
  print(N1320)
  
  Total_cost_1A320 = (T * F320 * CF1 + T * TM320 +CA320) * (TP1 / P320 - (TP1 / P320 - 12))
  print(Total_cost_1A320)


  N1330 = TP1 / P330 #number of flights capable, maximum 12
  print(N1330)

  Total_cost_1A330 = (T * F330 * CF1 + T * TM330 +CA330) * 10
  print(Total_cost_1A330)


  N1350 = TP1 / P350 #number of flights capable, maximum 12
  print(N1350)

  Total_cost_1A350 = (T * F350 * CF1 + T * TM350 +CA350) * 9
  print(Total_cost_1A350)


class Scneario2:
  #Scenario 2
  print("Scenario 2")
  TP2 = 1250 #Total passengers per week
  MF2 = 5 # Maximum number of flights per week
  CF2 = 0.88 #Cost fuel 
  

  N2_320 = TP2 / P320 #number of flights capable, maximum 20 per month
  print(N2_320)

  Total_A320 = (T * F320 * CF2 + T * TH320 +CA320) * 7
  print(Total_A320)


  N2_330 = TP2 / P330 #number of flights capable, maximum 20 per month
  print(N2_330)

  Total_A330 = (T * F330 * CF2 + T * TH330 +CA330) * 5
  print(Total_A330)


  N2_350 = TP2 / P350 #number of flights capable, maximum 20 per month
  print(N2_350)

  Total_A350 = (T * F350 * CF2 + T * TH350 +CA350) * 4
  print(Total_A350)



