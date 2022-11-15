# Project Name : AAE Github Project

# Group Number 9 

# Built With 

>
**Leader:** 
Yerlan - "captainnccrruunncchh"

**Member 2:** 
Namnet - "NamnetT"

**Member 3:** 
Hang - "Mr. Truth"

**Member 4:**
Frederick - "FrederickTam22"

**Member 5:**
Jophy - "JophyTse"

**Member 6:**
Tim - "Timtsangxd"

**Member 7:**
Boey - "boeytse"


## Content

* [About The Project](#about-the-project)
* [YouTube Video](#YouTube-Video)
* [Task 1](#task-1)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Usage](#Usage)
* [Reflections](#Reflections)
* [Contacts](#contacts)
* [Project Status](#project-status)


## About the project

As efficiency in cost and passanger satisfaction are a crucial factor that determines the sucess of airlines. This project is primarily focused on finding the most an efficeint pathway for a flight under various realworld circumstances using technologies and methods that are easily acessible.



## YouTube Video


## Task 1
**Goal**: To find an appropriate aircraft model that can achieve minimum cost for each given scenario. 

This is the most efficent flight plan that our group has formulated.
![gifv2](https://user-images.githubusercontent.com/116061877/200487324-6ef257dd-fb34-4669-9df2-e9cdba3829ab.gif)

**Coding**:

### Senario 1

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objective**: To transport 3000 passengers within a week from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 12 flights. The time cost should also be moderate, and the cost of fuel should be $0.76 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $85894.42 and $89186.64 per trip, respectively. Therefore, we came to a conclusion that Airbus 330neo would be the best option for the scenario.

![t1](https://user-images.githubusercontent.com/116061877/200476914-79e418d0-d2c1-4277-a744-4918da13b3f3.jpeg)

### Senario 2

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objectives**: To transport 1250 passengers within this month from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 5.The time cost should be high, and the cost of fuel should be $0.88 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $49191.80 and $45168.54 per trip, respectively. Therefore, we came to a conclusion that Airbus 350neo would be the best option for the scenario.

![Scenrio 2](https://user-images.githubusercontent.com/116084608/200457503-f5a6cb2a-30f1-4fdb-aca1-a79115e0227c.jpg)


### Senario 3

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objectives**: To transport 2500 passengers within this week from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 25.The time cost should be low, and the cost of fuel should be $0.95 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $84267.23 and $85552.68 per trip, respectively. Therefore, we came to a conclusion that Airbus 330neo would be the best option for the scenario.

![t3](https://user-images.githubusercontent.com/116061877/200477263-8196e13e-60e9-4c3b-8210-56d93b83a78c.jpeg)

<p align="right">(<a href="#readme">back to top</a>)</p>

## Task 2
**Goal**: To design a new cost area that can reduce the cost of the route.

**Background**: There are certain areas called jet-streams where aircraft could consume relatively less fuel. Jet streams are formed when warm air masses meet cold air masses in the atmosphere. Although, flying with the jet-stream would be quicker and more fuel-efficient. However if the aircraft arrives too early, circling on a holding patter over the airspace is not ideal. In contrast, if the jet stream is weak, flying against it would need more fuel and slow the aircraft down, perhaps resulting in delays. In this task we will aim to create a scenario where we can use the jet stream to our advantage in-order better grasp the concept of flight planning.

**Methodology**: Taking the scenario from [Task 1](#task-1) as a background, we had to find the best place to set the jet stream where the cost of the flight is reduced by 5%. The recommended parameters are that the jet stream region stretch across the map laterally and span 5-units vertically.


**Results**: 

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/116061877/200550990-c1e6800d-d076-4813-be21-ff3ba1aaaa21.gif)

**Coding**:

<p align="right">(<a href="#readme">back to top</a>)</p>


## Task 3
**Goal**: To design a new aircraft model that achives minimum costs for the specific scenarios in [Task1](#task-1).

**Trend**: According to the fuel price analysis, the fuel cost in 2022 had increased a total of 73.7% compared to 2021 which indicated that jumbo jets like B747 or A380 should not be considered in this task.

**Results**: The aircraft B797 using twin RR Trent 1000 engine is the best fit for scenario 1 in task 1 as this aircraft is able to meet the cost specification between A321 & A330. The targetted no of flights is 11 with 273 passengers per flight.


A potential design for the aircraft

![b797-main](https://user-images.githubusercontent.com/116061877/201460210-70e0f01d-554d-414a-a875-baadc2b19493.jpg)


**Calculation**: Refering to to the formula Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>, We have found that the total cost approximates to $69375.13 which is much lower than the cost for an A330neo. Meanwhile, the capacity of newly designed aircraft, B797, is 273 passengers. Allowing us to exploit twin-engine aircraft, flying 11 flights weekly. 

![Task 3](https://user-images.githubusercontent.com/116084608/201460707-bde85a28-0aa7-467f-ab65-3ceca6e30986.jpg)


**Reasons Behind**: By comparing other existing aircraft which may be possible candidates for this role such as the A321, A330, A340, A350 and the B787. We determined that an aircraft with a moderate seating capacity and twin-engine layout would be the most efficient. As such we designed our aircraft to have a capacity between the A330-200 (250 seats) and the b787-9 (296 seats), so our group initially assumed that an aircraft with a 275-seating capacity will expend the lowest possible cost. A twin-engine design was favoured due to examing the efficency of the A340 and A350, one had an inefficient quad engine layout whiles the other had a very efficent twin engine layout which help boost its overall appeal. As such it was an easy decision on which engine configuration to choose. To solidify our assumption, our group has written a code that calculates whether we need a twin-engine or 4-engine aircrfat with its capacity and operational cost. Hence we have designed our aircraft the B797 to follow our setout guidelines and to comply with the guidelines of the task.

**Coding**:

<p align="right">(<a href="#readme">back to top</a>)</p>


## Usage 


<p align="right">(<a href="#readme-top">back to top</a name>)</p>

## Reflections
**Yerlan's Reflection:**


**Namnet's Reflection:** 


**Hang's Reflection:** 


**Frederick's Reflection:** 


**Jophy's Reflection:** 


**Tim's Reflection:** 


**Boey's Reflection:** 

<p align="right">(<a href="#readme">back to top</a>)</p>

## Contacts
**Yerlan** - https://www.linkedin.com/in/yerlan-turaly-5b2310246/ - 22096542d@connect.polyu.hk

**Namnet** - 22031071d@connect.polyu.hk

**Hang** - 

**Frederick** - pts031022@gmail.com

**Jophy** - jhtse72@gmail.com

**Tim** - timmttsang@yahoo.com.hk

**Boey** -boeytse0822@gmail.com

**Project Link** - https://github.com/captainnccrruunncchh/AAE2004-group-9

<p align="right">(<a href="#readme">back to top</a>)</p>

## Project Status
Project is in progress. Compulsory coding tasks are done, ReadMe and ppt are in progress

<p align="right">(<a href="#readme">back to top</a>)</p>
