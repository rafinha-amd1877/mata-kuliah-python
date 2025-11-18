def argumen_tanpa_definisi(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)
    print(args)
    print(kwargs)
        
argumen_tanpa_definisi(10,20,30,40, name="azello", asep="nama")