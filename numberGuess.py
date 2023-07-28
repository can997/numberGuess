class numberGuess():

    def __init__(self):
        pass
    def randomNumber():
        import random

        random_number=random.randrange(1,100)
        return random_number

        
    def guessNumber():
        count = 1
        random_number=numberGuess.randomNumber()
        while True:
    
            guess_number=input("Lütfen tahiminizi giriniz: ")
            try:

                guess_number=int(guess_number)
                
                if not 0 < guess_number < 100:
                    raise Exception("Lütfen 0 ile 100 arasında bir rakam seçiniz")
                elif guess_number < random_number:
                    print("Girdiğiniz rakam küçük")
                    count+=1
                elif guess_number > random_number:
                    print("Girdğiniz rakam büyük")
                    count+=1
                elif guess_number == random_number:

                    print(f"\n\n\n!!!!!\nDoğru Tahmin!!!\n{count}. Tahmininizde bildiğiniz\nSayı: {guess_number}\n\n\n")
                    break
            
            except ValueError:

                print("Lütfen Sayısal Bir değer Giriniz")
            except Exception as Ex:
                print(Ex)


numberGuess.guessNumber()
