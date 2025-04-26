import smtplib
mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()
mail.login('diposreebiswas@gmail.com', 'gqmj bfwl gdaj frfg')
message = 'hello'
try:
   mail.sendmail('diposreebiswas@gmail.com','asmitroy383@gmail.com',message)
   print("Successfully completed")
except:
    print("Error")   
mail.quit()