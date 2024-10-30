def musobaqa_oyini():
    print("Musobaqa o'ynaymiz !!!")

    #o'yinchilarning ismlarini olamiz
    ishtirokchi_1=input("1-ishtirokchi ismingizni kiriting:")
    ishtirokchi_2=input("2-ishtirokchi ismingizni kiriting:")


    #o'yinchilarning natijalari
    ishtirokchi1_score=0
    ishtirokchi2_score=0

    #Savollar ro'yxati
    savollar=[
        {
            "savol":"lower() funksiyasining vazifasi matnlarni ....  ga o'zgartirish ",
            "javoblar":["katta","kichik","integerga "],
            "t_javob":"kichik"

        },
        {
            "savol": "Konstitutsiya qabul qilingan yil qaysi ? ",
            "javoblar": ["1992", "1993", "1994 "],
            "t_javob": "1992"

        },
        {
            "savol": "upper() funksiyasining vazifasi matnlarni ....  ga o'zgartirish",
            "javoblar": ["katta", "kichik", "integerga "],
            "t_javob": "katta"

        },
        {
            "savol": "5**2  pythonda  qanday natija chiqadi ?",
            "javoblar": ["25", "10", "error "],
            "t_javob": "25"

        }


    ]

    for i,savol in enumerate(savollar,start=1):
        print(f"{i}-savol {savol['savol']}")

        for z,j in enumerate(savol['javoblar']):
            print(j)

        #o'yinchi javobini kiritishi kerak
        if i%2==1:
            javob=input(f"{ishtirokchi_1} javobingizni kiriting:")
        else:
            javob=input(f"{ishtirokchi_2} javobingizni kiriting:")

        #tog'ri javobni tekshirish
        if i%2==1:
            if javob==savol['t_javob']:
                print("Javobingiz tog'ri")
                ishtirokchi1_score+=1
            else:
                print("Javoblingiz xato")
        elif i%2==0:
            if javob == savol['t_javob']:
                print("Javobingiz to`g`ri")
                ishtirokchi2_score += 1
            else:
                print("javobingiz noto`g`ri:")
         #to`plagan ballar
    print(f"{ishtirokchi_1 }birinchi ishtirokchining to`plagan ballari{ishtirokchi1_score}")
    print(f"{ishtirokchi_2 }ikkinchi ishtirokchining to`plagan ballari{ishtirokchi2_score}")


musobaqa_oyini()
