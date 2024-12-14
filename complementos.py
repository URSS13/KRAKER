import os, sys, tqdm, random, colorama, subprocess
import var, krak_zip_


class kraker_fin_():
    def fin_(kraker_):
        if kraker_.zip == None:
            if kraker_.ruta == None:
                print(var.fin_.msg_, var.fin_.ruta_G, var.app.path_+"|",kraker_.nombre)
            else:
                print(var.fin_.msg_, var.fin_.ruta_G,str(kraker_.ruta)+"|"+kraker_.nombre)
        else:
            if kraker_.ruta == None:
                print(var.fin_.msg_, var.fin_.ruta_G, var.app.path_+"|",kraker_.nombre+kraker_.zip)
            else:
                print(var.fin_.msg_, var.fin_.ruta_G,str(kraker_.ruta)+"|"+kraker_.nombre+kraker_.zip)

    def fin_extaer_(r, nombre):
        print(var.fin_.msg_, var.fin_.ruta_G,r,nombre)

class union_5050_():
    def  union_(kraker_):
        tipos_combinacion = list()
        for tipo in kraker_:
            for item in var._5050_.l_5050.keys():
                if tipo == item:
                    tipos_combinacion.append(var._5050_.l_5050[item])
                    caractrz_ = "".join(tipos_combinacion)
        return caractrz_


class comb_manual():
    def m_q_1_(kraker_):
        #ruta = ruta_Krak.ruta_(kraker_)
        ruta = os.chdir(kraker_.ruta)
        l_suma = kraker_.posicion+ len(kraker_.key)
        l_restantes =  kraker_.longitud- l_suma
        rep_ = kraker_.longitud - len(kraker_.key)
        contraseñas = set()
        with open("{1}".format(ruta,kraker_.nombre), "w") as kraker:
            for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,desc=var.barra_.title_,
            bar_format=var.barra_.formato_):
                if kraker_.repite == None:
                    antes_pwd = random.choices(kraker_.caracter, k=kraker_.posicion-1)
                    antes = "".join(antes_pwd)
                    despues_pwd = random.choices(kraker_.caracter,k=l_restantes+1)
                    despues= "".join(despues_pwd)
                    contraseñas = antes+kraker_.key+despues
                    kraker.writelines(contraseñas+"\n")
                else:
                    seleccion = random.choices(kraker_.caracter,k=rep_)
                    combo = list(krak_rep_.rep_(kraker_, seleccion))
                    contra = combo[0]
                    caract = combo[1]
                    vari = combo[2]
                    contra_ = krak_rep_.max_rep_(kraker_,contra, selec_= kraker_.caracter)
                    n = krak_rep_.rec_o(contra_, caract,kraker_,vari)
                    random.shuffle(n)
                    n.insert(kraker_.posicion-1,kraker_.key)
                    contraseña = "".join(n)
                    contraseñas.add(contraseña)
                    if contraseña in contraseñas:
                        kraker.writelines(contraseña+"\n")
            kraker.close()
            if kraker_.zip != None:
                krak_zip_.zip_control_.control_(kraker_)
            else:
                kraker_fin_.fin_(kraker_)

    def i_1_(kraker_):
        contraseñas = set()
        ruta = os.chdir(kraker_.ruta)
        l_restantes =  kraker_.longitud- len(kraker_.key)
        with open("{1}".format(ruta,kraker_.nombre), "w") as kraker:
            for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,desc=var.barra_.title_,
            bar_format=var.barra_.formato_):
                seleccion = random.choices(kraker_.caracter,k=l_restantes)
                if kraker_.repite == None:
                    despues= "".join(seleccion)
                    contraseñas = kraker_.key+despues
                    kraker.writelines(contraseñas+"\n")
                else:
                    combo = list(krak_rep_.rep_(kraker_, seleccion))
                    contra = combo[0]
                    caract = combo[1]
                    vari = combo[2]
                    contra_ = krak_rep_.max_rep_(kraker_,contra, selec_= kraker_.caracter)
                    n = krak_rep_.rec_o(contra_, caract,kraker_,vari)
                    random.shuffle(n)
                    contraseña = kraker_.key+"".join(n)
                    contraseñas.add(contraseña)
                    if contraseña in contraseñas:
                        kraker.writelines(contraseña+"\n")
            kraker.close()
            if kraker_.zip != None:
                krak_zip_.zip_control_.control_(kraker_)
            else:
                kraker_fin_.fin_(kraker_)

    def permuta_(kraker_):
        nombre = os.path.basename(kraker_.permuta)
        ruta = os.chdir(os.path.dirname(kraker_.permuta))
        with open("{1}".format(ruta,nombre),"r")as lista_:
            l1 = list(lista_)
            l =[n.strip() for n in l1]
            with open("{0}".format(kraker_.nombre),"w")as kraker:
                for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,
                desc=var.barra_.title_,bar_format=var.barra_.formato_):
                    seleccion = random.choices(l, k=kraker_.longitud)
                    contraseñas = "".join(seleccion)
                    kraker.writelines(contraseñas+"\n")
                    continue
                kraker.close()
                if kraker_.zip != None:
                    krak_zip_.zip_control_.control_(kraker_)
                else:
                    kraker_fin_.fin_(kraker_)


