print('''
████████╗██╗██████╗      ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗     
╚══██╔══╝██║██╔══██╗    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    
   ██║   ██║██████╔╝    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝    
   ██║   ██║██╔═══╝     ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗    
   ██║   ██║██║         ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    
   ╚═╝   ╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    

Welcome to tip calculator.''')
bill = float(input("What was the total bill? \n ₹"))

tip = int(input("\n What percentage tip would you like to give? \n Enter 10, 12, or 15 \n"))

people = int(input("\n How many people to split the bill? \n"))

tipPer = bill *(tip / 100)
TotalBill = (tipPer + bill) / people

print(f"\n Each person should pay ₹{round(TotalBill, 2)}")