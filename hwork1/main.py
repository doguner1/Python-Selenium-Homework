#Tam Sayılar (int): Tamsayıları ifade etmek için kullanılır. Örneğin, 1, 2, 3 gibi.

#Kayan Noktalı Sayılar (float): Virgüllü sayıları ifade etmek için kullanılır. Örneğin, 1.0, 2.5, 3.1415 gibi.

#Karmaşık Sayılar (complex): Gerçek ve sanal sayılardan oluşan sayıları ifade etmek için kullanılır. Örneğin, 3+2j, 1-4j gibi.

#Karakter Dizileri (str): Metin verilerini ifade etmek için kullanılır. Örneğin, "Merhaba Dünya", "Python Programlama Dili" gibi.

#Boolean (bool): Doğru veya Yanlış değerlerini ifade etmek için kullanılır. Bu veri tipi, sıklıkla koşullu ifadelerde veya döngülerde kullanılır.

#Listeler (list): Değiştirilebilir elemanlardan oluşan veri yapılarıdır. Liste elemanları arasında farklı veri tipleri bulunabilir. Örneğin, [1, "Merhaba", 2.5, True] gibi.

#Demetler (tuple): Değiştirilemez elemanlardan oluşan veri yapılarıdır. Demet elemanları arasında farklı veri tipleri bulunabilir. Örneğin, (1, "Merhaba", 2.5, True) gibi.

#Sözlükler (dictionary): Anahtar-değer çiftleri halinde saklanan veri yapılarıdır. Anahtarlar ve değerler farklı veri tiplerinden olabilir. Örneğin, {"isim": "Ahmet", "yaş": 25, "cinsiyet": "Erkek"} gibi.

#Kümeler (set): Benzersiz elemanlardan oluşan değiştirilebilir veri yapılarıdır. Örneğin, {1, 2, 3, 4} gibi.


userName="doğukan"
userPassword=1234

user_Name= input("lütfen kullanici adinizi giriniz: ")
user_Password = int(input("lütfen sifrenizi giriniz: "))

if userName==user_Name and userPassword==user_Password:
  print(f"Basariyla giriş yapildi. Hoşggeldin {userName}")
elif userName==user_Name and userPassword!=user_Password:
  print(f"{userName} şifreniz hatalı!")
else:
  print("Kullanıcı bulunamadı")
  