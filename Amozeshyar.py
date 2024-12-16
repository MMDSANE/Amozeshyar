# AMOZESHYAR
# Author: MMDSANE
# Date: 8 / November / 2024
# """این اسکریپت نمونه کوچک شده سامانه آموزشیار می‌باشد که در یک روز نوشته شده و در حقیقت پروژه دانشگاهی من می‌باشد"""

from random import randint
from datetime import datetime

class Person:
    """قالب اصلی تمامی موجودیت‌های برنامه که تمامی کلاس‌هایی که بصورت موجودیت تعریف شدند مستقیم یا غیر مستقیم از این کلاس ارث‌بری می‌کنند"""
    def __init__(self, name: str = None, family: str = None, Ncode: str = None) -> None:
        self._name = name
        self._family = family
        self._Ncode = Ncode

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, in_name: str):
        if in_name:
            self._name = in_name
        else:
            raise ValueError(f"Invalid Name {in_name!r}")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, in_family: str):
        if in_family:
            self._family = in_family
        else:
            raise ValueError(f"Invalid Family {in_family!r}")

    @property
    def Ncode(self):
        return self._Ncode

    @Ncode.setter
    def Ncode(self, in_Ncode: str):
        if in_Ncode:
            self._Ncode = in_Ncode
        else:
            raise ValueError(f"Invalid Nation Code {in_Ncode!r}")


class ModirGP(Person):
    """این کلاس قابلیت اضافه کردن درس به سیستم را دارا می‌باشد و کلاس شروع کننده عملیات آموزشی است"""
    def __init__(self, name=None, family=None, Ncode=None, Pcode: str = None, List_Dars: list = None) -> None:
        super().__init__(name, family, Ncode)
        self.__Pcode = Pcode  
        self.List_Dars = List_Dars if List_Dars is not None else []
        self.List_Ostad = []  

    @property
    def Pcode(self):
        return self.__Pcode

    @Pcode.setter
    def Pcode(self, in_Pcode):
        if in_Pcode:
            self.__Pcode = in_Pcode
        else:
            raise ValueError(f"Invalid Pcode {in_Pcode!r}")

    def add_dars(self, tedadDars):
        for i in range(tedadDars):
            Dars = input("name dars ra vared konid: ")
            OstadDars = input("name ostad ra vared konid: ")
            self.List_Dars.append({"name_dars": Dars, "name_ostad": OstadDars, "zarfiat": None})
            print("dars ezafe shod!!!")
            
        return self.List_Dars

    def add_ostad(self, name, password):
        self.List_Ostad.append({"name": name, "password": password})
        print(f"Ostad {name} ezafe shod.")


class OSTAD(Person):
    """این موجودیت تحت عنوان استاد صرفا قابلیت ظرفیت دهی به کلاس‌های تعریف شده توسط مدیرگروه می‌باشد"""
    def __init__(self, name=None, family=None, Ncode=None, List_Dars=None) -> None:
        super().__init__(name, family, Ncode)
        self.List_Dars = List_Dars if List_Dars is not None else []

    def zarfiat(self):
        if not self.List_Dars:
            print("list doros khali ast!")
            return

        NameOstad = self.name

        found_lessons = [dars for dars in self.List_Dars if dars["name_ostad"] == NameOstad]

        if not found_lessons:
            print("hich darsi baraye in ostad peyda nashod!!!")
            return

        for dars in found_lessons:
            dars_name = dars["name_dars"]
            capacity = input(f"Lotfan zarfiat dars {dars_name} ra vared konid: ")
            dars["zarfiat"] = capacity
            print(f"zarfiat dars {dars_name} set shod be: {capacity}")
            print('\n')


