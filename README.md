# Project Name : AAE Github Project

# Group Number 9 

## Members

**Leader:** 
Yerlan - "YerlanTuraly"

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
* [Project Video](#Project-Video)
* [Task 1](#task-1)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Additional Task 2](#additional-task-2)
* [Additional Task 3](#additional-task-3)
* [Usage](#Usage)
* [Reflections](#Reflections)
* [Contacts](#contacts)
* [Project Status](#project-status)


## About the project

As efficiency in cost and passanger satisfaction are a crucial factor that determines the success of an airline. But, getting from point A to Point B is not as simple as flying the passengers and cargo from destination A to destination B in a safe and timely manner. The airspace which is basically the vast span of sky that we see whenever we look overhead is claimed by countries that reside below the patch of sky as their territory, which often extends around FL600. Therefore, entering an airspace without prior authorization would be a violation of the respective nation's sovereignty. Fortunately, we have the Five Freedom of Air that facilitates the aviation industry, but the airlines have to pay for the charges of flying into foreign airspace. Additionally, there are various physical barriers such as high terrain like hills and mountains, area with critically bad weather, even high-rise skyscrapers that can limit the mobility of the path that an aircraft can take during takeoff and landing. This project is primarily focused on finding the best efficent pathway for a flight under various real-world circumstances using technologies and methods that are easily accessible. 


## Project Video

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/oVIgmGrZtqs/0.jpg)](https://www.youtube.com/watch?v=oVIgmGrZtqs)

We have included only compulsory tasks in our presentation even if additional tasks are done. As those tasks are mandatory, while additional tasks are only optional. It is a reason, why we have decided to exclude additional tasks from our presentation, but you can check the information and resutls of those tasks in our readme reflection!

## Task 1
**Goal**: To find an appropriate aircraft model that can achieve minimum cost for each given scenario. 

This is the most efficent flight plan that our group has formulated.
![gifv2](https://user-images.githubusercontent.com/116061877/200487324-6ef257dd-fb34-4669-9df2-e9cdba3829ab.gif)

**Coding Section**:

>![IMG-20221115-WA0005](https://user-images.githubusercontent.com/116084608/202359218-bb89ef6b-bb16-41a1-ba1f-50b204c73ea7.jpg)

Those two rows are accountable for the percentage charge of going through these two cost intensive areas, cost and time zones. In each row we can detect C1 and C2 which represents own intensive areas. After the part "self.Delta_C1" we wrote numbers such as 0.2 and 0.4 which represent 20% and 40$ respectively, but in numerical aspect. For example, when the aircraft will fly over time intensive area, every point in it will increase tspent amount of time by 20%; however, if you are eager you to change those charges to another one, you can just replace it here to any other value.  

![IMG-20221115-WA0006](https://user-images.githubusercontent.com/116084608/202359228-77b299ba-fbce-49d8-b555-7ae1da43fe6d.jpg)

Here, starting from row 6 we have added many constants in the code. First of all, the most essential part is time. The code here already calculates the total amount of time that is necessary for the path ("current.cost"), so we just named this value by T, simplifying our future coding formulas. 

As we have 3 different scenarios with 3 different aircrafts, I have written each constant for each aircraft separately, making it more easier to understand and change in the future; here we can note the constant values of A321neo aircraft, where I have added its Fuel consumption, capacity, different cost time, and fixed cost values, which will be used in the formulas presented in the next photo.

![IMG-20221115-WA0007](https://user-images.githubusercontent.com/116084608/202359260-39ebbaa4-ed1a-4e5d-bcdc-d5aaa1b999a7.jpg)

At that point, we already have all vital constant values for our aircraft, so we can start our coding for calculating its cost of operation. 

"N320 = math.ceil(TP / P321)"

This part calculates the total number of flights necessary for A321neo to carry all 3000 passengers in a week. Moreover, I have added "math.ceil" part since we have to round this value. As no aircraft can make a number of 0.5 flight to somew place.

Next row shows us a whole formula that is crucial for calculating the total cost of this type of aircraft. Continuing further, you can notice that next 4 rows contains "if" condition. At that part, the code decides by itself, should it include the cost of operation at the end or it should say that the aircraft is not viable due to the excessed number of flights per week by "if N320 <= 12" part that shows if total number of calculated flights is less or equal to 12 or not.

![IMG-20221115-WA0008](https://user-images.githubusercontent.com/116084608/202359371-031b45c8-a16d-427b-a357-846365976e93.jpg)

This part is the most simple and easy one. Here we just put our coordinates of staring and goal points in both x and y coordinates.

![IMG-20221115-WA0009](https://user-images.githubusercontent.com/116084608/202359400-782e8248-40fb-490f-b277-eb1028a38bf0.jpg)

This code represents the obstacles that do not let aircraft to fly throught them. For example, the second obstacle. As we can note from the gif, there are only 3 additional obstacles in our map, where two of them are lines with a slope. Setting its range from 40 to 50 at x coordinates, we have to put it like shown above "for i in range(40, 50):", continuing it by "ox.append". In "ox.append", we just need to i in bracets, while in "oy.append" we have to input the equation which is obtained. It is a "-2*i +140", where i represents x, -2 is the slope of this line in range of 40 to 50, and +140 as a y-intercept. For getting those values, the slope and intercept. We have to use the basic equation from math, y = kx + b, and create a system that contains 2 unknown values k and b and hence find out them manually.

![IMG-20221115-WA0010](https://user-images.githubusercontent.com/116084608/202359409-980aa882-7285-4b2a-8026-09531fa416da.jpg)

The last part of code that should be mentioned is setting of intensive areas. Let's consider only cost intensive area 1 since they both pretty similar in the code content. The second row, "for i in range(-10, 10)" we have set the coordinates of our time intesinve area  between -10 and 10 of x values. Consequently, the next row "for j in range(20, 40)" we have, also, set coordinates ranging from 20 to 40 in y coordinate terms. Meanwhile, next two rows with "append" content are essential for seting up this area in our final map calculation.


### Scenario 1

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objective**: To transport 3000 passengers within a week from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 12 flights. The time cost should also be moderate, and the cost of fuel should be $0.76 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $85894.42 and $89186.64 per trip, respectively. Therefore, we came to a conclusion that Airbus 330neo would be the best option for the scenario.

![t1](https://user-images.githubusercontent.com/116061877/200476914-79e418d0-d2c1-4277-a744-4918da13b3f3.jpeg)

### Scenario 2

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objectives**: To transport 1250 passengers within this month from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 5.The time cost should be high, and the cost of fuel should be $0.88 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $49191.80 and $45168.54 per trip, respectively. Therefore, we came to a conclusion that Airbus 350neo would be the best option for the scenario.

![Scenario 2](https://user-images.githubusercontent.com/116084608/200457503-f5a6cb2a-30f1-4fdb-aca1-a79115e0227c.jpg)


### Scenario 3

**Methodology**: We first setup our obstacles and cost intensive areas, which represent physical or environmental barriers and areas that should be avoided to maximize performance. Then we used a function where Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>,  where C<sub>F</sub> represents the cost of fuel, ΔF is the fuel required to complete the trip,  T<sub>best</sub> is the most efficient time, C<sub>T</sub> is the time related cost per minute of flight, and C<sub>c</sub> represents the fixed cost independent of time.

**Objectives**: To transport 2500 passengers within this week from the the start point to end point, while adhering to a number of objectives, such as the weekly flight cap of 25.The time cost should be low, and the cost of fuel should be $0.95 per kilogram.

**Results**: The program calculated the time required to fly the proposed flight path. The rest of the calculation was also rechecked using the Cost function (C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>.  and comparing the performance and between two widebody airliners the Airbus 330neo and Airbus350-900 which came out to be approximately $84267.23 and $85552.68 per trip, respectively. Therefore, we came to a conclusion that Airbus 330neo would be the best option for the scenario.

![t3](https://user-images.githubusercontent.com/116061877/200477263-8196e13e-60e9-4c3b-8210-56d93b83a78c.jpeg)

<p align="right">(<a href="#readme">back to top</a>)</p>

## Task 2
**Goal**: To design a new cost area that can reduce the cost of the route.

**Background**: There are certain areas called jet-streams where aircraft will consume relatively less fuel while crusing. Jet streams is a narrow band of fast air circulating near the top of troposphere. They are formed when warm air masses meet cold air masses in the atmosphere. 

![Jetstream](https://user-images.githubusercontent.com/116084608/202598116-c83647e8-f8cb-440f-922f-ac3f7056fa99.jpeg)
(**Image-source**: Lotus Arise. (2020, July 24). Jet Stream UPSC: Geography IAS (Climatology). https://lotusarise.com/jet-stream-upsc/. https://lotusarise.com/jet-stream-upsc/)

Although, flying with the jet-stream would be quicker and more fuel-efficient. However if the aircraft arrives too early, circling on a holding patter over the airspace is not ideal. In contrast, if the jet stream is weak, flying against it would need more fuel and slow the aircraft down, perhaps resulting in delays. In this task we will aim to create a scenario where we can use the jet stream to our advantage in-order better grasp the concept of flight planning.

**Methodology**: Taking the scenario from [Task 1](#task-1) as a background, we had to find the best place to set the jet stream where the cost of the flight is reduced by 5%. The recommended parameters are that the jet stream region stretch across the map laterally and span 5-units vertically.


**Results**: 

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/116061877/200550990-c1e6800d-d076-4813-be21-ff3ba1aaaa21.gif)

![WhatsApp Image 2022-11-22 at 3 00 35 AM](https://user-images.githubusercontent.com/111409650/203145395-0d197ca5-983b-42d7-a4b3-3560fb0f01b0.jpeg)

Here, we can see that by the jet stream area, we can probably save more than a thousand usd by using A350-900 rather than without this jet stream area. A350-900 requires only 88067 usd, while in task1 scenario one it would ask us for 89187 usd for carrying all passengers! Furthemore, A321neo is still not viable for this route.


**Coding part**:

![IMG-20221115-WA0011](https://user-images.githubusercontent.com/116084608/202359542-d97b9104-49c1-48ca-9c13-50e9b718d0ab.jpg)

At this part, we add a new area, a jet stream area. Understanding that aircraft's path will be only between somewhere around 10 and 50(Those values are not exact, but very close), we have managed the x range between 10 and 49. Meanwhile, i is in range -10 till 60, which is probably the whole horizontal range of the map, we have managed the range of j as x and x+5 since the jet stream's size was only 5 points, where x is some unknown for us constant, so code should consider the whole pointed area for the most effective place to suit this stream. 

The last part of coding:

" if x==10:
   lowest = costpath
   bestx = x"

We make coding to start from coordinate x, 10, calculating a new costpath as the lowest one, and making this x as the best coordinate. Continuing, we have added the next part:

"if costpath < lowest:
   lowest = costpath
   bestx = x"
   
Here we just make the programme to calculate all possible values of x and comparing all costpath with each other, for finding the best x value. The new and hence final x value we mention as bestx for our further calculations. 

![IMG-20221115-WA0012](https://user-images.githubusercontent.com/116084608/202359563-2667faf4-3fb6-4e07-82d9-8d3c5f02d860.jpg)

Even if the previous codes probably calculate the best x value and hence the best area for fitting jet stream area, the code itself will not work, since it will take only the first value x, which is 10, and put it in all formulas without consideration of other values. It is why we have to add this part to make it elaborate. At that part, we mention j range from bestx and bestx + 5 that are revealed from previous code, so now it chooses best area for the jet stream basing on the best x value.

![IMG-20221115-WA0013](https://user-images.githubusercontent.com/116084608/202359649-d8b52aa5-c71e-4d18-9b4d-a004f1dabca9.jpg)

Even though, just adding codes will not make programme work since we have not put js_x and js_y with x at the "a_star" and "rx, ry, costapth" content in the code. Without putting them, programme could not proceed all calculations at the output since it has no such command. However, changing this part which is showed in the screenshot, we are making our programme to include jet-stream too in the whole process.

<p align="right">(<a href="#readme">back to top</a>)</p>

## Task 3
**Goal**: To design a new aircraft model that achieves minimum costs for the specific scenarios in [Task1](#task-1).

**Trend**: According to the fuel price analysis, the fuel cost in 2022 had increased a total of 73.7% compared to 2021 which indicated that jumbo jets like B747 or A380 should not be considered in this task.
![image](https://user-images.githubusercontent.com/116059527/202887053-3c2f0643-ecfd-469a-8507-72be0f2ae950.png)

**Results**: The aircraft B797 using twin RR Trent 1000 engine is the best fit for scenario 1 in task 1 as this aircraft is able to meet the cost specification between A321 & A330. The targetted no of flights is 11 with 273 passengers per flight.


A potential design for the aircraft

![b797-main](https://user-images.githubusercontent.com/116061877/201460210-70e0f01d-554d-414a-a875-baadc2b19493.jpg)


**Calculation**: Refering to the formula Cost(C) = C<sub>F</sub>· ΔF · T<sub>best</sub> + C<sub>T</sub> . T<sub>best</sub> +C<sub>c</sub>, We have found that the total cost approximates to $69375.13 which is much lower than the cost for an A330neo. Meanwhile, the capacity of newly designed aircraft, B797, is 273 passengers. Allowing us to exploit twin-engine aircraft, flying 11 flights weekly. Having a table of fuel price, we have noted that bbl was mainly used there, it is why we used this website, "https://www.convertunits.com/from/barrel+%5bUS,+liquid%5d/to/kilo+gram#:~:text=Quick%20conversion%20chart%20of%20barrel%20%5BUS%2C%20liquid%5D%20to,liquid%5D%20to%20kilo%20gram%20%3D%20238.48094%20kilo%20gram", for converting barrels to kilograms for further calculations in coding

![Task 3](https://user-images.githubusercontent.com/116084608/201460707-bde85a28-0aa7-467f-ab65-3ceca6e30986.jpg)


**Reasoning**: By comparing other existing aircraft which may be possible candidates for this role such as the A321, A330, A340, A350 and the B787. We determined that an aircraft with a moderate seating capacity and twin-engine layout would be the most efficient. As such we designed our aircraft to have a capacity between the A330-200 (250 seats) and the b787-9 (296 seats), so our group initially assumed that an aircraft with a 275-seating capacity will expend the lowest possible cost. A twin-engine design was favoured due to examing the efficency of the A340 and A350, one had an inefficient quad engine layout whiles the other had a very efficent twin engine layout which help boost its overall appeal. As such it was an easy decision on which engine configuration to choose. To solidify our assumption, our group has written a code that calculates whether we need a twin-engine or 4-engine aircrfat with its capacity and operational cost. Hence we have designed our aircraft the B797 to follow our setout guidelines and to comply with the guidelines of the task.

**Coding Section**:

![IMG-20221115-WA0014](https://user-images.githubusercontent.com/116084608/202359677-9eea788e-3ec3-43e5-b214-b0bd23ba06b7.jpg)

This part of coding is just a list of constant for future calculations that will be made. Taking scenario 1 from task 1, our newly designed aircraft should carry 3000 passengers in a week, with maximum number of flights of 12. We have, also, input other constants such as CT and CF for both twin and 4 engine aircrafts, but the most vital part is the "usdbbl". Looking at provided table, we have taken a value for Asia and Oceania Region since this region is more actual than others for us. 

![IMG-20221115-WA0015](https://user-images.githubusercontent.com/116084608/202359695-74d42f47-2578-493b-bcd8-8019764de541.jpg)

This part is the most essential for completing Task 3. Firstly, we have written a formula for converting from usd per barrel to cost for fuel in terms of kilograms since further calculations should include exactly kilograms, but not barrels. Next two formulas of "m" and "N" are responsible for adding additional costs for every 50 passengers and  revealing the total number of flights, which will not be changed in further, respectively. Both values are rounded to the next number by code "math.ceil".

Continuing the code, we can note that there are two possible outcomes of Total_cost, where one of them is for twin-engine aircraft, while the second one is for 4-engine and from now, the most interesting part starts:

"if passengers==250:
   lowest = Total_cost
   bestpassengers = passengers"

Here we make the code start to calculate the most cheapest value and the best type of aircraft in terms of engine by itself. Starting from the lowest number of passenegrs, 250, code makes the Total_cost of 250 people as the lowest and bestpassengers, number of passengers that suits much more for our case, as 250.
The second part of the code:

"if Total_cost < lowest:
   lowest = Total_cost
   bestpassengers = passengers"
In this part, we make the code search the most reliable results of both costs and number of passengers by itself by comparing all values and choosing the most effective one. 

![IMG-20221115-WA0016](https://user-images.githubusercontent.com/116084608/202359709-08e7948e-25c2-4de2-9bdf-c02044a4f821.jpg)

This formula is pretty similar with other formulas in task 1 and 2, but here the coding can give either one of the solution which probably describes all information that is needed. Already calculating the best number of passengers, the code proceeds its further calculation of the Total_cost of our new aircraft, by checking in which condition the capacity suits more. The part "if bestpassengers >= 300" makes coding to choose which type of new aircraft we should use to minimize our costs. If a new aircraft's capacity is higher, then coding print name of a new aircraft, the number of engines that it should possess, and the cost that it requires for operation. Moreover, it, also, prints the number of seats that is needed for the aircraft to fulfill requirements. Otherwise, if the number of passengers is lower than 300, as in our case, it swicthes to twin-engine aircraft, showing its passenger capacity and operational cost.  

<p align="right">(<a href="#readme">back to top</a>)</p>

## Additional Task 2
**Goal**: To generate new paths for aircraft in changing conditions and start with end points at each scenario.

**Methodology**: We have to create a code that could be able to generate different conditions with reasonable density with start and goal coordinates at every different cases. Meanwhile, there should be only fuel-consuming area with fixed area 30x30. Moreover, diagonal movement of aricraft should be disabled in this part of task.

**Results**:

![ad2 opt](https://user-images.githubusercontent.com/116061877/203242085-bc0add2a-a12f-40eb-85fb-5b92f3cc6c81.gif)

As we can see here, it is one of the possible maps of randomly generated obstacles with start and goal points. The path planning analysis all possible ways to reach the final destination, bypassing all obtsacles that are black dotes. In addition, in that case fuel-intensive area was generated almost at the centre of our map, making it much harder for the aircraft to find the goal point. Even though this area is placed almost at the centre, programme found that bypassing this zone is better option for us than going through it. Furthemore, the programme was managed that way, so obstacles would be generated with appropriate density, where aircraft would not struggle find the shortest way, but still would have to search one. Running the code that is uploaded above, we can try as many times, as we want, and see at the end that programme continuously generates different and unalike variations of our path. 

<p align="right">(<a href="#readme">back to top</a>)</p>

## Additional Task 3
**Goal**: To test other unalike algorithms for finding the most efficient path.

**Methodology**: We have to choose additional 2 different algorithms from the GitHub platform and compare all 3 codes with outcomes together, with the same obstacle deisgn.

**Result for A***:

![ad3 star](https://user-images.githubusercontent.com/116061877/203325855-2e52a6e9-39b3-47f9-8398-0d1cb574b051.gif)

We can see here that it is normal A* planning outcome, that we used in our compulsory tasks. Comparing with the next two repositories from GitHub, we can clearly notice that A* planning is the fastest programme in terms of time to find the goal point.

**Result for BFS (sped up by x5)**:

![ad3 bnj opt](https://user-images.githubusercontent.com/116061877/203325929-1243684f-df51-4270-b470-de75af62491d.gif)

Certainly, BFS takes much longer time than A* planning, it takes relatively a long amount of time for calculating and finding the final pathway from our star point to the final one. We even speeded up the process by 5 for our github. Nevertheless, if we compare those two programmes, we would like to suggest everyone to use A* path planning since it takes significantly less amount of time.

**Results for Dijkstra (sped up by x3)**:

![ezgif com-gif-maker (15)](https://user-images.githubusercontent.com/116061877/203242548-13ea08f7-16a6-4827-8540-3cfacd3ab60d.gif)

Already seeing 3 different codings' outcomes, we can sum up that the Dijkstra is the code that finds the aircraft's path flight longer than the A* path planning, but significantly faster than BFS, even if Dijkstara was speeded up by 3 times. Even though Dijkstra path finding programme searches a path so long, the BFS takes substantially more time for own calculations and searching for the final path; we even speeded up it by 5 times for making it relaatively faster in our article.
In conclusion, it is crystal clear that A* planning is the best programme that can be and have to be chosen for our tasks. As it reaches the goal point in the shortest possible way. It is why we can conclude that choosing A* path planning was the best decision for our project coding part.

<p align="right">(<a href="#readme">back to top</a>)</p>

## Usage 
The usage of path planning is a key component of the aviation industry. Path planning is achieved through the use of software and machine learning. A machine with the use of code will be able to plot the most efficient path through a map while navigating through objects, special points of interest and zones to avoid. Many airlines around the world rely on such programs to help pinpoint the most efficient role their aircraft should follow. By increasing their aircraft's efficiency airlines would have shortened their travelling times, decreased fuel costs and increased their overall net profit. With the future development of path planning software, the efficiency of air routes will be increased resulting in the positive growth of airlines and the aviation industry as a whole.

<p align="right">(<a href="#readme-top">back to top</a name>)</p>

## Reflections
**Yerlan's Reflection:**   If truth be told, I was scared to start compulsory coding assignments of Astar planning since I was a newcomer for coding at all. However, after starting the project, it did not seem so unachievable anymore even though I have spent a lot of my time for those assignments. During each on and off session times, I, always, learnt something new about python in visual studio. Let's take task 1 for example. When I started do it, I realized that most of the part of coding here is just changing values by your logic, while a whole of my life I believed that any project that we start to do, we have to write each code by yourself. It was one of the reasons why I was afraid even to start it before in my life. Furthermore, there were parts where I was needed to write a code by myself from the beginning, an autonomous calculation of cost of each type of airbus, but it was as simply as general math equations. Just input some constant values and write the formula for them. After finishing of all 3 compulsory coding tasks, I have finally found some logic in python through the pain and tears. Even more, I just started to love it. During the GitHub project I have not only learnt coding, but I have also revealed some new aviation terms that bother me currently. Starting task 2, I was so confused about jet stream. As I have never heard about jet stream term before in my life, I did not even understand the task fully. Spending some time on reading separate articles and watching videos about those jet streams, I finally understood that, continuing completing a task with a new knowledge. 

At the same time, it was the first time for me when I was a leader of a serious group project and managed groupmates with their tasks. During the first week of GitHub project, everyone was so quiet, so I came to the decision that I should take the role of being leader. We all understand that success of the results mainly depends on a leader, who should divide tasks and choose correct person for this task wisely. Moreover, understanding that none of my fellow groupmates can code, I decided to split up other tasks of GitHub to small groups of people, so everyone could work on the project. Giving them their tasks, I also set up the deadlines, so I could control the whole process and understand will we finish it at time or not. 

To sum up, having GitHub project just did not teach me some basic concepts in coding and aviation, but also enhanced my leadership skills. After finishing all tasks, it can sound weird, but I am eager to start a new GitHub project with the team, trying all my soft and coding skills in solving issues that face current aviation. Even though it could be impossible, I have a willing to start learning coding more deeply, and I will do some courses during my winter break! The last but not least, the most essential part I think, I found new good friends from my cohort with whom I can easily start talking at any time!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Namnet's Reflection:**  When we first started the project I was very worried because of the coding that would be involved. As I do not have any coding experience, but luckily I was not the only one.  Everyone else in the group had zero to none experience in coding, which gave us all the opportunity to learn with each other and help develop our coding skills together. Although I did not do much in the main coding sections in the task, I was able to help out by working with Dina Hang to fill out the readme report. But none of my commitments to this project compares to the amount of work our group leader Yerlan has put into this project. He has constantly worked on the project since the beginning from organizing our group, to setting targets and to his commitment in task 2. He is the real reason our group has been able to function this well, he really is the true MVP of the group.

Throughout the whole subject including this project, I have learnt more about the aviation industry as a whole. From the key topics in the first few lectures to the concepts shown in MOOC and the collaborative experience in this project. I have learnt a lot and will treasure these experiences to better prepare myself for my journey in the aviation industry.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Hang's Reflection:** The first day that I stepped into the lecture hall, I was as always, late. Fortunately, my teammates were there and they even had a seat for me. You are welcome! Then when the lecturer started talking about the the project, I told myself, “I am so forked.” I mean coding for real, and like for a significant project? Anyways, I listened on nodding to every single word Dr. Hsu said, as if I knew I what he was saying. It takes patience to listen and it takes skill to pretend you’re listening, I have skills.

Anyways, I saw that the project was not all about making computers do things for you. We also had to write summaries notoriously called the Read.me, make PowerPoint slides, and even a record video. When Dr. Hsu stated that we need to nominate a group leader at the first lecture, it was one of the most memorable moment. Everyone started playing hide-and-seek at once. “Ummm, I don’t know coding, do you?” Fortunately, we fund a leader and our team members exhibited selflessness to such a degree that I think they should receive a 'Medal of Hard-work’. Some even worked tirelessly on the code throughout the day and night, including, as far as I can recall, other subject lectures. 

The initiative allowed me to get to know some extremely wonderful and selfless individuals and deepen my friendship with others I was previously acquainted with. I picked up a few technical tips here and there, but the greatest part was that I got to write, which is something I like doing.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Frederick's Reflection:** Before doing this project, I thought coding is irrelevant to Aviation Engineering this is my first time knowing about coding. Initially, what I was hoping is that after I had finished this project, I don’t need to ‘keep in touch’ with coding anymore. In the first lesson, I downloaded the VS Code to familiarize myself and also it lets me communicate with my groupmates easily. Personally, I hate using a computer so much. Therefore, I spent a lot of time learning how to use the VS Code but there were many technical issues existed and I feel helpless at that time. Luckily, my groupmates are generous and they help me to fix the issue. After that, I successfully finished some parts of task 1 such as editing both the start node and goal node. After that, I did task 3 in the readme to explain which aircraft we selected to best fit Scenario 1 in task 1 and the reason why we had selected this aircraft. I collected some information from my groupmates related to calculation parts and summarize it in the readme. Trends, results and reasons etc. had been explained deeply in the readme to support why we had selected B797 to minimize the costs for task 1.

In this project, what I learned is that coding took an important role not just in our course, it also affected the whole world. For example, in our project, we are required to use coding to solve three tasks these three tasks are really complicated or even impossible if it is solved by our own hands. Therefore, we need to overcome any challenges as using advanced technologies will be a trend in the real world situation. Moreover, to determine whether an airline is successful or not, there are many factors we need to consider.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Jophy's Reflection:**    As I was majorly focus on the calculations part in Task 1 and Task 3, as well as deciding the type of aircraft we would like to design, this project really opened my eyes up on the algorithms behind the aviation industry in order to strive for profit maximization due to the skyrocketting fuel price and meeting the market demand. It was never an easy task to decide the best aircraft for the route due to all sorts of constraints, let alone designing a new aircraft that will fit the exsisting market. In the project our group has discussed a lot on whether a smaller twin-engine aircraft or a larger quad-engine aircraft will best fit this scenario we are given as well as the future trends in the world of aviation.
Thus, we are able to optimize the cost and the revenue of each flight as it can have a significant impact an an airline's financial state and sustainability.  Morover, this project also equipped me the basics on coding which this area is vitally important to the future development of the aviation industry regarding safety and profit-making. Being an aviation enthusiast since a young age, I have tried several airline managing games in the past and I used to spend quite a lot of effort on the calculations of each flight using in-game statistics. Those experiences really bring me an upper hand in this project and I am looking forward to apply those knowledge acquired from the project into my future career.
  However, from my recent obserations and researches, the parameters that appeared in the project are not the only parameters that affect the final decisions of airline choosing which aircraft for the specific route due to other market concerns. For example, the A350 and B777 series have a much wider body which can equip a more spacious, luxurious and cutting-edge first-class products to receive a higher ticketting revenue whilst enhancing its brand value. LLCs usually have an air fleet consist of one or few types of aircrafts only in order to minimise its staff training and maintenance parts cost which makes them have fewer choice on the aircraft selection for specific routes compare to major cities' flag carriers. This already involving considerations in not only engineering but also marketing and human resources.
  I really enjoy being part of this project and helping with the calculations involved in the codes. Once again I am so grateful for all the hardwork everyone has done in this project.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Tim's Reflection:**   When the teacher told me I have to do coding like the sample he showed, I was shocked since I didn't do programming before. Luckily I don't have to start from nothing , he provided some basic A* path finding algorithms for us. After a discussion with my group member, I discover that it is no that difficult, in fact I change some values and it run perfectly. I was so delighted at the time I successfully run the code. I also find coding is so interesting therefore spending some time to do research. As I am doing additional task 2 and 3 coding ,it help enhancing my technical skill and make me confidence on coding. Moreover my groupmates is very supportive and give many important infomation for us. I really enjoy being part of this project and doing research on the coding. After this lesson I understand that coding is useful in aviation industry like minimize the cost and finding shortest flight path. I am so thankful for all the hard work my group members have done in this project. Also I gain useful skills and made a lot of friends.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Boey's Reflection:**   To be honest I don’t even know what is github at first. Before the project start, I thought coding is unrelated to aviation engineering, thanks to the explanation from lecturer whereas it made me a total newbie for coding. When I knew I need to work with someone I don’t know before, I was very frustrating and nervous when I join the first lesson. Fortunately, the lecturer is interesting and easy going, making me feel relieve. But during the whole lecture, even though I listen very concentrated, I’m still puzzling about the project, but my groupmates already have some ideas. Since my technical skill is insufficient, I responsible for the PowerPoint and the video editing. It seems easy but hard because I need to understand what the content for each task are and why my groupmates code like that. I am an introvert, so it takes me some time to communicate with my groupmates initiatively. Luckily, my groupmates are all kind and helpful. Thanks to their help and the video on YouTube, I can understand the complicated theory and edit the ppt fluently. From this experience, I learnt that communication is important and the importance of path planning. Without bonding with groupmates, I won’t be able to finish the ppt accurately.

<p align="right">(<a href="#readme">back to top</a>)</p>

## Contacts
**Yerlan** - https://www.linkedin.com/in/yerlan-turaly-5b2310246/ - 22096542d@connect.polyu.hk

**Namnet** - 22031071d@connect.polyu.hk

**Hang** - 22072105d@connect.polyu.hk

**Frederick** - pts031022@gmail.com

**Jophy** - jhtse72@gmail.com

**Tim** - timmttsang@yahoo.com.hk

**Boey** -22075814d@connect.polyu.hk

**Project Link** - https://github.com/captainnccrruunncchh/AAE2004-group-9

<p align="right">(<a href="#readme">back to top</a>)</p>

## Project Status
Project is in progress. Compulsory coding tasks, two additional coding tasks, ReadMe, and presentation are done. Video is in production.

<p align="right">(<a href="#readme">back to top</a>)</p>
