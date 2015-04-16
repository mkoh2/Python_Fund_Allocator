from sys import exit

def choose(principal):
	# Taken from the Allocator.py example	
	savings = input('So, how much can you put into a savings account? $')
	interest_rate = .01
	time = input('How many years do you plan on keeping it in savings?: ')
	time += 1
	compound = 1
	annual = raw_input('Do you plan on adding funds annually? (Y/N): ')
	if annual == "Y":
		annual = input('How much do you plan on adding a year?: $')
	else:
		annual = 0
	
	print "Year %30s" % "Amount on deposit"
	
	for time in range(0, time):
 		formula = savings * (1 + interest_rate) ** time + \
		annual * (1+interest_rate) * ((1+interest_rate) ** time - 1) / interest_rate
		print "%4d%21.2f" % (time, formula)
	return principal
	
# Manually updated daily. 
# 	Need to find how to automatically scrape data from Google Finance
def schwab(principal):
	SWTSX = 38.12
	SWISX = 19.71
	SWLBX = 9.96
	
	SWTSX = float(SWTSX)
	SWISX = float(SWISX)
	SWLBX = float(SWLBX)
	
	principal = float(principal)
	
	#Allocation
	alloc1 = principal * .50
	alloc2 = principal * .20
	alloc3 = principal * .30
	
	#Calculating shares
	schwab_portfolio1 = (principal * .50) / SWTSX
	schwab_portfolio2 = (principal * .20) / SWISX
	schwab_portfolio3 = (principal * .30) / SWLBX
	
	schwab_portfolio1 = float(schwab_portfolio1)
	schwab_portfolio2 = float(schwab_portfolio2)
	schwab_portfolio3 = float(schwab_portfolio3)
	
	print """We recommend you use:\n
	50% US Stock
	20% International Stock
	30% Bonds\n"""
	
	print """And so:
	$%.2f will be invested into SWTSX (US Stock), which is at $%.2f.
	$%.2f will be invested into SWISX (Int'l Stock), which is at $%.2f.
	$%.2f will be invested into SWLBX (Bond), which is at $%.2f.\n""" % (alloc1, SWTSX, alloc2, SWISX, alloc3, SWLBX)
			
	print """From your principal of $%.2f, we calculated your portfolio to have the following:
	%.2f shares of SWTSX
	%.2f shares of SWISX
	%.2f shares of SWLBX""" % (principal, schwab_portfolio1, schwab_portfolio2, schwab_portfolio3)

# Manually updated daily. 
# 	Need to find how to automatically scrape data from Google Finance
def vanguard(principal):
	VTSMX = 52.95
	VGTSX = 16.82
	VBMFX = 11.01
	
	VTSMX = float(VTSMX)
	VGTSX = float(VGTSX)
	VBMFX = float(VBMFX)
	
	principal = float(principal)
	
	#Allocation
	alloc1 = principal * .50
	alloc2 = principal * .20
	alloc3 = principal * .30
	
	#Calculating shares
	vanguard_portfolio1 = (principal * .50) / VTSMX
	vanguard_portfolio2 = (principal * .20) / VGTSX
	vanguard_portfolio3 = (principal * .30) / VBMFX
	
	vanguard_portfolio1 = float(vanguard_portfolio1)
	vanguard_portfolio2 = float(vanguard_portfolio2)
	vanguard_portfolio3 = float(vanguard_portfolio3)
	
	print """We recommend you use:
	50% US Stock
	20% International Stock
	30% Bonds\n"""
	
	print """And so:
	$%.2f will be invested into VTSMX (US Stock), which is at $%.2f.
	$%.2f will be invested into VGTSX (Int'l Stock), which is at $%.2f.
	$%.2f will be invested into VBMFX (Bond), which is at $%.2f.\n""" % (alloc1, VTSMX, alloc2, VGTSX, alloc3, VBMFX)
			
	print """From your principal of $%.2f, we calculated your portfolio to have the following:
	%.2f shares of VTSMX
	%.2f shares of VGTSX
	%.2f shares of VBMFX""" % (principal, vanguard_portfolio1, vanguard_portfolio2, vanguard_portfolio3)
	
def gone(x):
	exit(0)
	
def start(): 
	print 'Welcome to the Automated Portfolio Allocator.'
	print 'To begin, let\'s figure out how much you can first invest.\n'
	
	principal = input('How much can you invest?: $')
	if principal >= 1000 and principal < 3000:
		print 'For investments equal to or greater than $1000, you can invest with Schwab.'
		print 'Please note, however, for investements above $3000, we recommend you invest with Vanguard.'
		schwab(principal)
	elif principal >= 3000:
		print 'For investments equal to or greater than $3000, you should invest with Vanguard.\n'
		vanguard(principal)
	else:
		print 'You need to have at least $1000 to start.' 
		print 'You can put money into a high-yield savings account.'
		choose(principal)
	
start()