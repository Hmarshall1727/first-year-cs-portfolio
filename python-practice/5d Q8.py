string= "VfL Osnabruck won the 3. Liga with 80 points, they return to the 2. Bundesliga after two seasons in the third tier. Second place Energie Cottbus finish with 72 points. Rot-Weiss Essen in third finish with 70 points and lost their playoff matches against SpVgg Greuther Furth. MSV Duisburg missed out on promotion in fourth with 68 points, Hansa Rostock behind in fifth with 67 points. Sixth place SC Verl and seventh place Alemannia Aachen both got 64 points, while 1860 Munchen, Wehen Wiesbaden, and Waldhof Mannheim who got eighth, ninth, and tenth respectively all got over 50 points. However, 1860 Munich got relegated due to being unable to get a licence for the upcoming 2026/27 season. Eleventh place Viktoria Koln got 51 points whereas FC Ingolstadt got 49 points in twelth. In thirtheen is SSV Jahn Regensburg who got 49 points and behind them with 46 points is VfB Stuttgart II. 1. FC Saarbrucken had a disappointing season coming in fifteenth with 44 points while TSG Hoffenheim II received 43 points in 16th. Originally, TSV Havelse in seventeenth got relegated with 35 points but were spared after 1860 Munchen's problems. The other relegated teams are Erzgebirge Aue in eighteenth with 34 points, SSV Ulm 1846 in nineteenth with 33 points, and  1.FC Schweinfurt 05 at the bottom who got a horrible 21 points."

numbers = [string.strip() for string in string.split(" ") if string.isnumeric()]

print(f"This is the 3. Liga table report: {string}")


print(f"and these are all the numbers in that report: {numbers}")
