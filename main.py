
import time
import deck

dina_kort = []
dato_kort = []

def Calc_cards_min(hand):
    sum=0
    for item in hand:
        sum=sum+item.get_value_min()
    return sum

ans=True
while ans:
    print("""
    1.Start a black jack game
    9.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\nGame started")
      kortlek=deck.Deck()
      print('Dina kort')
      for i in range(1,3):
          kort = kortlek.give()
          dina_kort.append(kort)
          print(kort)
      print('Datorns kort')
      for j in range(1, 3):
        kort = kortlek.give()
        print(kort)
      while True:
        svar1 = input('vill du ha fler kort(j/n')
        if svar1=='j':
            kort = kortlek.give()
            dina_kort.append(kort)
            print(kort)
            kortvalue = Calc_cards_min(dina_kort)
            print('du har som minst ' + str(kortvalue))


        else:
            break






    elif ans=="9":
      print("\n Goodbye")
      time.sleep(3)
      ans = None
    else:
       print("\n Not Valid Choice Try again")