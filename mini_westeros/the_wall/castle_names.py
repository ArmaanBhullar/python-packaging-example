if (__name__=='__main__'):
    import os
    #Read all the castles and print them
    DATA_PATH = "." #To be loaded from pkg_utils
    with open(os.path.join(DATA_PATH, 'hardhome/the_castles.txt')) as fp:
        print(fp.read())