class EntkhabVahid:
    """بخش اصلی و نسخه کامل عملیات دانشجویی انتخاب واحد که بصورت غیرمستقیم از کلاس‌های مدیرگروه و استاد اطلاعات دریافت می‌کند"""
    def __init__(self, modir_gp: ModirGP, ostad: OSTAD) -> None:
        self.modir_gp = modir_gp
        self.ostad = ostad
        self.selected_courses = {}  # Dictionary baraye zakhire dars-haye entekhab shode va zarfiat anha

    def show_courses(self):
        """Namayesh list dars-ha va ostad-haye mojood dar class modir goroh."""
        if not self.modir_gp.List_Dars:
            print("Hich darsi mojood nist!")
            return

        print("List dars-ha:")
        for dars in self.modir_gp.List_Dars:
            dars_name = dars["name_dars"]
            ostad_name = dars["name_ostad"]
            zarfiat = dars["zarfiat"] if dars["zarfiat"] else "Namashkhas"
            print(f"Dars: {dars_name}, Ostad: {ostad_name}, Zarfiat: {zarfiat}")

    def select_course(self, dars_name: str):
        """Entekhab dars tavasot daneshjo va barresi zarfiat an"""
        if dars_name in self.selected_courses:
            print(f"Dars {dars_name} ghablan entekhab shode ast!")
            return

        # Peida kardan dars mored nazar dar list modir goroh
        selected_dars = next((dars for dars in self.modir_gp.List_Dars if dars["name_dars"] == dars_name), None)
        
        if not selected_dars:
            print(f"Dars {dars_name} dar list dars-ha mojood nist.")
            return

        # Barresi zarfiat dars
        if selected_dars["zarfiat"] and int(selected_dars["zarfiat"]) > 0:
            self.selected_courses[dars_name] = selected_dars["name_ostad"]
            # Kahesh zarfiat dars dar list modir goroh
            selected_dars["zarfiat"] = str(int(selected_dars["zarfiat"]) - 1)
            text = f"Dars {dars_name} ba movafaghiat entekhab shod. Zarfiat baghi mande: {selected_dars['zarfiat']}\n"
            print(text)
            current_time = datetime.now()
            print("Zaman Entekhab dars:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
            text2= current_time.strftime("%Y-%m-%d %H:%M:%S")
            with open("EntekhabVahed.txt", "w", encoding="utf-8") as file:
                file.write(text)  # نوشتن متن در فایل
                file.write(text2)

        else:
            print("Zarfiat dars por shode ast!")

    def remove_course(self, dars_name: str):
        """Hazf dars entekhab shode az list entekhab-ha"""
        if dars_name in self.selected_courses:
            del self.selected_courses[dars_name]
            print(f"Dars {dars_name} az list entekhab-shode-ha hazf shod.")

            # Afzayesh zarfiat dars dar list modir goroh
            for dars in self.modir_gp.List_Dars:
                if dars["name_dars"] == dars_name:
                    dars["zarfiat"] = str(int(dars["zarfiat"]) + 1) if dars["zarfiat"] else "1"
                    print(f"Zarfiat dars {dars_name} bazgardande shod be: {dars['zarfiat']}")
                    break
        else:
            print(f"Dars {dars_name} dar list entekhab-shode-ha mojood nist!")

    def restore_capacity(self, dars_name: str):
        """Bazgardandan zarfiat dars be meghdar avvali dar soorat niyaz"""
        if dars_name in self.selected_courses:
            capacity = self.selected_courses[dars_name]
            print(f"Zarfiat baraye {dars_name} bazgardande shod be: {capacity}")
        else:
            print(f"Dars {dars_name} dar list entekhab-shode-ha mojood nist!")


class Daneshjo(Person):
    """هر دانشجو اینجا ساخته شده و پس از ایجاد سرترم عملیات دانشجویی را انجام میدهد"""
    def __init__(self, name=None, family=None, Ncode=None, ShomareDaneshJo: str = None) -> None:
        super().__init__(name, family, Ncode)
        self.__ShomareDaneshJo = ShomareDaneshJo

    @property
    def ShomareDaneshJo(self):
        return self.__ShomareDaneshJo
    
    @ShomareDaneshJo.setter
    def ShomareDaneshJo(self, in_ShomareDaneshJo):
        if in_ShomareDaneshJo:
            self.__ShomareDaneshJo = in_ShomareDaneshJo
        else:
            raise ValueError(f"Invalid ShomareDaneshJo {in_ShomareDaneshJo!r}")
        
    def ShowInfo(self):
        print(f"\nDaneshjo\nname: {self.name}\nfamily: {self.family}\nNational code: {self.Ncode}\nShomareDaneshJoE: {self.ShomareDaneshJo}")

    def SarTerm(self):
        rand = randint(100000, 900000)
        print(f"! Code Ejad sarterm shoma {rand} mibashad !")
        while True:
            sartermrand = input("Code Ejad sarterm khod ra vared konid: ")
            if sartermrand.isdigit():
                sartermrand = int(sartermrand)
                break
            else:
                print("Invalid input")
    
        if sartermrand == rand:
            print("Sar Term tavasot daneshjo ejad shod!")
        
    def ENTEKHABVAHED(self):
        entkhab_vahid = EntkhabVahid(modir, ostad)

        x = input("baraye Entekhab vahed Adad -1- va baraye hazf dars Adad -2- va braye khoroj adad 0 ra vared konid: ")
        while(x != '0'):
            if x=='1':
                # نمایش درس‌ها (با ظرفیت اولیه)
                print("\n list doros EntkhabVahid:")
                entkhab_vahid.show_courses()

                # انتخاب یک درس توسط دانشجو
                print("\n entekhab dars:")
                entkhab_vahid.select_course(dars_name=input("dars ra entekhab konid: "))

                # دوباره نمایش لیست درس‌ها برای بررسی ظرفیت تغییر کرده
                print("\n list dars baad az entekhab vahed: ")
                entkhab_vahid.show_courses()
                print("\n")
                x = input("baraye Entekhab vahed Adad -1- va baraye hazf dars Adad -2- va braye khoroj adad 0 ra vared konid: ")

            elif x=='2':
                print("\nhazf dars:")
                entkhab_vahid.remove_course(dars_name=input("kodam dars ra mikhahid hazf konid: "))

                # نمایش لیست درس‌ها بعد از حذف برای بررسی ظرفیت بازگردانی شده
                print("\n list dars baad az hazf: ")
                entkhab_vahid.show_courses()    
                print("\n")
                x = input("baraye Entekhab vahed Adad -1- va baraye hazf dars Adad -2- va braye khoroj adad 0 ra vared konid: ")
            
            else:
                print("Gozine Eshtebah")
                print("\n")
                x = input("baraye Entekhab vahed Adad -1- va baraye hazf dars Adad -2- va braye khoroj adad 0 ra vared konid: ")
            
        return



try:
    if __name__ == '__main__':
        print("! Be System Amozeshyar Khosh Amadid !\n\n")
        print("Lotfan Amaliat Amozeshi khod ra Entekhab konid:\n1) Amaliat Amozeshi GP\n2) Amaliat Amozeshi DaneshjoE\n3) EXIT")
        EntekhabAmaliat = input("Amaliat Amozeshi ra Entekhab konid: ")
        while True:
            if EntekhabAmaliat == '1':

                modir = ModirGP()
                name_ModirGP = input("name ModirGP: ")
                family_ModirGP = input("family ModirGP: ")
                Ncode_ModirGP = input("National code ModirGP: ")
                Pcode_ModirGP = input("Personali code ModirGP: ")
                while True:
                    add_dars_ModirGP = input("Che tedad dars mikhahid ezaf konid? : ")
                    if add_dars_ModirGP.isdigit():
                        add_dars_ModirGP = int(add_dars_ModirGP)
                        break
                    else:
                        print("Invalid input")

                modir.name = name_ModirGP
                modir.family = family_ModirGP
                modir.Ncode = Ncode_ModirGP
                modir.Pcode = Pcode_ModirGP
                modir.add_dars(add_dars_ModirGP)
                print("list doros ersE shode tavasot ModirGP:", modir.List_Dars)
                print('\n')

                print("Baraye vorod be amaliat Zarfiat dehi adad 1 ra vared konid")
                print("! Vaghti tamami doros Zarfiat Anha vared shod adad 0 ra vared karde ta az amaliat ostad kharej shavid !")
                os1 = input("Amaliat: ")

                while(os1 != '0'):
                    name_ostad = input("Name ostad dars ra vared konid: ")
                    ostad = OSTAD(name=name_ostad, List_Dars=modir.List_Dars)
                    ostad.zarfiat()
                    print("Zarfiat Dehi movafaghiat Amiz bood\n")
                    os1 = input("Amaliat: ")
                    print("\n")

                print("Lotfan Amaliat Amozeshi khod ra Entekhab konid:\n1) Amaliat Amozeshi GP\n2) Amaliat Amozeshi DaneshjoE\n3) EXIT")
                EntekhabAmaliat = input("Amaliat Amozeshi ra Entekhab konid: ")

            elif EntekhabAmaliat == '2':
                list_daneshjoha = ["400163", "401163", "402163", "16399", "16398", "16397"]

                name_Daneshjo = input("name Daneshjo: ")
                family_Daneshjo = input("family Daneshjo: ")
                Ncode_Daneshjo = input("National code Daneshjo: ")
                Daneshjocode= input("Shomare DaneshjoE: ")

                if Daneshjocode in list_daneshjoha:
                    Daneshjo1 = Daneshjo(name_Daneshjo, family_Daneshjo, Ncode_Daneshjo, Daneshjocode)
                    print("\n")
                    Daneshjo1.ShowInfo()
                    print("\n")
                    Daneshjo1.SarTerm()
                    print("\n")
                    print("Baraye vorod be amaliat Entekhab vahed adad 1 ra vared konid va baraye Khoroj adad 0")
                    da1 = input("Amaliat: ")
                    while(da1 != 0):
                        Daneshjo1.ENTEKHABVAHED()
                        print("Amaliat Movafaghiat amiz bood!")
                        da1 = input("Amaliat: ")
                        print("\n")
                print("Lotfan Amaliat Amozeshi khod ra Entekhab konid:\n1) Amaliat Amozeshi GP\n2) Amaliat Amozeshi DaneshjoE\n3) EXIT")
                EntekhabAmaliat = input("Amaliat Amozeshi ra Entekhab konid: ")
            
            elif EntekhabAmaliat == '3':
                break

            else:
                print("Invalid input")
                print("\n")
                print("Lotfan Amaliat Amozeshi khod ra Entekhab konid:\n1) Amaliat Amozeshi GP\n2) Amaliat Amozeshi DaneshjoE\n3) EXIT")
                EntekhabAmaliat = input("Amaliat Amozeshi ra Entekhab konid: ")
except:
    print("Some ERROR ditected")
                    

# # تست کد
# modir = ModirGP()
# modir.name = "amin"
# modir.family = "eskandari"
# modir.Ncode = "228"
# modir.Pcode = "iau@228"
# modir.add_dars(2)
# print("list doros ersE shode tavasot ModirGP:", modir.List_Dars)
# # اضافه کردن استاد به لیست درس‌ها
# ostad = OSTAD(name="e", List_Dars=modir.List_Dars)

# # فراخوانی متد Zarfiat برای تعریف ظرفیت درس
# ostad.zarfiat()
# Daneshjo1 = Daneshjo("samin", "Dinparvar", "228", "401163")
# Daneshjo1.ShowInfo()
# Daneshjo1.ENTEKHABVAHED()

# FINISH