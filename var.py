import os,sys, string, colorama
from pyfiglet import Figlet

class app:
# NOMBRE Y VERCION DEL KRAKER
    nombre =("KRAKER")
    try:
        kraker_hi = Figlet(font='ansi_shadow', justify="center")
    except:
        kraker_hi = Figlet(font='whimsy', justify="center")
    vol = ("0.0.1")
    description_ = ("""
                    !!!GENERADOR_DE_DICCIONARIOS_FOR_FUERZA_BRUTA¡¡¡ XD
    ------------------------------------------------------------------------------------
    KRAKER en su (version 0.0.1)CLI, cuenta con 3 modos de ejecucion + un descompresor 
            con una amplia flexibilidad para la Generacion de diccionarios
                        de Krackeo!!! TOTALMENTE EN ESPAÑOL!!!
                            ** Echo por: Xibalba_Z **
                    ----------------------------------------------
""")
    epilogo =("********* Mexico *********").center(85, " ")
# AYUDA DE COMANDOS
    m_standar_ =("combina 3 tipos de caracteres")
    m_5050_ = ("combina de 1 a 4 tipos de caracteres")
    m_manual_ = ("especifica 1 a 1 los caracteres mas palabra clave")
    m_desnprx_ = ("descomprime el Kraker y mas...")
# DESCRIPCIONES DE GRUPOS_
    standar_ = ("Modo standar", "combinacion minus.. mayu.. y nume..(recomendado \"auditorias\" wifi)")
    _5050_  = ("Modo 5050", "Comandos standar + eleccion de 1 a 4 tipos de caracteres a combinar")
    manual_ = ("Modo_manual_", "Comandos standar + caracters a utilizar + incercion pocicional de palabras clave")
    decompres_ = ("Descompresor","descomprime el kraker y mas...") 
# AYUDA DE ARGUMENTOS
    nombre_ =  ("Nombre_del_Dict_Kraker(\"opcional\") por defecto kraker_pwned(.txt, .zip)")
    longitud_ = ("Longitud_de_la_Key")
    tamaño_ = ("Tamaño_ del_Dict_Kraker")
    ruta_ = ("Especifica_la_ruta_for_save(opcional, se guardara en el directoria actual)")
    combi_= ("Especifica  los caracteres a combinar Mayusculas, minusculas, numeros, especiales")
    caracteres = ("espesifica 1 a 1 los caracteres a ocupar min.. Mayu.. nume.. espe..")
    key_ =("introduce la plalabra clave a ocupar")
    nu_ = ("introduce combinacion especifica de numeros")
    index_ = ("introduce el numero del index de la palabra clave, numeros o carcteres especiales")
    m_rep_=("Rango  de repeticiones por palabra(-rE <caracter,mini,<opcional[maximo]> ej: [-rE x13 i25 B23]))")
    zip_ = ("elige el formato de comprecion")
    decoprx_file_ = ("Ingresa la ruta y nombre(´s) de Archivo(´s)")
    permuta_ = ("ingresa un archivo .txt con una lista de palabras para combinar")
    exclucion_ = ("exclulle los caracteres especificado en la generacion del kraker")
# OPCIONES 
    modos_c = ["standar","5050","manual"]
    c_mo_5050 = ["mayus","minus","numer","espec"] 
    zip_format_ = [".zip",".gzip",".bz2",".tar.gz",".lzma", ".xz"]
# VALORES POR DEFECTO
    nom_def =("kraker_pwned.txt")
    path_ = os.getcwd()

class estandar_:
    standar = string.ascii_lowercase + string.ascii_uppercase + string.digits+string.digits


class _5050_:
    l_5050 = {}
    l_5050 ["mayus"] = string.ascii_uppercase
    l_5050 ["minus"] = string.ascii_lowercase
    l_5050 ["numer"] = string.digits
    l_5050 ["espec"] = ("°|¬!#$%&/=?~*+><^")


class _manual_:
    pass
class barra_:
    formato_=(colorama.Fore.YELLOW+"{l_bar}{bar}"+colorama.Fore.BLUE+"{n_fmt}/{total} | {remaining}")
    title_ = ("G-KRAKER")
    t_extrax = ("EX-KRAKER")
    color =("blue")


class compresor:
    msg_zip = ("comprimiendo...")

class fin_:
    msg_ = (colorama.Fore.GREEN+"¡¡¡EL ARCHIVO ESTA LISTO!!!: ")
    ruta_G = ("Almacenado en: ")


class errors_:
    err_l_ =("la longitud de (-k) + (-ca) es = ó mayor que (-l)")
    err_p_ = ("el numero de (-p) no puede ser = ó < a 0")
    err_param_ma_ =("ocurrio un error de ejecución")
    err_permiso = ("!El permiso en la ruta fue denegado checa tu configuracion para guardar¡")
    err_borrado =("!no se puede eliminar el archivo intente manualmente¡")
    err_decoprex = ("error al descomprimir")