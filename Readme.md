# lupa

Read what is relevant from a web page (and nothing else)


## Introduction

lupa is though to simply reading information from familiar web pages. Pages 
usually full of propaganda, images and things which can be too destracting. 


## Installation
  -- Work in progress --
  
Make should install all necessary code to enable the local execution from the 
current directory. 
  
    $ make


## Usage

    $ lupa <page> <tag> <element> <alue>
    
Example:

    $ ./lupa http://www.cbc.ca h3 class headline
    Part-time, contract and seasonal workers now qualify for COVID-19 emergency benefits
    Coronavirus: What's happening in Canada and around the world Wednesday
    Chief medical officer of health to update Albertans about COVID-19
    Trump's move to cut WHO funding prompts world condemnation
    My husband doesn't need me to parent him
    Former Blue Jays all-star Damaso Garcia dies at 63
    Test your knowledge with this Canadian music-themed crossword puzzle
    Pandemic could affect food supplies, power grids, telecommunications
    Experts answer your COVID-19 questions at town hall
    Andrew Scheer says he has 'serious concerns' about WHO, Trudeau vows to stick with global health agency
    Experts criticize Ottawa for mismanaging and destroying millions of N95 masks
    COVID-19 in Quebec: 'We are asking doctors to join humanitarian mission,' health minister pleads
    Planning your first edible garden? Here are the steps to follow and common mistakes to avoid
    Ontario steps up fight against COVID-19 in long-term care homes as province confirms 494 new cases
    MLB, NFL possible in empty stadiums, disease expert Dr. Fauci says
    Experts criticize Ottawa for mismanaging and destroying millions of N95 masks
    11 tricky quizzes about Canada, eh?
    Compared to U.S., Canada's COVID-19 response a case study in political civility
    Architects and engineers are turning old shipping containers into mobile intensive care units
    Trudeau, ministers back Dr. Tam and Health Canada after Jason Kenney attacks pandemic response
    'Suspicious' biological passport leads to doping suspension for elite marathoner
    Global economy will suffer worst year since Great Depression of 1930s, IMF says
    4 Great Canadian Baking Show cookie recipes to try while you're stuck at home
    Ex-Flames coach Bill Peters hired by KHL team
    Jeopardy host Alex Trebek publishing memoir in July 2020
    This 107-year-old remembers the 1918 Spanish flu, and sees the similarities with COVID-19
    Scheer and Trudeau on the defensive over weekend travel during pandemic lockdown

    $ ./lupa https://www.distrowatch.com td class NewsHeadline
    News Filtering Options
    NEW • Development Release: deepin 20 Beta
    NEW • Distribution Release: Guix System 1.1.0
    NEW • Distribution Release: EndeavourOS 2020.04.11
    NEW • DistroWatch Weekly, Issue 861
    NEW • OS Release: ReactOS 0.4.13
    NEW • Distribution Release: AV Linux 2020.4.10
    NEW • Distribution Release: Tails 4.5
    NEW • DistroWatch Weekly, Issue 860
    NEW • Development Release: Ubuntu 20.04 Beta
    NEW • Distribution Release: ExTiX 20.4
    NEW • BSD Release: NetBSD 8.2
    NEW • Distribution Release: Rescatux 0.73
    Featured Distribution: 3CX Phone System

