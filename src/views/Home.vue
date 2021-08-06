<template>
  <div >
      
     
      <Header/>
      
        <div id="wrapper" @click.prevent="modal">


            <section id="bloque1">

                
                <h1>Tu aliado para Cumplir tus sueños</h1>
                
        
            </section>

            <section id="bloque2">

                <p>Somos una empresa de diseño de páginas web, estamos ubicados en Valencia, Carabobo. Le ofrecemos todos los servicios necesarios para tener presencia efectiva en internet. Analizamos, le damos forma y vida a su proyecto!</p>

                <p>Que hacemos En RSL TECH, trabajamos para darle vida a sus ideas. 
                    Nuestro equipo de trabajo aportará todo su experiencia para que su proyecto sea un caso de exito</p>

              
          

            </section>


            <section id="bloque3">

                <hr>
                <hr>
                <hr>
              <h2> Nuestros Productos</h2>
              <hr>
              <hr>
              <hr>

              <div class="columns" v-if="imagendesc!=false ">
                  <div class="column " v-for="producto in productos" :key="producto" >


                                <div class="col-m-8" >
                                  <div class="card" >
                                      <div class="card-image">

                                    
                                    <figure class="image is-4by3">
                                      <img :src="producto.imagen"  alt="Imagen producto">
                                    </figure>
                                    </div>
                                    
                                      <div class="container">

                                        <div class="card-body">
                                          <h4 class="card-title" ><strong>{{producto.nombre}}</strong></h4>
                                          <p class="card-text" ><b>Valor: </b>{{producto.costo}}. $</p>
                                          
                                            
                                            
                                          <a @click.prevent="carrito(producto.nombre,producto.costo,producto.imagen)" target="_blank" class="btn btn-primary">añadir al carrito   <i class="fas fa-shopping-cart"></i></a> 
                                          
                                        </div>
                                      </div>
                                  </div>
                                </div>


                           
                      

                   
                      
                  </div>

              </div>

                
                  

            </section>


            <section id="bloque4">
              
                <br>
              <br>
              <br>
              <br>
              <br>
            <article class="tile is-child notification box">
                <p class="title">Características y beneficios</p>
                <p class="subtitle">de nuestras páginas web</p>
                <div class="content">
                    <p>En RSL TECH estamos mejorando cada día, con cada proyecto que desarrollamos mejoramos nuestro standard de calidad, 
                      nuestros proyectos cuentan con:</p>
                      <br>
                      <i class="fa fa-check"></i>
                        Diseño moderno
                      <i class="fa fa-check"></i>
                        Web responsive
                      <i class="fa fa-check"></i>
                        Optimizadas
                      <i class="fa fa-check"></i>
                      Facil de navegar
                </div>
            </article>
              <br>
              <br>
              <br>
              <br>
              <br>








             

                <br>
                <div class="tile is-ancestor">
                  <div class="tile is-vertical is-7">
                    <div class="tile">
                      <div class="tile is-parent is-vertical ">
                        <article class="tile is-child notification box ">
                          <div class="container-fluid"></div>
                          <p class="title has-text-centered">Servicios</p>
                          
                          <div class="content has-text-centered">
                            <p>Servicios Diseño gráfico, 
                              imágen corporativa, logotipos, 
                              redes sociales, hosting y dominios, 
                              redes sociales</p>
                        </div>                          
                        </article>
                      
                      </div>
                      <div class="tile is-parent   " >
                        <article class="tile is-child notification box">
                          
                            
                            <p class="title has-text-centered">Contacto</p>
                           
                            
                            
                            
                            <div class="content has-text-centered">
                              <p>Diseñados para adaptarse a sus necesidades, Promo Web, Web Corporativa, E-commerce, Inmobiliarias</p>
                              


                               <!-- <button id="btnmodal" class="button has-text-white has-background-primary-dark
                                  m-6" @click.prevent="modal2">
                                  <i class="fas fa-envelope-open-text large " >
                                    Contactanos
                                  </i>
                                  
                                </button>
                                 --> 
                            <div class="modal" :class=" {'is-active': toggleModal } ">

                                <div class="modal-background"></div>
                                <div class="modal-card">
                                  
                                    <header class="modal-card-head">
                                      
                                      <p class="modal-card-title"><img src="https://dewey.tailorbrands.com/production/brand_version_mockup_image/208/4822454208_e6c5094a-c93c-4020-ae86-63567f6d6254.png?cb=1615316196" width= "120px" height= "120px"  >
                                      
                                      </p>
                                                                         
                                      <button class="delete" aria-label="close" @click.prevent="modal2"></button>
                                      
                                    </header>

                                    <div class="modal-card-body">
                                        <div class="is-size-6  has-text-info-dark
                                        has-text-centered mr-2 ">
                                          
                                          
                                         
                                                  <p><b>Rellene el formulario a continuación y 
                                                  le contestaremos lo antes posible.</b></p>
                                                  <br>

                                                    <div class="field">
                                                        <label  class="label">Nombre</label>
                                                        <div class="control">
                                                            <input name="nombre" class="input" type="text" placeholder="e.g Alex Smith" v-model="nombre">
                                                        </div>
                                                      </div>


                                                      <div class="field">
                                                          <label class="label">costo</label>
                                                          <div class="control">
                                                              <input name="email" class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="correo">
                                                          </div>
                                                      </div>

                                                      <div class="field">
                                                          <label class="label">En curso</label>
                                                          <div class="control">
                                                              <input name="telefono" class="input" type="text" pattern="(?=.*\d).*" placeholder="+58 4127449249" v-model="telefono">
                                                          </div>
                                                      </div>

                                                          <label class="label">Foto del producto</label>
                                                            <div class="control">
                                                                <input class="input is-primary" @change="uploadimage($event)" type="file"  accept="image/*">
                                                            </div>
                                                        


                                                      

                                                    <br>

                                                  <div class="notification is-danger mt-10" v-if="error">
                      
                                                      {{error}}
                                                  </div>

                                                  <div class="notification is-success mt-10" v-if="enviado">
                      
                                                      {{enviado}}
                                                  </div>
                                                    
                                                    
                                                      
                                                  

                                            

                                          
                                          </div>
                                                    
                                    </div>

                                    <footer class="modal-card-foot">
                                      <button name="enviar" @click.prevent="SaveMessage"  type=submit class="button is-primary is-hoverable"> Enviar Mensaje</button>
                                    
                                    </footer>

                                </div>
                                
                            </div>
                  



                              
                            </div>
                            
                         
                          
                        </article>
                        
                      </div>
                    </div>
                   
                  </div>
                  <div class="tile is-parent  ">
                    <article class="tile is-child notification box ">
                      <div class="content">
                        
                        <p class="title has-text-centered">Objetivos De RSL</p>
                        
                         <div class="content has-text-centered">
                            <p>Convertirse en una de las marcas líderes en el mercado nacional del ramo.
                              Superar el margen anual de ventas estipulado en al menos 50%.
                              Establecer un nicho de consumo internacional en un mercado incipiente.
                              Superar a la competencia en visibilidad y ventas dentro del mercado on-line del ramo nacional e internacional.
                            </p>
                          </div>
                      </div>
                    </article>
                  </div>
                </div>
                      
                      
                    
            </section>


        </div>

        <section  id="portafolio">
          <div class="container">
          <br>
          <br>
          <br>
          <br>
          <h2 class="has-text-centered">Negocios</h2>
         
          <br>
          <br>
          

          <div class="container portafolio">
       
            
              <div class="columns" v-if="imagendesc!=false ">
                  <div class="column " v-for="imagen in imagenes" :key="imagen" >


                                <div class="col-sm-7" >
                                  <div class="card" >

                                    <div class="card-image">

                                    
                                    <figure class="image is-4by3">
                                      <img :src="imagen.id"  alt="Placeholder image">
                                    </figure>
                                    </div>
                                    
                                      <div class="container">

                                        <div class="card-body">
                                          <h4 class="card-title"><strong>{{imagen.nombre}}</strong></h4>
                                          <p class="card-text"><b>Tipo de Negocio: </b>{{imagen.categoria}}.</p>
                                          <p class="card-text"><b>Productos y Servicios: </b>{{imagen.subcategoria}}.</p>
                                            <p class="card-text"><b>Localidad: </b>{{imagen.desarrollo}}.</p>
                                            
                                          <a v-bind:href="imagen.url" target="_blank" class="btn btn-primary">Ver ubicacion  <i class="fas fa-map-marked"></i></a> 
                                          
                                        </div>
                                      </div>
                                  </div>
                                </div>


                           
                      

                   
                      
                  </div>

              </div>




              
              
            </div>
            
          </div>
          
          
        </section>
       

    
       



           
      <div>
        
        <br>
        <Footer/>
      </div>


     

  </div>
