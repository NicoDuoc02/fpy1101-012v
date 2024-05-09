import os

menu = 0
menu2 = 0
menu3 = 0
producto=0
total_de_productos=0

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
    
    while menu2 != 5:
        print("Tipo de comidas")
        print("1.Rolls")
        print("2.Consultar Boleta")
        print("3.Eliminar Producto")
        print("4.pagar")
        print("5.salir")
        try:
            menu3= int(input())
            if menu3 <= 0 or menu3 >5:
                raise ValueError("")
        except(ValueError,TypeError,SyntaxError):
            print("Ha ingresado un dato invalido")
            continue
        if menu2 == 5 :
                print("saliendo del programa")
                menu=3
                
        while menu3 == 3 :
            os.system('cls')
            print("Productos para eliminar")
            print("1.",rolls1,"\t" )
            print("2.",rolls2,"\t" )
            print("3.",rolls3,"\t")
            print("4.",rolls4,"\t")
            print("5.salir")
            try:
                Eliminar_pedido= int(input())
                if Eliminar_pedido <= 0 or Eliminar_pedido > 5:
                    raise ValueError("")
            except(ValueError,TypeError,SyntaxError):
                print("Ha ingresado un dato invalido")
                continue
            if Eliminar_pedido == 5 :
                print("saliendo del menu de eliminacion")

            if rolls1 > 0:
                while Eliminar_pedido == 1:
                    os.system('cls')
                    print("Usted tiene "f"{total_de_rolls1} del rolls de ", rolls1)
                    print("cuantos desea eliminar")
                    Eliminar_rolls_1=int(input(""))
                    if Eliminar_pedido < rolls1:
                        print("Esta seguro de eliminar este producto?")
                        print("ingrese la opcion correspondiente (Si:1/No:2)")
                        Asegurar_eliminacion = int(input(""))
                        if Asegurar_eliminacion == 1:
                            while Asegurar_eliminacion == 1:
                                total_de_productos -= 1
                                total_de_rolls1 -= Eliminar_rolls_1
                                print("Usted ha eliminado: ", Eliminar_rolls_1,)
                                print("Sera eliminado de su boleta")
                                print("Desea realizar otra operacion ?(Si:1/no:2)")
                                Eliminar_pedido = int(input(""))
                                Asegurar_eliminacion = 0
                        else:
                            print("Volviendo al menu de eliminacion")
                            Eliminar_pedido = 0
                            Asegurar_eliminacion=0
                    else:
                        print("ha ingresado una cantidad mayor a la que pose")
                        Eliminar_pedido = 1
            
            if rolls2 > 0:
                while Eliminar_pedido == 2:
                    os.system('cls')
                    print("Usted tiene "f"{total_de_rolls2} del rolls de ", rolls2)
                    print("cuantos desea eliminar")
                    Eliminar_rolls_2=int(input(""))
                    if Eliminar_pedido < rolls2:
                        print("Esta seguro de eliminar este producto?")
                        print("ingrese la opcion correspondiente (Si:1/No:2)")
                        Asegurar_eliminacion = int(input(""))
                        if Asegurar_eliminacion == 1:
                            while Asegurar_eliminacion == 1:
                                total_de_productos -= 1
                                total_de_rolls2 -= Eliminar_rolls_2
                                print("Usted ha eliminado: ", Eliminar_rolls_2,)
                                print("Sera eliminado de su boleta")
                                print("Desea realizar otra operacion ?(Si:1/no:2)")
                                Eliminar_pedido = int(input(""))
                                Asegurar_eliminacion = 0
                        else:
                            print("Volviendo al menu de eliminacion")
                            Eliminar_pedido = 0
                            Asegurar_eliminacion=0
                    else:
                        print("ha ingresado una cantidad mayor a la que pose")
                        Eliminar_pedido = 2
            
            if rolls3 > 0:
                while Eliminar_pedido == 3:
                    os.system('cls')
                    print("Usted tiene "f"{total_de_rolls3} del rolls de ", rolls3)
                    print("cuantos desea eliminar")
                    Eliminar_rolls_3=int(input(""))
                    if Eliminar_pedido < rolls3:
                        print("Esta seguro de eliminar este producto?")
                        print("ingrese la opcion correspondiente (Si:1/No:2)")
                        Asegurar_eliminacion = int(input(""))
                        if Asegurar_eliminacion == 1:
                            while Asegurar_eliminacion == 1:
                                total_de_productos -= 1
                                total_de_rolls3 -= Eliminar_rolls_3
                                print("Usted ha eliminado: ", Eliminar_rolls_3,)
                                print("Sera eliminado de su boleta")
                                print("Desea realizar otra operacion ?(Si:1/no:2)")
                                Eliminar_pedido = int(input(""))
                                Asegurar_eliminacion = 0
                        else:
                            print("Volviendo al menu de eliminacion")
                            Eliminar_pedido = 0
                            Asegurar_eliminacion=0
                    else:
                        print("ha ingresado una cantidad mayor a la que pose")
                        Eliminar_pedido = 3


            if rolls1 > 0:
                while Eliminar_pedido == 4:
                    os.system('cls')
                    print("Usted tiene "f"{total_de_rolls4} del rolls de ", rolls4)
                    print("cuantos desea eliminar")
                    Eliminar_rolls_4=int(input(""))
                    if Eliminar_pedido < rolls4:
                        print("Esta seguro de eliminar este producto?")
                        print("ingrese la opcion correspondiente (Si:1/No:2)")
                        Asegurar_eliminacion = int(input(""))
                        if Asegurar_eliminacion == 1:
                            while Asegurar_eliminacion == 1:
                                total_de_productos -= 1
                                total_de_rolls4 -= Eliminar_rolls_4
                                print("Usted ha eliminado: ", Eliminar_rolls_4,)
                                print("Sera eliminado de su boleta")
                                print("Desea realizar otra operacion ?(Si:1/no:2)")
                                Eliminar_pedido = int(input(""))
                                Asegurar_eliminacion = 0
                        else:
                            print("Volviendo al menu de eliminacion")
                            Eliminar_pedido = 0
                            Asegurar_eliminacion=0
                    else:
                        print("ha ingresado una cantidad mayor a la que pose")
                        Eliminar_pedido = 4



        while menu3 == 1:
            os.system('cls')
            print("Tipos de Rolls")
            print("1.",rolls1,"\t", f"{rolls1_precio}")
            print("2.",rolls2,"\t", f"{rolls2_precio}")
            print("3.",rolls3,"\t", f"{rolls3_precio}")
            print("4.",rolls4,"\t", f"{rolls4_precio}")
            print("5.Salir")
            print("Selecione el tipo de rolls que pedira")
            try:
                producto= int(input())
                if producto <= 0 or producto >4:
                    raise ValueError("")
            except(ValueError,TypeError,SyntaxError):
                print("Ha ingresado un dato invalido")
                continue
            
            if producto == 5 :
                print("saliendo del menu de producto")

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
                        total_de_productos += 1
                        total_de_rolls1 += cantidad_de_rolls1
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
                        total_de_productos += 1
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
                        total_de_productos += 1
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
                        total_de_productos += 1
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


        while menu3 == 4: 
            print("Tiene algun cupon de descuento(si:1/no:2)")
            codigo_si_o=int(input(""))
            if codigo_si_o == 1:
                print("ingrese el codigo de descuento")
                codigo_user=input("")
                if codigo_user == Codigo_de_descuento:
                    print("se le ha aplicado un el decuento")
                    print("se Impira su boleta")
                    os.system('cls')
                    print("*************************")
                    print("total de productos")
                    print(total_de_productos)
                    print("*************************")
                    print(rolls1, f":{total_de_rolls1}")
                    print(rolls2, f":{total_de_rolls2}")
                    print(rolls3, f":{total_de_rolls3}")
                    print(rolls4, f":{total_de_rolls4}")
                    print("************************")
                    subtotal=((total_de_rolls1*rolls1_precio)+(total_de_rolls2*rolls2_precio)+(total_de_rolls3*rolls3_precio)+(total_de_rolls4*rolls4_pedidos))
                    print("Subtotal:",subtotal)
                    descuento_por_el_codigo=subtotal*descuento_de_10
                    print("descuento por codigo:",descuento_por_el_codigo)
                    total= subtotal - descuento_por_el_codigo
                    print("total:",total)
                    print("**********************************") 
                    print("desea salir del programa(si:1/no:2)")
                    salir=int(input())
                    if salir == 1:
                        print("saliendo")
                        menu3=5
                        menu2=5
                        menu=3
                    else:
                        print("volviendo al menu")
                        menu3=0
                else:
                    print("desea intentalo de nuevo(si:1/no:2")
                    menu3=int(input(""))
                    if menu3 == 1:
                        menu3=4
                    else:
                        menu3=0
                        menu2=0
        else:
            print("se le ha aplicado un el decuento")
            print("se Impira su boleta")
            os.system('cls')
            print("*************************")
            print("total de productos")
            print(total_de_productos)
            print("*************************")
            print(rolls1, f":{total_de_rolls1}")
            print(rolls2, f":{total_de_rolls2}")
            print(rolls3, f":{total_de_rolls3}")
            print(rolls4, f":{total_de_rolls4}")
            print("************************")
            subtotal=((total_de_rolls1*rolls1_precio)+(total_de_rolls2*rolls2_precio)+(total_de_rolls3*rolls3_precio)+(total_de_rolls4*rolls4_pedidos))
            print("Subtotal:",subtotal)
            descuento_por_el_codigo=0
            print("descuento por codigo:",descuento_por_el_codigo)
            total= subtotal - descuento_por_el_codigo
            print("total:",total)
            print("**********************************")
            print("desea salir del programa(si:1/no:2)")
            salir=int(input())
            if salir == 1:
                print("saliendo")
                menu3=5
                menu2=5
                menu=3
            else:
                print("volviendo al menu")
                menu3=0
if menu == 3:
    print("saliendo del programa")