class ruta_Krak():
    def ruta_(kraker_):
        try:
            subprocess.run("runas /user:Administrador \"python kraker.py\"", shell=True)
            ruta = os.chdir(kraker_.ruta)
            return ruta
        except:
            print(colorama.Fore.RED+var.errors_.err_permiso)
            sys.exit()


class krak_rep_():
    def max_rep_(kraker_, contra, selec_):
        var_lista = list(selec_)
        for caract in kraker_.repite:
            try:
                max_= int(caract[2])
            except:
                max_ = int(caract[1])
            letra_ = caract[0]
            try:
                var_lista.remove(letra_)
            except:
                pass
            if contra.count(letra_)> max_:
                num_ = contra.count(letra_)-max_
                for n in range(num_):
                    contra.remove(letra_)
        if len(contra) < kraker_.longitud:
            faltan_ = kraker_.longitud - len(contra)
            let_ = random.choices(var_lista, k=faltan_)
            contra = contra+let_
        return contra

    def rec_o(contra_, caract,kraker_, vari):
        del(caract[-1])
        caract.insert(0,"pwd !=")
        vari["pwd"]=""
        car = " ".join(caract)
        try:
            if kraker_.key:
                if len(contra_)>(kraker_.longitud-len(kraker_.key)):
                    while len(contra_)>(kraker_.longitud-len(kraker_.key)):
                        for pwd in contra_:
                            vari["pwd"]=pwd
                            if eval(car,vari):
                                contra_.remove(pwd)
                                if len(contra_) == (kraker_.longitud-len(kraker_.key)):
                                    return contra_
        except:
            pass
        if len(contra_) > kraker_.longitud:
            while len(contra_)>kraker_.longitud:
                for pwd in contra_:
                    vari["pwd"]=pwd
                    if eval(car,vari):
                        contra_.remove(pwd)
                        if len(contra_) == kraker_.longitud:
                            return contra_
        else:
            return contra_

    def rep_(kraker_, seleccion):
        caracteres = list()
        vari =dict()
        for tupla_ in kraker_.repite:
            n_rep_ = tupla_[1]
            caracter = tupla_[0]
            vari[caracter]=caracter
            caracteres.append("\""+caracter+"\"")
            caracteres.append("and pwd !=")
            r = seleccion.count(caracter)
            suma_ = int(n_rep_) -r
            if suma_ <=(0):
                continue
            else:
                seleccion.append(caracter*suma_)
                continue
        a = "".join(seleccion)
        c = list(a)
        return c, caracteres, vari


class lib_kraker():
    def libro_(kraker_, libro):
        if kraker_.exclucion != None:
            lib_ = list(libro)
            for caract in kraker_.exclucion:
                for ca in lib_:
                    if caract == ca:
                        lib_.remove(caract)
            libro_ = "".join(lib_)
            return libro_
        else:
            return libro