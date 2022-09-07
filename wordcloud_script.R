library(RColorBrewer)
library(wordcloud2)
library(tidyverse)

#Here is a version where you would have a boolean applied to specific word groups or frequencies in EXCEL. This code would seperate those words
#by color inthe word cloud while still following the figure path

#Here you can edit the format of the table if needed. If not just leave it. 

pivot_names_f2 <- read_csv("#cleaned wordlist with boolean.csv", col_types = cols( Freq = col_integer()))

fill_path <- filter(pivot_names_f2)
#Here additional filter can be added to the list

wordcloud2(fill_path, size = 0.245,gridSize = 0.4, figPath = '#a silhouette image.png', 
           color =  ifelse(fill_path$Boolean == TRUE, 'white', 'yellow'),
           backgroundColor = 'light-grey',
           rotateRatio = 1)
           
#A lot of customization can be done in the chunk above. You can use the special color codes and gradients provided by RColorBrewer library.



#This version is without the ifelse statment for the boolean insert in the wordcloud

pivot_names_f2 <- read_csv("#cleaned wordlist.csv", col_types = cols( Freq = col_integer()))

fill_path <- filter(pivot_names_f2)
#Here additional filter can be added to the list

wordcloud2(fill_path, size = 0.245,gridSize = 0.4, figPath = '#a silhouette image.png', 
           color =  'white'),
           backgroundColor = 'light-grey',
           rotateRatio = 1)
