import os

menu = 0
menu2 = 0
menu3 = 0
producto=0

empresa= "Shushy Rolls"
rolls1="Pikachiu Roll"
rolls1_precio=4500
rolls1_pedidos=0
cantidad_de_rolls1= 0
total_de_rolls1= 0 

rolls2="Otaku Roll"
rolls2_precio=5000
rolls2_pedidos=0
cantidad_de_rolls2= 0
total_de_rolls2= 0

rolls3="Pulpo Venenoso Roll"
rolls3_precio=5200
rolls3_pedidos=0
cantidad_de_rolls3= 0
total_de_rolls3= 0

rolls4="Anguila Eléctrica Roll"
rolls4_precio= 4800
rolls4_pedidos=0
cantidad_de_rolls4= 0
total_de_rolls4= 0

descuento_de_10 = 0.1
Codigo_de_descuento=("soyotaku")

while menu != 3:
    print("bienvendido a ", empresa)
    print("Ingrese su usuario")
    user=input("")
    os.system('cls')
    while menu2 != 3:
        print("Tipo de comidas")
        print("1.Rolls")
        print("2.Consultar Boleta")
        print("3.Eliminar Producto")
        print("4.Salir")
        menu3= int(input())
        while menu3 == 3 :
            print("Productos para eliminar")
            print("1.",rolls1,"\t" )
            print("2.",rolls2,"\t" )
            print("3.",rolls3,"\t")
            print("4.",rolls4,"\t")











        while menu3 == 1:
            os.system('cls')
            print("Tipos de Rolls")
            print("1.",rolls1,"\t", f"{rolls1_precio}")
            print("2.",rolls2,"\t", f"{rolls2_precio}")
            print("3.",rolls3,"\t", f"{rolls3_precio}")
            print("4.",rolls4,"\t", f"{rolls4_precio}")
            print("5.Salir")
            print("Selecione el tipo de rolls que pedira")
            producto=int(input(""))

            while producto == 1:
                print("Ingrese a la cantidad que desea comprar")
                cantidad_de_rolls1 =int(input(""))
                print("Esta seguro de comprar este producto?")
                print("ingrese la opcion correspondiente (Si:1/No:2)")
                Asegurar_compra = int(input(""))
                if Asegurar_compra == 1:
                    while Asegurar_compra == 1:
                        print("Usted ha comprado: ", rolls1,)
                        print("Cantidad de pedida: ",cantidad_de_rolls1 )
                        print("Valor unitario: $", f"{rolls1_precio}")
                        print("Valor total: $",(cantidad_de_rolls1 * rolls1_precio ))
                        print("Sera Agregado a su boleta")
                        print("Desea comprar Nuevamente lo mismo?(Si:1/no:2)")
                        Asegurar_compra = int(input(""))
                        if Asegurar_compra == 1:
                            Asegurar_compra=0
                            producto = 1
                            os.system('cls')
                        else:
                            print("Volviendo al menu de rolls")
                            Asegurar_compra = 0
                            producto= 0
                            menu3=0
                else:
                    print("Volviendo al menu de rolls")
                    producto= 0
                    menu3=1
            
            while producto == 2:
                print("Ingrese a la cantidad que desea comprar")
                cantidad_de_rolls2 =int(input(""))
                print("Esta seguro de comprar este producto?")
                print("ingrese la opcion correspondiente (Si:1/No:2)")
                Asegurar_compra = int(input(""))
                if Asegurar_compra == 1:
                    while Asegurar_compra == 1:
                        print("Usted ha comprado: ", rolls2,)
                        print("Cantidad de pedida: ",cantidad_de_rolls2 )
                        print("Valor unitario: $", f"{rolls2_precio}")
                        print("Valor total: $",(cantidad_de_rolls2 * rolls2_precio ))
                        total_de_rolls2 += cantidad_de_rolls2
                        print("Sera Agregado a su boleta")
                        print("Desea comprar Nuevamente lo mismo?(Si:1/no:2)")
                        Asegurar_compra = int(input(""))
                        if Asegurar_compra == 1:
                            Asegurar_compra=0
                            producto = 2
                            os.system('cls')
                        else:
                            print("Volviendo al menu de rolls")
                            Asegurar_compra = 0
                            producto= 0
                            menu3=0
                else:
                    print("Volviendo al menu de rolls")
                    producto= 0
                    menu3=1
            
            while producto == 3:
                print("Ingrese a la cantidad que desea comprar")
                cantidad_de_rolls3 =int(input(""))
                print("Esta seguro de comprar este producto?")
                print("ingrese la opcion correspondiente (Si:1/No:2)")
                Asegurar_compra = int(input(""))
                if Asegurar_compra == 1:
                    while Asegurar_compra == 1:
                        print("Usted ha comprado: ", rolls3,)
                        print("Cantidad de pedida: ",cantidad_de_rolls3 )
                        print("Valor unitario: $", f"{rolls3_precio}")
                        print("Valor total: $",(cantidad_de_rolls3 * rolls3_precio ))
                        total_de_rolls3 += cantidad_de_rolls3
                        print("Sera Agregado a su boleta")
                        print("Desea comprar Nuevamente lo mismo?(Si:1/no:2)")
                        Asegurar_compra = int(input(""))
                        if Asegurar_compra == 1:
                            Asegurar_compra=0
                            producto = 3
                            os.system('cls')
                        else:
                            print("Volviendo al menu de rolls")
                            Asegurar_compra = 0
                            producto= 0
                            menu3=0
                else:
                    print("Volviendo al menu de rolls")
                    producto= 0
                    menu3=1

            while producto == 4:
                print("Ingrese a la cantidad que desea comprar")
                cantidad_de_rolls3 =int(input(""))
                print("Esta seguro de comprar este producto?")
                print("ingrese la opcion correspondiente (Si:1/No:2)")
                Asegurar_compra = int(input(""))
                if Asegurar_compra == 1:
                    while Asegurar_compra == 1:
                        print("Usted ha comprado: ", rolls4,)
                        print("Cantidad de pedida: ",cantidad_de_rolls4 )
                        print("Valor unitario: $", f"{rolls4_precio}")
                        print("Valor total: $",(cantidad_de_rolls4 * rolls4_precio ))
                        total_de_rolls4 += cantidad_de_rolls4
                        print("Sera Agregado a su boleta")
                        print("Desea comprar Nuevamente lo mismo?(Si:1/no:2)")
                        Asegurar_compra = int(input(""))
                        if Asegurar_compra == 1:
                            Asegurar_compra=0
                            producto = 4
                            os.system('cls')
                        else:
                            print("Volviendo al menu de rolls")
                            Asegurar_compra = 0
                            producto= 0
                            menu3=0
                else:
                    print("Volviendo al menu de rolls")
                    producto= 0
                    menu3=1           