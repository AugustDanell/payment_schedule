# payment_schedule
A friend asked me for a system to calculate payments based on worked schedule. The implementation of this system is rather naive in a sense. We use nested a hashmap D that maps keys like this: Day -> Hour -> Minute -> Pay.

As such the good user can input the days, hour and minutes and what is the pay of those. Thereafter we take in the user's time input on the form of:
Start: HH:MM
End: HH:MM

The difference between them is calculated and we iterate through the map D for each minute. As such we can account for work time that overlaps between two different scheduled times in terms of pay (Consider for instance if monday 10-16 = 100 sek, but 16-18 = 150 sek, and our friend works from 10-17). Iterating over every minute will yield the hourly pay per minute (least time unit). We then just divide this sum with 60 and obtain for our deer friend what he has earned for his hard work. 

Examples:
Here the user earns 100 SEK for each our hour:
![image](https://user-images.githubusercontent.com/70810124/171604785-c3cbbafc-82f7-4f66-817a-fe0df6c81d9a.png)

