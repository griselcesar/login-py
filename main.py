#Importamos la biblioteca para crear GUI (Interfaces de Usuarios Gráficas)
from tkinter import * #Esta es la forma más moderna de importar TKinter
#Importamos las cajas de mensajes de TKinter
from tkinter.messagebox import * #Esto nos va a permitir mostrar cuadros de mensajes al usuario

#Creamos nuestro objeto <root>
root = Tk()
#Configuramos nuestra ventana
root.title("Entrar al Sistema") #titulo
root.iconbitmap("./assets/icons/favicon.ico") #icono
root.resizable(0,0) #No permitir cambiar el tamaño de la ventana
root.geometry("300x320") #Establecer el tamaño de la ventana

############################### Lógica ###############################
#declaramos un función para manejar los eventos del formulario
def verificar_usuario():
  user = user_name.get() #almacenamos el nombre
  pswd = user_pswd.get() #almacenamos la contraseña
  
  #verificamos que halla un usuario
  if not user:
    showwarning(title="Usuario Requerido",
                message="Debe introducir un usuario")
    #mostramos un mensaje para indicar el error
    return #detenemos la ejecución de la función
  
  #verificamos que halla una contraseña
  if not pswd:
    #mostramos un mensaje para indicar el error
    showwarning(title="Contraseña Requerida",
                message="Debe introducir su contraseña")
    return #detenemos la ejecución de la función
  
  #comprobamos la existencia del usuario en la base de datos
  if user == "admin" and pswd == "admin":
    #mostramos un mensaje de sesión exitosa
    showinfo(title="Sesión Iniciada",
            message="Bienvenido administrador")
    #limpiamos los input
    user_name.delete(0,END)
    user_pswd.delete(0,END)
    #Colocamos el foco en el input usuario
    user_name.focus()
  
  else:
    showerror(title="Error al iniciar sesión",
              message="Usuario y Contraseña incorrectos")
    #mostramos un mensaje de error de sesión

####################### Diseñamos la GUI ########################

logo = PhotoImage(file='./assets/img/logo.png') #Cargamos una imagen para el login

#Creamos un Frame para organizar los widget
main_frame = LabelFrame(root,
                        text="Iniciar Sesión",
                        font="Roboto 12 bold",
                        width=280, padx=10, pady=10,
                        labelanchor='n') #Centramos el titulo

#empaquetamos el widget
main_frame.pack(padx=50, pady=25,ipadx=30)

#Usamos la imagen en una Etiqueta y ajustamos
Label(main_frame,image=logo,width=64,height=64).pack()

#creamos la etiqueta y el input para la variable usuario
Label(main_frame,text="Usuario",font="Roboto 10 bold").pack()#etiqueta
user_name = Entry(main_frame,justify="center")
user_name.pack(pady=5) #empaquetamos el input

#creamos la etiqueta y el input para la variable contraseña
Label(main_frame,text="Contraseña",font="Roboto 10 bold").pack()#etiqueta
user_pswd = Entry(main_frame,justify="center",show="*")
user_pswd.pack(pady=5) #empaquetamos el input

#Creamos el botón y le asignamos la función para manejar la sesión
Button(main_frame,text="Entrar",command=verificar_usuario,bg="#fc0",font="Roboto 10 bold").pack(ipadx=15,ipady=5)
Label(main_frame,text="Diseñado por CAGM",font="Roboto 9").pack() #Esta línea la puedes eliminar


mainloop()