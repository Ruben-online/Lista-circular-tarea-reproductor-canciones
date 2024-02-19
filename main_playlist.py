from circular_list import CircularList

circular_list = CircularList()

while True:
    print("Gestor de musica\n")
    print("1. Agregar cancion")
    print("2. Eliminar cancion")
    print("3. Reproducir la siguiente cancion")
    print("4. Reproducir la cancion anterior")
    print("5. Mostrar la lista de reproduccion")
    print("6. Salir ")

    music_managment = input("Ingrese una opcion (1-6): ")

    if music_managment == "1":
        add_song = input("Ingrese la cancion que desea agregar a la playlist: ")
        circular_list.add_element(add_song)

    elif music_managment == "2":
        delete_song = input("Ingrese la cancion que desea eliminar: ")
        circular_list.delete_element(delete_song)

    elif music_managment == "3":
        circular_list.next_song()

    elif music_managment == "4":
        circular_list.prev_song()

    elif music_managment == "5":
        print("Playlist")
        circular_list.print_list()

    elif music_managment == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Seleccione una opcion valida")