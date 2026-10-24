# Journalistic
An esolang that looks like a diary entry.
Uses cells as memory and you can use entries to manipulate cells and their contents.

Keywords and phrases:
- Again
is a loop, by default will loop the rest of the code until count = 0.
- Again, at HH:MM
is the standard Again keyword but it loops with the specified time:
1. Odd but composite hour <
2. Even but composite hour >
3. Odd but prime hour =
4. Even but prime hour !=
the minute provided is the number being compared to the current cell contents
- Remember
this one prompt the user a number, and adds that number to the current cell contents.
- DD/MM/YYYY
the timestamp at the start of each entry.
1. Day = cell
2. Month = operator (even:minus/odd:plus)
3. Year = base value
- Today was the same as (day)
copies over the value of a cell to the current cell.

Positive words add 1 to the current cell.
Negative words minus 1 from the current cell.
Non-neutral punctuation (! and ?) add or minus 1 depending on month.
Neutral words print the current cell contents to console.
Neutral words in brackets print the current cell contents as an ASCII character to the console.

Have fun!
