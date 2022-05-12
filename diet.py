import mysql.connector
from mysql.connector import Error
import json
import pandas as pd

def meal_logger():

	totalcalories = 0
	totalcarbs = 0
	totalprotein = 0
	totalfat = 0

	weight = int(input("How much do you weight today(enter number in pounds)?"))
	breakfast = int(input("What did you eat for breakfast?\n 1. (2) scrabled eggs \n 2. bacon & egg sandwhich \n 3. oatmeal \n 4. cup of cereal \n 5. nothing \n"))
	lunch = int(input("What did you eat for lunch?\n 1. grilled chicken \n 2. (1) pizza slice \n 3. tacos(3 count) \n 4. chicken nuggets(5 count) \n 5. nothing \n"))
	dinner = int(input("What did you eat for dinner?\n 1. grilled chicken \n 2. for salmon fillet \n 3. tacos(3 count) \n 4. chicken nuggets(5 count) \n 5. nothing \n"))
	anything_else = int(input("Did you eat anything else? \n 1. Chicken Ceaser salad \n 2. Chicken tenders(3 count) \n 3. Banana \n 4. bag of potatoe chips \n 5. cheese pizza slice \n 6. Tuna sandwhich \n 7. Cheese Burger \n 8. Nothing \n "))


	if breakfast == 1:
		totalcalories = totalcalories + 200
		totalcarbs = totalcarbs + 2
		totalprotein = totalprotein + 13
		totalfat = totalfat + 13
	elif breakfast ==2:
		totalcalories = totalcalories + 388
		totalcarbs = totalcarbs + 28
		totalprotein = totalprotein + 21
		totalfat = totalfat + 21
	elif breakfast ==3:
		totalcalories = totalcalories + 145
		totalcarbs = totalcarbs + 25
		totalprotein = totalprotein + 6
		totalfat = totalfat + 2
	elif breakfast ==4:
		totalcalories = totalcalories + 124
		totalcarbs = totalcarbs + 27
		totalprotein = totalprotein + 6
		totalfat = totalfat + 2
	elif breakfast ==5:
		totalcalories = totalcalories + 0
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 0
		totalfat = totalfat + 0

	if lunch == 1:
		totalcalories = totalcalories + 284
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 57
		totalfat = totalfat + 7
	elif lunch ==2:
		totalcalories = totalcalories + 254
		totalcarbs = totalcarbs + 32
		totalprotein = totalprotein + 11
		totalfat = totalfat + 10
	elif lunch ==3:
		totalcalories = totalcalories + 630
		totalcarbs = totalcarbs + 33
		totalprotein = totalprotein + 57
		totalfat = totalfat + 10
	elif lunch ==4:
		totalcalories = totalcalories + 238
		totalcarbs = totalcarbs + 13
		totalprotein = totalprotein + 12
		totalfat = totalfat + 15
	elif lunch ==5:
		totalcalories = totalcalories + 0
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 0
		totalfat = totalfat + 0
	

	if dinner == 1:
		totalcalories = totalcalories + 284
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 57
		totalfat = totalfat + 7
	elif dinner ==2:
		totalcalories = totalcalories + 468
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 50
		totalfat = totalfat + 28
	elif dinner ==3:
		totalcalories = totalcalories + 630
		totalcarbs = totalcarbs + 33
		totalprotein = totalprotein + 57
		totalfat = totalfat + 10
	elif dinner ==4:
		totalcalories = totalcalories + 238
		totalcarbs = totalcarbs + 13
		totalprotein = totalprotein + 12
		totalfat = totalfat + 15
	elif dinner ==5:
		totalcalories = totalcalories + 0
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 0
		totalfat = totalfat + 0	


	if anything_else == 1:
		totalcalories = totalcalories + 309
		totalcarbs = totalcarbs + 8
		totalprotein = totalprotein + 29
		totalfat = totalfat + 17
	elif anything_else ==2:
		totalcalories = totalcalories + 336
		totalcarbs = totalcarbs + 21
		totalprotein = totalprotein + 21
		totalfat = totalfat + 18
	elif anything_else ==3:
		totalcalories = totalcalories + 89
		totalcarbs = totalcarbs + 23
		totalprotein = totalprotein + 1
		totalfat = totalfat + 0
	elif anything_else ==4:
		totalcalories = totalcalories + 150
		totalcarbs = totalcarbs + 15
		totalprotein = totalprotein + 2
		totalfat = totalfat + 5
	elif anything_else ==5:
		totalcalories = totalcalories + 260
		totalcarbs = totalcarbs + 32
		totalprotein = totalprotein + 11
		totalfat = totalfat + 10	
	elif anything_else ==6:
		totalcalories = totalcalories + 440
		totalcarbs = totalcarbs + 42
		totalprotein = totalprotein + 30
		totalfat = totalfat + 16
	elif anything_else ==7:
		totalcalories = totalcalories + 535
		totalcarbs = totalcarbs + 39
		totalprotein = totalprotein + 30
		totalfat = totalfat + 29
	elif anything_else ==8:
		totalcalories = totalcalories + 0
		totalcarbs = totalcarbs + 0
		totalprotein = totalprotein + 0
		totalfat = totalfat + 0

	print("Total calories:\n",totalcalories)
	print("Total carbs:\n",totalcarbs)
	print("Total protien:\n",totalprotein)
	print("Total fat:\n",totalfat)
	print("You weight",weight)

	try:
	    connection = mysql.connector.connect(host='127.0.0.1',
	                                         database='diet',
	                                         user='root',
	                                         password='')

	    mySql_select_Query = "INSERT INTO diet(total_calories,total_carbs,total_fat,total_protein,weight) VALUES (%s,%s,%s,%s,%s)"
	    val = (totalcalories,totalcarbs,totalprotein,totalfat,weight)
	    cursor = connection.cursor()
	    #cursor.execute(mySql_select_Query)
	    cursor.execute(mySql_select_Query,val)
	    #row_count = 2
	    connection.commit()
	    print(cursor.rowcount, "record inserted.")

	except Error as e:
	    print("Error while connecting to MySQL", e)
	finally:
	    if connection.is_connected():
	        cursor.close()
	        connection.close()
	try:
	    connection = mysql.connector.connect(host='127.0.0.1',
	                                         database='diet',
	                                         user='root',
	                                         password='')

	    mySql_select_Query = """SELECT * FROM diet"""
	    cursor = connection.cursor()
	    #cursor.execute(mySql_select_Query)
	    cursor.execute(mySql_select_Query)
	    #row_count = 2
	    myresult = cursor.fetchall()
	    #record = cursor.fetchall()
	    #result = json.dumps(myresult)
	    #print(result)
	    df = pd.DataFrame(myresult, columns=['id', 'total_calories', 'total_carbs','total_fat','total_protein','weight'])
	    averagecalories = df['total_calories'].mean()
	    averagecarbs = df['total_carbs'].mean()
	    averagefat = df['total_fat'].mean()
	    averageprotein = df['total_protein'].mean()
	    averageweight = df['weight'].mean()

		#avgweight = df[df['FT%']==maxFT]
	    print(df)
	    print("Average Weight ", averageweight)
	    print("Average calories consumed: ", averagecalories)
	    print("Average carbs consumed: ", averagecarbs)
	    print("Average fat consumed: ", averagefat)
	    print("Average protein consumed: ", averageprotein)

	except Error as e:
	    print("Error while connecting to MySQL", e)
	finally:
	    if connection.is_connected():
	        cursor.close()
	        connection.close()

meal_logger()