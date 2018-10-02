
print("Berat",23,"Gökberk","İşler")
print("Berat\nGökberk\nİşler")
print("19","09","1993",sep="/") #bu satır yorum satırıdır.
print("{} + {} = {}".format(2,3,2+3)) 




a = 3  #int
b = 3.14 #float
c = "Python" #string
d = [1,2,3,4,5,6] # liste
e = (1,2,3,4,5,6,7) #tupple
f = {"Elma":3,"Armut":4,"Kiraz":5} #sözlük
g = True # False iki değer alır boolean

print(type(a)) # a değişkeni hangi veri tipine sahiptir.

print(a,b,c)



print(3+4) #matematiksel operatörler
print(10-3)
print(10*3)
print(10/2)

print(10 // 4) # tam sayı bölmesi için kullanılan operatör

print(10 %4 ) # kalan bulma operatörü

a = 5
b = 10

c = a+ 2 * b
print(c)

a = "Python"
b = "Programlama"
c = "Dili"

d = a + b + c 
print(d)

a = "python"
print(a * 5)

print("*" * 1)
print("*" * 2)
print("*" * 3)


a = "python"
b = [1,2,3,4,5,6,7]

print(a[0]) #kaçıncı index
print(a[2])
print(len(a)) #a değişkeni içinde kaç eleman var , uzunluk
print(len(b))

print(a[5]) # 5. indexteki eleman

print(a[len(a)-1]) #uzun bir listedeki son elemanı bulurken kullanabiliriz
print(b[len(b)-1])

print(a[0:2]) # 0. indexten 2. indexe kadar olan elemanlar
print(a[2:]) #2. indexten sona kadar parçala

print(a[:4]) #baştan başlayıp 4.indexe git ve parçala

print(b[2:]) # 2.indexten başla sona kadar git

print(b[0:6:2]) # 0dan başla 6.indexe 2 atlayarak git.

print(b[::2]) #bastan sona 2 atlayarak git .

a = {"Elma":3,"Armut":4,"Kiraz":5} #sözlük veri tipi

print(a["Elma"]) #elmaya karşılık gelen değer.
print(a["Kiraz"]) #kiraza karşılık gelen değer.


yas = input("Yaşınızı Giriniz :") #input alma 
print("Yaşınız",yas)

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("Toplam",a+b+c) # burada çıktı string olarak toplanır , dönüştürülme yapılması gerekir.

yas = int(input("Lütfen Yaşınızı Giriniz : ")) #if koşullu durumu
if yas < 18:
    print("Mekana Giremezsiniz....")
else:
    print("Mekana Hoşgeldiniz !!!!!!!")
    
islem  = int(input("İşlemi Giriniz : "))
if islem == 1:
     print("İşlem 1'i seçtiniz...")
elif islem == 2:
    print("işlem 2'yi seçtiniz...")
elif islem == 3:
    print("işlem 3'ü seçtiniz...")
else:
    print("Geçersiz İşlem !!!")


a = 3
b = 4

if a == 3 and b == 4 : #bağlama mantığı kontrol mekanizması (and,or)
    print("Başarılı !")
else:
    print("Başarısız :((")
   
   if (not (3==4)): # true yu false false u true yapar.
    print("Evet") 

#while döngüsü

i = 0

while i < 10 :
    print("i:",i)
    i = i+1 #döngünün sonlanması için arttırma değeri i += 1 yazabiliriz.
    
    i = 1
while (i < 1000):
    print("i:",i)
    i *= 2 #i değişkeni sayac değeri iki ile çarpılarak arttırılmıştır.


i = 0

while(i < 10):
    if i == 5 :
        break  # break 5 e gelindiğinde programdan çıkış yapılır.
    print("i:",i)
    i += 1
    
    # birde continue kodu var  , bu kod elde edilen değere gelince programı başa döndürür.
    #continue dan önce arttırma işlemi yapılmalıdır çünkü sonsuz döngüye yol açabilir.
    
    
#for döngüsü

a = [1,2,3,4,5,6]
b = "Python"
for karakter in b:
    print(karakter)


for sayi in range(0,100): # 0 dan 100 e kadar giden bir sayı dizisi oluştu. üçüncü parametre olarak atlama değeri verilebilir.
    print(sayi)
    

#fonksiyonlar

def selamla():
    print("Merhaba")
    print("Nasılsın")
    print("Burnun Kappıya Kısılsın xd ")
def selamla(isim = "Default Name"):
    print("Merhaba",isim)

selamla("Berat")
selamla("Burak")
selamla()  #atanmış isim çalıştırılır.

def toplama(a,b,c):
    return (a+b+c)  return fonksiyonu dışarıya bir çıktı yaratmak amacıyla kullanılır,normal şartlar altında atayacağımız bir değişkene none sonucu dönerken return sayesinde istediğimiz sonucu elde edebiliriz.

toplam = toplama(3,4,5)

print(toplam)


"""

"""
liste = [1,2,3,4,5,6]
a = "araba"

liste.append("Python") #listeye eleman ekleme
print(liste)

liste.pop() #içi boşken listenin  son elemanını çıkartır. içerisine index değeri verilince o indexi çıkartır.
print(a.startswith("b"))  # a stringi b harfi ile başlıyor mu ? False
print(a.endswith("b")) # a stringi b harfi ile bitiyor mu ? False

a = a.replace("a","o")  #a stringi içerisindeki a harflerini o harfi ile değiştir.
print(a)

#dosya işlemleri

file = open("Dosya.txt","a") #dosya kipleri nedir a,w ,r kipi okuma kipi a kipi ekleme w kipi yazma kipi ??

file.write("Naber Python\nNaber Java\nNaber Android") # bir sonraki yazılan içerik öncekini yok eder.

file.close()



file = open("Dosya.txt","r")
file.seek(10) #dosyanın 10.konumundaki veriye gider.
veri = file.read() #dosya içierğini okuma işlemi kodu. içerisine sayısal parametre verilmesi halinde belirtilen kadar karakter okur.
print(veri)
file.close()

file = open("Dosya.txt","r")  # for düngüsü ile okuma işlemi.
for satir in file:
    print(satir)
file.close()


#intro to python oop

class Account:
    def __init__(self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapbilgileri(self):
        print("İsim : ",self.isim)
        print("Numara : ",self.numara)
        print("Bakiye : ",self.bakiye)
    def paracek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz Yeterli Değil")
        else:
            self.bakiye -= miktar
            print("Yeni Bakiye : ",self.bakiye)
    def parayatir(self,miktar):
        self.bakiye += miktar
        print("Yeni Bakiye :",self.bakiye)


account = Account("Berat Gökberk İşler",123,1000)
account.hesapbilgileri()

account.paracek(800)
account.hesapbilgileri()
account.parayatir(3000)
account.hesapbilgileri()






