PITCH FINAL

Hola, somos 5 estudiantes de Ingenieria en Informatica del ITBA.

- Tomarnos 20 segs para presentarnos y decir nombres y año en la carrera -

EJEMPLO USUARIO

Queremos presentarles a Juli, una chica que está en el ultimo año del secundario. 

Ella tiene una hermana que estudia abogacia pero nunca tuvo ganas de hacerle preguntas sobre el tema.

Como jamás investigó carreras, cree que va a estudiar eso, pero la verdad es que tiene ganas de saber mas, y no esta muy conforme con estudiar abogacia.

En el colegio no le mostraron mucho sobre el mundo universitario, asi que eso no la ayuda mucho. Se acerca el momento de elegir que hacer, pero no tiene idea de que hacer.

Esta plataforma esta hecha para chicos y chicas como Juli, que nunca tuvieron mucha info sobre el tema o estan poco seguros.

IDEA

Nosotros ideamos una plataforma, en donde al momento que Juli ingresa, se le pregunta si esta segura o no de lo que quiere estudiar.

En el caso que dice que no, se le pide que seleccione algunos intereses y gustos de entre una lista, y a traves de un algoritmo de ML, obtener una mejor idea de las carreras a las que se puede llegar a orientar.

Recien ahi puede acceder a nuestro Feed y Wiki. 

El Feed se personaliza segun los intereses mas frecuentes de cada uno. En el mismo puede encontrar posts, videos y lives de los profesionales, pero parte de este contenido esta bloqueado a partir de un sistema de puntajes.

Mientras mas contenido vea, osea mientras mas se informe, mas puntos gana, y mas features desbloquea. De esta forma Juli investiga mas para poder desbloquear hacer preguntas en los live, por ejemplo.

La Wiki tiene informacion util sobre las diferentes carreras, para que Juli se pueda informar sobre todas las carreras al mismo tiempo.

Todos los datos se recuperan con una API hecha en Python.

MENTOR

Al momento de ya saber una carrera, Juli elige la opcion que dice que sabe la carrera, selecciona la carrera que quiere y al posible mentor. Esto le envia una notificacion al sistema de monitoreo para administradores, con la informacion de los perfiles de Juli y el posible Mentor. Para que Junior Achievement apruebe la mentoria.

Esta plataforma es parte de una suite compuesta por la plataforma para alumnos, una plataforma de control para administradores para ver datos en tiempo real, y una plataforma donde pueden ingresar los Profesionales y cargar y postear informacion.

DISEÑO

En terminos de diseño, tuvimos en cuenta que los chicos que usarian la plataforma tienen entre 16 y 19 años, decidimos diseñar algo similar a las redes sociales que estan acostumbrados a utilizar



PITCH TECNICO

Puntos:
	Idea
	ML
	Feed
		Puntos
		Contenido
	API

----------------------------Contar idea:

Nosotros pensamos en una plataforma que al entrar por primera vez, el usuario se le ofrece la opcion de completar un pequeño cuestionario/"test vocacional", donde tiene que marcar areas de interes y otras cosas y a traves de Machine Learning, obtener una aproximacion de los intereses del mismo.

----------------------------Por que ML?

Este problema, el como determinar un area de interes basada en otras areas de interes, es de los problemas que mejor resuelve ML, en donde hay muchos datos que para un humano aparentan no tener una relacion, pero una computadora puede interpolar conclusiones a partir de eso.

Esto deberia hacerse si o si con un metodo supervisado de entrenamiento, pero el unico factor limitante seria conseguir una cantidad suficiente de datos para alimentar el entrenamiento.
ESCRIBIR COMO SE HARIA

-----------------------------Feed:

Esto sirve para alimentar a nuestro Feed, con una serie de categorias para mostrarle al usuario, si no completa lo anterior, se muestran cosas al azar. El mismo se adapta al usuario, mostrando contenido similar al mas visto.

El Feed muestra contenido generado por los Profesionales, sean videos, posts de texto y videos en vivo donde los usuarios pueden hacer preguntas en tiempo real. Este contenido inicialmente esta parcialmente bloqueado, a partir de nuestro sistema de puntajes

La idea es que mientras mas contenido se consuma o se complete el cuestionario inicial, mas features se desbloquean. De esta forma se motiva al usuario a "investigar" mas para acceder a mejor contenido.

Al momento de tener una carrera elegida, eligen la opcion de "Ya tengo carrera", en donde seleccionan su carrera y se les ofrece una variedad de Mentores en esa area. Al seleccionar alguno de los Mentores, se le envia esta informacion a una plataforma de control para los administradores, JA, para que revisen y aprueben la mentoria.

----------------------------Datos:

Actualmente todos los datos se recuperan con una API hecha en Python con el framework de Flask, donde se hace una request de la forma /feed/career y la misma devuelve un JSON con los datos, y JQuery se encarga de popular el HTML.

Si esto se llevara a una mayor escala, se tendria una base de datos que se comunica con la WebApp, para recuperar los datos de las universidades y carreras, ya que sabemos que cambian constantemente

----------------------------Plus:

Esta plataforma viene con un sistema de monitoreo para los administradores, que en este caso seria Junior Achievement, para que puedan tener datos en tiempo real, sobre el comportamiento de los chicos.

En este caso, las acciones que se realizan, se contabilizan y se envian directamente a la plataforma de control.