</template>

<script>

import footer from './footer'
import header from './header'


import '@/firebase/init'
import firebase from 'firebase'


import {storage} from '../firebase/init'
const ref =storage.ref()


export default {
  

  data(){
    return{
        toggleModal: false,
        pNombre:'',
        Ppresentacion:'',
        showModal: false,
         imagendesc:false,
         imagenes:[],
         productos:[],
        nombre:'',
        telefono:'',
        correo:'',
        Mensaje:'',
        error:'',
        enviado:'',
        
        mensajes:[],
            mensaje: {
                id:'',
                nombre:'',
                telefono:'',
                correo:'',
                mensaje:'',
                leido: '' 
             },


    }
  },
  
  components: {
    'Footer':footer,
    'Header':header,
    
   
  },
   mounted(){
     
         var user = firebase.auth().currentUser;
          //Presentacion Y nombre del Usuario
             var db=firebase.firestore();
            
            
            console.log(user.id)
             db.collection("usuarios").doc("robert")
             .get().then(result =>{
                 
                 this.Ppresentacion=result.data().presentacion
                  this.pNombre=result.data().nombre
                
             })
             

           //Carga de imagenes del portafolio
              db.collection("usuarios").where("negocios",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    this.imagendesc=true
                    this.imagenes=doc.data().negocios
                   
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });

               db.collection("usuarios").where("productos",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    this.imagendesc=true
                    this.productos=doc.data().productos
                   
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });

         


   },
  methods:{
     uploadimage(e){
            

            let file= e.target.files[0];
           var storageref= ref.child('portafolio/' + file.name);
            let uploadtask= storageref.put(file);

            uploadtask.on('state_changed', ()=>{
                
                
                }, (error) =>{
                    console.log(error)
                }, () =>{
                
                uploadtask.snapshot.ref.getDownloadURL().then((downloadURL) =>{
                    this.video.foto=downloadURL;
                    console.log('File available at', downloadURL);
                 });
                });

        },
    
    
   modal2(){
     
            this.toggleModal = !this.toggleModal
        
   },
   
       carrito(Nproduct,Cproduct,Iproduct){
          
            
            var db=firebase.firestore();
                                 
            

          if(Nproduct && Cproduct && Iproduct ){


                          
                         
                          

                           var aux_mensaje=[]

                        
                          db.collection("usuarios").where("mensajes","!=",null)
                            .get()
                            
                            .then((querySnapshot) => {
                                
                            
                                querySnapshot.forEach((doc)=> {
                                    
                                    console.log("entro2")
                                    aux_mensaje=doc.data().mensajes
                                    console.log(aux_mensaje,"entos es aux")


                                    
                                 console.log("entrooooooooooooo3")
                                this.mensaje.nombre=Iproduct
                                this.mensaje.correo=Nproduct
                                this.mensaje.telefono=Cproduct
                                this.mensaje.leido=false
                                this.mensaje.mensaje=""
                                this.mensaje.id=
                                aux_mensaje.push(this.mensaje)
                                    
                            console.log("ya viene el otro db")
                            //aux_video.push(aux_video)
                            
                           
                            
                           // this.videos=aux_video

                            db.collection("usuarios").doc("robert")
                               
                            .update({
                                
                              mensajes: aux_mensaje

                            }).then(result=>{
                                    console.log("Guardo correctamente")
                                    console.log(result)
                                    console.log("entrooooooooooooo4")
                                  
                                    
                            })
                            .catch(error=>{
                                console.log("No se guardo correctamente en la bases de datos")
                                console.log(error)
                                this.error="No se guardo correctamente en la bases de datos"
                            }) 
                                    
                                })

                            })
                            .catch((error)=>{
                                
                                console("error no se guardo",error)
                            })

                           

                          

          }else{
              this.error="todos los campos son obligatorios"
          }
        },

        SaveMessage(){
          
            
            var db=firebase.firestore();
                                 
            

          if(this.nombre && this.telefono && this.correo && this.mensaje){


                          
                         
                          

                           var aux_mensaje=[]

                        
                          db.collection("usuarios").where("productos","!=",null)
                            .get()
                            
                            .then((querySnapshot) => {
                                
                            
                                querySnapshot.forEach((doc)=> {
                                    
                                    console.log("entro2")
                                    aux_mensaje=doc.data().productos
                                    console.log(aux_mensaje,"entos es aux")


                                    
                                 console.log("entrooooooooooooo3")
                                this.mensaje.nombre=this.nombre
                                this.mensaje.costo=this.correo
                                this.mensaje.imagen=this.telefono
                                this.mensaje.leido=false
                                this.mensaje.mensaje=this.Mensaje
                                this.mensaje.id=
                                aux_mensaje.push(this.mensaje)
                                    
                            console.log("ya viene el otro db")
                            //aux_video.push(aux_video)
                            
                           
                            
                           // this.videos=aux_video

                            db.collection("usuarios").doc("robert")
                               
                            .update({
                                
                              productos: aux_mensaje

                            }).then(result=>{
                                    console.log("Guardo correctamente")
                                    console.log(result)
                                    console.log("entrooooooooooooo4")
                                    this.nombre=''                                 
                                    this.Mensaje=''
                                    this.correo=''
                                    this.telefono=''
                                    this.enviado='Enviado al administrador'
                                    
                            })
                            .catch(error=>{
                                console.log("No se guardo correctamente en la bases de datos")
                                console.log(error)
                                this.error="No se guardo correctamente en la bases de datos"
                            }) 
                                    
                                })

                            })
                            .catch((error)=>{
                                
                                console("error no se guardo",error)
                            })

                           

                          

          }else{
              this.error="todos los campos son obligatorios"
          }
        }
   
      
  },
 

  
  
}

