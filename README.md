# CrackSAT
My first ever web scraping project to extract all pdf data from CrackSAT website.

CrackSAT is a website that hosts a plethora of worksheets and practice exams for SAT exam prep. This is a tool that I built to scrape their site to extract those pdf files.

To gain access to their pdf files, one must navigate three seperate links, the last of which leads to a hashed google drive file. 

My initial attempt involved using autoHotkey to automate a series of clicks and keyboard presses to dl the material. I also used ahk's image search capabiities, which I learned with the help of Pulover's Macro creator. Despite its initial promise, this approach ultimately failed since it was not robust enough to handle varying page load times.

After giving up on that approach, I decided to use python's beautiful soup module to extract the html of the page, then use regular expressions to find the clickable element. I then use the requests module to get the html data for the next page and repeat the process.

Were I to repeat this project today, I would no doubt use the python library selenium to automate a series of clicks on particular html elements by using their corresponding xpaths. 

Note: some of the files have been recently taken down from the cracksat website.
