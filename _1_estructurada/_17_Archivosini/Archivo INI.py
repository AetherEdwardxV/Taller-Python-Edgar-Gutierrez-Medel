import configparser
import sys

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    #Verifica las secciones y claves que existan
    if ('Maximus' in config and
            'basedatos' in config['Maximus'] and
            'usuario' in config['Maximus'] and
            'contrasena' in config['Maximus']):

        bd = config['Maximus']['basedatos']
        user = config['Maximus']['usuario']
        password = config['Maximus']['contrasena']


    print(bd,user,password)