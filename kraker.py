#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os, sys, random, argparse, tqdm, pathlib,colorama
import var, complementos, krak_zip_


class run_kraker_():
    def standar_(kraker_):
        contraseñas = set()
        ruta = os.chdir(kraker_.ruta)
        libro_ = complementos.lib_kraker.libro_(kraker_, libro=var.estandar_.standar)
        with open("{1}".format(ruta,kraker_.nombre), "w") as kraker:
            while len(contraseñas)< kraker_.tamaño:
                for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,
                desc=var.barra_.title_,bar_format=var.barra_.formato_):
                    seleccion = random.choices(libro_, k=kraker_.longitud)
                    if kraker_.repite == None:
                        contraseña ="".join(seleccion)
                        contraseñas.add(contraseña)
                        if contraseña in contraseñas:
                            kraker.writelines(contraseña+"\n")
                    else:
                        selec_ = var.estandar_.standar
                        combo = list(complementos.krak_rep_.rep_(kraker_, seleccion))
                        contra = combo[0]
                        caract = combo[1]
                        vari = combo[2]
                        contra_ = complementos.krak_rep_.max_rep_(kraker_, contra, selec_)
                        n = complementos.krak_rep_.rec_o(contra_, caract,kraker_,vari)
                        random.shuffle(n)
                        contraseña = "".join(n)
                        contraseñas.add(contraseña)
                        if contraseña in contraseñas:
                            kraker.writelines(contraseña+"\n")
            kraker.close()
            contraseñas.clear()
            if kraker_.zip != None:
                krak_zip_.zip_control_.control_(kraker_)
            else:
                complementos.kraker_fin_.fin_(kraker_)

    def _5050_(kraker_):
        contraseñas = set()
        ruta = os.chdir(kraker_.ruta)
        caractrz_ = complementos.union_5050_.union_(kraker_.combinacion)
        libro_ = complementos.lib_kraker.libro_(kraker_, libro=caractrz_)
        with open("{1}".format(ruta,kraker_.nombre), "w") as kraker:
            while len(contraseñas) < kraker_.tamaño:
                for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,
                desc=var.barra_.title_,bar_format=var.barra_.formato_):
                    seleccion = random.choices(libro_,k=kraker_.longitud)
                    if kraker_.repite == None:
                        contraseña ="".join(seleccion)
                        contraseñas.add(contraseña)
                        if contraseña in contraseñas:
                            kraker.writelines(contraseña+"\n")
                    else:
                        combo = list(complementos.krak_rep_.rep_(kraker_, seleccion))
                        contra = combo[0]
                        caract = combo[1]
                        vari = combo[2]
                        contra_ = complementos.krak_rep_.max_rep_(kraker_,contra, selec_= caractrz_)
                        n = complementos.krak_rep_.rec_o(contra_, caract,kraker_,vari)
                        random.shuffle(n)
                        contraseña = "".join(n)
                        contraseñas.add(contraseña)
                        if contraseña in contraseñas:
                            kraker.writelines(contraseña+"\n")
            kraker.close()
            contraseñas.clear()
            if kraker_.zip != None:
                krak_zip_.zip_control_.control_(kraker_)
            else:
                complementos.kraker_fin_.fin_(kraker_)

    def manual_(kraker_):
        contraseñas = set()
        ruta = os.chdir(kraker_.ruta)
        if kraker_.caracter != None and kraker_.key != None and kraker_.posicion == None and kraker_.permuta == None:
            if len(kraker_.key)<kraker_.longitud:
                esp_rest = kraker_.longitud-int(len(kraker_.key))
                with open("{1}".format(ruta,kraker_.nombre), "w") as kraker:
                    while len(contraseñas) < kraker_.tamaño:
                        for numero in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,
                        desc=var.barra_.title_,bar_format=var.barra_.formato_):
                            seleccion = random.choices(kraker_.caracter,k=esp_rest)
                            if kraker_.repite ==None:
                                seleccion.append(kraker_.key)
                                random.shuffle(seleccion)
                                contraseña = "".join(seleccion)
                                contraseñas.add(contraseña)
                                if contraseña in contraseñas:
                                    kraker.writelines(contraseña+"\n")
                            else:
                                combo = list(complementos.krak_rep_.rep_(kraker_, seleccion))
                                contra = combo[0]
                                caract = combo[1]
                                vari = combo[2]
                                contra_ = complementos.krak_rep_.max_rep_(kraker_,contra, selec_= kraker_.caracter)
                                n = complementos.krak_rep_.rec_o(contra_, caract,kraker_,vari)
                                n.append(kraker_.key)
                                random.shuffle(n)
                                contraseña = "".join(n)
                                contraseñas.add(contraseña)
                                if contraseña in contraseñas:
                                    kraker.writelines(contraseña+"\n")
                    kraker.close()
                    contraseñas.clear()
                    if kraker_.zip != None:
                        krak_zip_.zip_control_.control_(kraker_)
                    else:
                        complementos.kraker_fin_.fin_(kraker_)
            else:
                print(var.errors_.err_l_)
        elif kraker_.caracter != None and kraker_.key != None and kraker_.posicion != None and kraker_.permuta == None:
            if kraker_.posicion>(1):
                    complementos.comb_manual.m_q_1_(kraker_)
            elif kraker_.posicion == (1):
                complementos.comb_manual.i_1_(kraker_)
            else:
                print(var.errors_.err_p_)
        elif kraker_.caracter != None and kraker_.key == None and kraker_.posicion == None and kraker_.permuta == None:
            with open("{1}".format(ruta,kraker_.nombre),"w")as kraker:
                for n in tqdm.tqdm(range(kraker_.tamaño),colour=var.barra_.color,desc=var.barra_.title_,bar_format=var.barra_.formato_):
                    seleccion = random.choices(kraker_.caracter, k=kraker_.longitud)
                    if kraker_.repite == None:
                        contraseñas = "".join(seleccion)
                        kraker.writelines(contraseñas+"\n")
                    else:
                        combo = list(complementos.krak_rep_.rep_(kraker_, seleccion))
                        contra = combo[0]
                        caract = combo[1]
                        vari = combo[2]
                        contra_ = complementos.krak_rep_.max_rep_(kraker_,contra, selec_= kraker_.caracter)
                        n = complementos.krak_rep_.rec_o(contra_, caract,kraker_,vari)
                        random.shuffle(n)
                        contraseña = "".join(n)
                        contraseñas.add(contraseña)
                        if contraseña in contraseñas:
                            kraker.writelines(contraseña+"\n")
                kraker.close()
                if kraker_.zip != None:
                    krak_zip_.zip_control_.control_(kraker_)
                else:
                    complementos.kraker_fin_.fin_(kraker_)
        elif kraker_.caracter == None and kraker_.key == None and kraker_.posicion == None and kraker_.permuta != None:
            complementos.comb_manual.permuta_(kraker_)
        else:
            print(var.errors_.err_param_ma_)


