.. _concept_benefitsofcontrollingatown:

Benefits of Controlling a Town
===============================

********
Benefits
********

Controlling a town brings with it a number of benefits:

1. Having the support of more than 50% of the population is a win condition
2. It will increase the amount of HR you get from the population of the town. The amount of HR you get is relative to the population of the town and whether you control the town (among other factors). Controlling a town effectively doubles the HR you will receive from it.
3. You get a (small) amount of money as well from the population that supports you
4. If you control a town, it definitely won't spawn enemy patrols
5. The support hit you receive when stealing a car from the town is lower
6. Perhaps the most important benefit is that the Occupiers will obsessively attack rebel towns to no real effect. This flaw in the enemy’s strategy is basically what gives the player the ability to expand elsewhere on the map and keep their important holdings (like resources) safe

************************************************************
Specific Calculation for a Town’s Contribution to HR
************************************************************

1. [Population] * ([Amount of Support] / 10000)
2. If the town is not controlled by the player’s faction, divide the number by 2
3. If the closest radio town is not owned by the player’s faction, divide the number by 2 again
4. Always round the number up

You may notice here that if you have any amount of support in the town it will always at least give you 1 HR. No matter how small the fraction of an HR is calculated to be, you always round up.

An example: 

1. Given a town with 290 population and 35 support for the player’s faction. The town is NOT controlled by the player and the player does not control the nearby radio tower
2. 290 * (35 / 10000) = 1.015
3. We do not control the city so divide by 2 = .5075
4. We do not control the closest radio tower so divide by 2 = .25375
5. Always round up the result = 1 HR

************************************************************
Specific Calculation for a Town’s Money Contribution
************************************************************

1. [Population] * ([Amount of Support] / 100) / 3
2. If the town is not controlled by the player’s faction, divide the number by 2
3. If the closest radio town is not owned by the player’s faction, divide the number by 2 again
4. Always round the number up

An example:

1. Given the same situation as the example above
2. 290 * (35 / 100) / 3 = 33.8333333333
3. We do not control the city so divide by 2 = 16.9166666667
4. We do not control the closest radio tower so divide by 2 = 8.45833333333
5. Always round up the result = $9
