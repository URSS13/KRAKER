import os, sys, tqdm
import zipfile,gzip,lzma, bz2, tarfile
import var,complementos


class  krak_zip():
    def zip_(kraker_):
        print(var.compresor.msg_zip)
        with zipfile.ZipFile("{}".format(kraker_.nombre+kraker_.zip), "w", compression=zipfile.ZIP_BZIP2,
        compresslevel=(9)) as kraker_zip:
            kraker_zip.write("{1}".format(kraker_.ruta,kraker_.nombre))
        try:
            os.remove(str(kraker_.ruta)+"\\"+kraker_.nombre)
            complementos.kraker_fin_.fin_(kraker_)
        except:
            complementos.kraker_fin_.fin_(kraker_)
            print(var.errors_.err_borrado)
            sys.exit()

    def tar_(kraker_):
        print(var.compresor.msg_zip)
        with tarfile.open("{}".format(kraker_.nombre+kraker_.zip),"w:gz") as kraker_tar:
            kraker_tar.add("{1}".format(kraker_.ruta,kraker_.nombre))
            kraker_tar.close()
        try:
            os.remove(str(kraker_.ruta)+"\\"+kraker_.nombre)
            complementos.kraker_fin_.fin_(kraker_)
        except:
            complementos.kraker_fin_.fin_(kraker_)
            print(var.errors_.err_borrado)
            sys.exit()

    def gzip_(kraker_):
        print(var.compresor.msg_zip)
        with open("{1}".format(kraker_.ruta,kraker_.nombre),"rb") as krakers:
            with gzip.open("{}".format(kraker_.nombre+kraker_.zip), "wb")as kraker_gzip:
                kraker_gzip.writelines(krakers)
        try:
            os.remove(str(kraker_.ruta)+"\\"+kraker_.nombre)
            complementos.kraker_fin_.fin_(kraker_)
        except:
            complementos.kraker_fin_.fin_(kraker_)
            print(var.errors_.err_borrado)
            sys.exit()

    def bz2_(kraker_):
        print(var.compresor.msg_zip)
        with open("{1}".format(kraker_.ruta,kraker_.nombre),"rb") as kraker:
            with bz2.BZ2File("{}".format(kraker_.nombre+kraker_.zip),"wb", compresslevel=(9)) as kraker_bz2_:
                kraker_bz2_.writelines(kraker)
        try:
            os.remove(str(kraker_.ruta)+"\\"+kraker_.nombre)
            complementos.kraker_fin_.fin_(kraker_)
        except:
            complementos.kraker_fin_.fin_(kraker_)
            print(var.errors_.err_borrado)
            sys.exit()

    def xz_lzma_(kraker_):
        print(var.compresor.msg_zip)
        with open("{1}".format(kraker_.ruta,kraker_.nombre),"rb") as kraker:
            with lzma.open("{1}".format(kraker_.ruta,kraker_.nombre+kraker_.zip),"wb", preset=(9)) as kraker_lzma_:
                kraker_lzma_.write(kraker.read())
        try:
            os.remove(str(kraker_.ruta)+"\\"+kraker_.nombre)
            complementos.kraker_fin_.fin_(kraker_)
        except:
            complementos.kraker_fin_.fin_(kraker_)
            print(var.errors_.err_borrado)
            sys.exit()

class zip_control_():
    def control_(kraker_):
        if kraker_.zip == (".zip"):
            krak_zip.zip_(kraker_)
        elif kraker_.zip == (".tar.gz"):
            krak_zip.tar_(kraker_)
        elif kraker_.zip == (".gzip"):
            krak_zip.gzip_(kraker_)
        elif kraker_.zip == (".bz2"):
            krak_zip.bz2_(kraker_)
        elif kraker_.zip  == (".xz") or (".lzma"):
            krak_zip.xz_lzma_(kraker_)
        else:
            Exception()


class extrae_kraker_():
    def bz2_f(r, file_):
        n = str(os.path.basename(file_)).split(".")
        del(n[-1])
        nombre = ".".join(n)
        ruta =str(r)+"\\"+nombre
        with open("{0}".format(file_),"rb") as ex_krak_:
            ex =ex_krak_.read()
            krak = bz2.decompress(ex)
            with open("{0}".format(ruta),"wb") as kraker:
                kraker.write(krak)
    def gzip_f(r,file_):
        n = str(os.path.basename(file_)).split(".")
        del(n[-1])
        nombre = ".".join(n)
        ruta =str(r)+"\\"+nombre
        with open("{0}".format(file_),"rb") as ex_krak_:
            ex =ex_krak_.read()
            krak = gzip.decompress(ex)
            with open("{0}".format(ruta),"wb") as kraker:
                kraker.write(krak)
    def xz_lzma_f(r,file_):
        n = str(os.path.basename(file_)).split(".")
        del(n[-1])
        nombre = ".".join(n)
        with lzma.open("{0}".format(file_),"rb") as kraker_lzma_:
            with open("{1}".format(r,nombre),"wb") as kraker:
                kraker.write(kraker_lzma_.read())


class extrae_krak_():
    def extraccion_(kraker_):
        for file_ in tqdm.tqdm(kraker_.file,colour=var.barra_.color,desc=var.barra_.t_extrax,
                bar_format=var.barra_.formato_):
            tipo = os.path.splitext(file_)[1]
            r = os.path.dirname(file_)
            if tipo == (".zip"):
                try:
                    with zipfile.ZipFile("{0}".format(file_), "r") as ex_krak_:
                        ex_krak_.extractall(r)
                except:
                    print("\n",var.errors_.err_decoprex,file_)
            elif tipo == (".gz"):
                try:
                    with tarfile.open("{0}".format(file_), "r:gz") as ex_krak_:
                        ex_krak_.extractall(r)
                except:
                    print("\n",var.errors_.err_decoprex,file_)
            elif tipo == (".gzip"):
                try:
                    extrae_kraker_.gzip_f(r, file_)
                except:
                    print("\n",var.errors_.err_decoprex,file_)
            elif tipo == (".bz2"):
                try:
                    extrae_kraker_.bz2_f(r,file_)
                except:
                    print("\n",var.errors_.err_decoprex,file_)
            elif tipo == (".xz") or (".lzma"):
                extrae_kraker_.xz_lzma_f(r,file_)
            else:
                print("\n",var.errors_.err_decoprex,file_)
                continue
        print("Extraccion Finalizada".center(100," "))