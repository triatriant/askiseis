print ("Καλησπέρα" +\
"!! Χρησιμοποιείται η έκδοση 3.6 της python !!")

print ("ΆΣΚΗΣΗ 2:Γράψτε ένα πρόγραμμα το οποίο παίρνει σαν είσοδο μία ακολουθία \n"
" παρενθέσεων και επιστρέφει True/False αν αυτή η ακολουθία μπορεί να υπάρχει σε μία μαθηματική παράσταση.")

class askisi_2:
    def parenthesi(par):
        pchar= { "(" : ")" }
        #ελέγχει αν η ακολουθία μπαίνει στην παράσταση
        if par in pchar:
            print("Μπορεί να είναι σε μαθηματική παράσταση:")
            return True
        else:
            print("Δεν μπορεί να είναι σε μαθηματική παράσταση:")
            return False


par=(input("Δώστε την ακολουθία ου επιθυμείτε."))
print(askisi_2().parenthesi())

print ("!! ΤΕΛΟΣ ΑΣΚΗΣΗΣ 2 !!")