class kraker_control_():
    def control_(kraker_):
        if kraker_.modo == ("standar"):
            run_kraker_.standar_(kraker_)
        elif kraker_.modo == ("5050"):
            run_kraker_._5050_(kraker_)
        elif kraker_.modo == ("manual"):
            run_kraker_.manual_(kraker_)
        elif kraker_.modo == ("extrae"):
            krak_zip_.extrae_krak_.extraccion_(kraker_)

class kraker_app_():
    def kraker_():
        arg_Gen_1_ = argparse.ArgumentParser(add_help=False)
        arg_Gen_1_.add_argument('-eX', "--exclucion", type=list, help=var.app.exclucion_)
        arg_Gen = argparse.ArgumentParser(add_help=False)
        arg_Gen.add_argument('-n', "--nombre", type= str, help=var.app.nombre_, default=var.app.nom_def)
        arg_Gen.add_argument('-l', "--longitud", type= int, help=var.app.longitud_,required=True)
        arg_Gen.add_argument('-t', "--tamaño", type= int, help=var.app.tamaño_, required=True)
        arg_Gen.add_argument('-r', "--ruta", type=pathlib.Path, help=var.app.ruta_, default=var.app.path_)
        arg_Gen.add_argument('-rE',"--repite", type=tuple,nargs=("+"),help=var.app.m_rep_)
        arg_Gen.add_argument('-z',"--zip",type=str, choices=var.app.zip_format_, help=var.app.zip_)

        m_standar = argparse.ArgumentParser(parents=[arg_Gen, arg_Gen_1_],add_help=False)
        standar_g = m_standar.add_argument_group(var.app.standar_[0],var.app.standar_[1])

        m_5050_ = argparse.ArgumentParser(parents=[arg_Gen, arg_Gen_1_],add_help=False)
        _5050_g = m_5050_.add_argument_group(var.app._5050_[0],var.app._5050_[1])
        _5050_g.add_argument("-c","--combinacion", nargs=("+"), type=str, help=var.app.combi_, choices=var.app.c_mo_5050)

        m_manual_ = argparse.ArgumentParser(parents=[arg_Gen], add_help=False)
        manual_g = m_manual_.add_argument_group(var.app.manual_[0],var.app.manual_[1])
        manual_g.add_argument("-ca", "--caracter", type=str, help=var.app.caracteres)
        manual_g.add_argument("-k", "--key", type=str, help=var.app.key_)
        manual_g.add_argument("-p", "--posicion", type=int, help=var.app.index_)
        manual_g.add_argument("-pE", "--permuta", type=pathlib.Path, help=var.app.permuta_)

        m_extractor = argparse.ArgumentParser(add_help=False)
        extractor_g = m_extractor.add_argument_group(var.app.decompres_[0],var.app.decompres_[1])
        extractor_g.add_argument(type=pathlib.Path, nargs=("+"), help=var.app.decoprx_file_, dest=("file"))

        Kraker =  argparse.ArgumentParser(
            prog=(colorama.Fore.GREEN+colorama.Style.BRIGHT+var.app.kraker_hi.renderText("\n"+var.app.nombre)),
            formatter_class=argparse.RawDescriptionHelpFormatter,
            add_help=True,
            description=colorama.Fore.BLUE+colorama.Style.BRIGHT+(var.app.description_),
            epilog=var.app.epilogo
            )
        Kraker.add_argument("--version", action=("version"), version=(var.app.nombre+" "+var.app.vol))
        modos_ = Kraker.add_subparsers(title=("Modos"),help=("Ayuda: <modo> + (-h)"), dest=("modo"), required=True)
        standar_ = modos_.add_parser('standar',parents=[m_standar],help=var.app.m_standar_)
        _5050_ = modos_.add_parser('5050',parents=[m_5050_],help=var.app.m_5050_)
        manual = modos_.add_parser('manual',parents=[m_manual_] ,help=var.app.m_manual_)
        decompresor = modos_.add_parser('extrae',parents=[m_extractor],help=var.app.m_desnprx_)
        kraker_ = Kraker.parse_args()
        kraker_control_.control_(kraker_)


if __name__ == '__main__':
    kraker_app_.kraker_()