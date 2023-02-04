#Atm Project
import sys
print("-"*50)
print("\tATM OPerations")
print("-"*50)
print("\t1.Deposit")
print("\t2.Withdraw")
print("\t3.Bal Enq")
print("\t4.Exit")
print("-"*50)
bal=500
while(True):
	try:
		
		ch=int(input("\nEnter Your Choice:"))
		match(ch):
			case 1:
				
				damt=float(input("\nEnter how much amount you want to deposit:"))
				if(damt<=0):
					print("Please enter valid amount")
				if(damt>0):
				
					bal=bal+damt
					print("\n")
					print("="*60)
					print("your Account xxxxxxx123 credited with INR:{}".format(damt))
					print("Now Account xxxxxxx123 Balanace  after depositINR:{}".format(bal))
					print("="*60)
					
			case 2:
				
				wamt=float(input("\nEnter how much amount your want to Withdraw:"))#implcitly raises ValueError
				if(wamt<=0):
					print("Please enter valid amount")
				elif((wamt+500)>bal):
					print("InSuffFund")
				else:
					bal=bal-wamt
					print("\n")
					print("="*60)
					print("your Account xxxxxxx123 debited with INR:{}".format(wamt))
					print("Now  Account xxxxxxx123 Balanace after withdraw INR:{}".format(bal))
					print("="*60)
			case 3:
				print("your Account xxxxxxx123 BalanceINR:{}".format(bal))
			
			case 4:
				print("Thanks for using our Atm","\U0001F605")
				
				
			case _:
				print("your Selection of Operation is Wrong-try again")
	
		jh=input("\nDo you want to use ATM again:(Yes/No) ")
		if (jh.lower()=="no"):
			print("="*60)
			print("Thanx for using this program",'\U0001F605')
			print("="*60)
			sys.exit()	
	except ValueError:
		print("Don't enter strs, alpnums and symbols for choice of Operations:")
		