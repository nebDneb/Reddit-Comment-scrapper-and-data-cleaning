# Reddit-Comment-scrapper-and-data-cleaning
Reddit Comment scrapper with text cleaning. Word cloud presentation through R.

Hello!
So first, I'd go through the .py file and enter the correct reddit credentials while also entering which subreddit you'd want to explore.
I'd also try a trial run by changing the forest numbers so that you'd generate a smaller file. Change the limit from 1000 to 100.

Once generated, each "word" will be in it's own cell in Excel. As you notice, there are a ton of entries that have special character entries and a ton of space bars. 

This is where the VBA code is helpful. Install the Morfunc package for excel before you use the VBA script. 
Make sure you create a special characters sheet in a different tab. This can range from generating a wiki table with special characters to you deciding which characters
you want replaced in your list.
Have this list in a tab infront of the python generated list in excel. 

The function, "=replacer()", takes the active cells and runs it through the special character list, then if it identifies 
a character it would replace the special characters with a blank. 

Once that has been cleaned up, id save the clean column into a seperate file. I then brought the file into another program and capitalized every single entry in DOCs 
(working in caps made everythign easier) 

Now this is where some discrepancies may occur!
How can we count the frequency of each word?
That's where "=sumif()" comes in. In my situation I wanted to see the frequency of character names from One Piece. So I created a name list (all capitalized as well) and 
had the sumif function look at the name list and sum the frequency. You can also add a boolean value to the highest frequency words so that you can seperate the words 
by color in the word cloud.

Now that you have a table with the, cleaned words, frequency, and/optional boolean, you can finally start the word cloud generation in R. 

Thanks for checking out my project!!!
-nebDneb 
