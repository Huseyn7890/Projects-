saatliq_qazanc=int(input("Zəhmət olmasa saatliq qazancınızın daxil\nedin: "))
gunluk_is_saati=int(input("Zəhmət olmasa günlük iş saatını daxil\nedin: "))
hetelik_is_günü=int(input("Zəhmət olmasa həftədə necə gun işləyəsi olduğunuzu daxil edin: "))

gunluk_qazanc=gunluk_is_saati*saatliq_qazanc
hetelik_is_saati=gunluk_is_saati*hetelik_is_günü

def elavesiz_qazanc(saatliq_qazanc,gunluk_is_saati,hetelik_is_günü,gunluk_qazanc,hetelik_is_saati):
    if hetelik_is_saati>40:
        heftelik_qazanc=(hetelik_is_saati-(hetelik_is_saati-40))*saatliq_qazanc
    elif hetelik_is_saati<40:
        heftelik_qazanc=hetelik_is_saati*saatliq_qazanc 
    return heftelik_qazanc
   
   
def overtime_qazanc(saatliq_qazanc,gunluk_is_saati,hetelik_is_günü,gunluk_qazanc,hetelik_is_saati):
    overtime_is_saati=hetelik_is_saati-40
    overtime_heftelik_qazanc=overtime_is_saati*saatliq_qazanc*1.5
    return overtime_heftelik_qazanc


if hetelik_is_saati<40:
    print("Sizin toplam həftəlik gəliriniz: ")
    print(elavesiz_qazanc(saatliq_qazanc,gunluk_is_saati,hetelik_is_günü,gunluk_qazanc,hetelik_is_saati))

elif hetelik_is_saati>40:
    print("Sizin toplam həftəlik gəliriniz: ")
    print(elavesiz_qazanc(saatliq_qazanc,gunluk_is_saati,hetelik_is_günü,gunluk_qazanc,hetelik_is_saati)+overtime_qazanc(saatliq_qazanc,gunluk_is_saati,hetelik_is_günü,gunluk_qazanc,hetelik_is_saati))

else:
    print ("Ne isə səhv getdi")   