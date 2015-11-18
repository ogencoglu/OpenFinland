# Author         : Oguzhan Gencoglu
# Contact        : oguzhan.gencoglu@tut.fi
# Created        : 16.10.2015
# Latest Version : 18.11.2015

library(wikipediatrend)
library(ggplot2)

# Fetch page view data
wp_russia <- wp_trend(page = c("Venäjä","Vladimir_Putin"),
                   from = "2007-08-01", 
                   to   = "2015-10-01", 
                   lang = "fi")

ggplot(data=wp_russia,
       aes(x=date, y=count, colour=title)) +
        theme(legend.text=element_text(size=30)) +
        geom_line()