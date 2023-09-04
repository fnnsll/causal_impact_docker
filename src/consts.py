#Set these - currently they're hard coded and require a docker build command to replace in the image. Will make them settable by temp json file in the future
csv = '/home/input/dl_blverlauf.csv'
date = 'Datum'
region = 'Gruppe'
kpi = 'Genkopien pro EW / Tag * 10^6'
y = 'Wien' #Test
X = 'Salzburg' #Control
pre_period = ['2022-09-01', '2023-06-01']
post_period = ['2023-06-02', '2023-08-27']
test_percent = 1 #Set this to a value like 1.2 for a simulated 20% uplift, or 5 to get a visual picture that an uplift works
timestamp = '2023-01-01'