</script>
<style>
.card-body{
    width: auto;
    height: auto;
    
}
.card-img-top{
    width: 200px;
    height: 100px;

}
#wrapper {
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.8);
    margin: 0 auto;
    max-width: 1440px;
    width: 100% !important;
}
section {
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-size: cover;
    height: 1100px;
    margin: 0 auto;
    max-width: 1440px;
    overflow: hidden;
    padding: 0;
    position: relative;
    width: 100% !important;
}
#bloque1 {
    background-image: url("https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Teaser/web-development-t.jpg");
}
#bloque2 {
    background-image: url("https://digitalisthub.com/wp-content/uploads/2018/09/disen%CC%83o-web-solomarketing.jpg");
}
#bloque3 {
    background-image: url("https://www.mediaroomsolutions.es/wp-content/uploads/2018/12/desarrollo-y-dise%C3%B1o-web_00-1024x675.jpg");
}
#bloque4 {
    background-image: url("https://www.ingeniovirtual.com/wp-content/uploads/desarrollo-de-aplicaciones-web.png");
}

h1 {
    background-color: #02223a;
    bottom: 0;
    color: rgba(255, 255, 255, 0.9);
    display: block;
    font-size: 5em;
    font-weight: bold;
    margin-top: 3em;
    opacity: 0.76;
    text-align: center;
    text-shadow: 1px 1px 1px #666;
    text-transform: uppercase;
    width: 100%;
}
h2 {
    color: black;
    background: white;
    font-size: 5em;
    font-weight: bold;
    margin-top: 0em;
    opacity: 0.85;
    text-align: center;
    text-shadow: 1px 1px 1px #ccc;
    text-transform: uppercase;
}
h3{
  font-size:2em;
}
#logo {
    display: block;
    margin: 6em auto 0;
    opacity: 0.8;
    width: 200px;
}
#bloque2 p {
    background-color: rgba(255, 255, 255, 0.8);
    color: #333;
    font-size: 1.2em;
    font-weight: normal;
    margin: 7em auto;
    max-width: 800px;
    padding: 1.5em;
}



.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}



 p:hover{
    
    -webkit-transform:scale(1.1);
    transform:scale(1.1);
 }
 .imgRedonda {
    height: 250px;
    width: 250px;
 }
 
 



</style>
