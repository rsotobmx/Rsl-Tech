<template>
  
    <div   class="container mt-50">
          <div class="columns">
           <div class="column is-10 is-offset-1">
             
                  <h3 class="title is-3 has-text-centered">Registro de Productos o Servicios </h3> 
                  
                  <hr/>
                                                    <div class="field">
                                                        <label  class="label">Nombre</label>
                                                        <div class="control">
                                                            <input name="nombre" class="input" type="text" placeholder="e.g Alex Smith" v-model="nombre">
                                                        </div>
                                                      </div>


                                                      <div class="field">
                                                          <label class="label">costo</label>
                                                          <div class="control">
                                                              <input name="email" class="input" type="email" placeholder="e.g. alexsmith@gmail.com" v-model="costo">
                                                          </div>
                                                      </div>

                                                      <div class="field">
                                                          <label class="label">En curso</label>
                                                          <div class="control">
                                                              <input name="telefono" class="input" type="text" pattern="(?=.*\d).*" placeholder="+58 4127449249" v-model="curso">
                                                          </div>
                                                      </div>

                                                          <label class="label">Foto del producto</label>
                                                            <div class="control">
                                                                <input class="input is-primary" @change="uploadimage($event)" type="file"  accept="image/*">
                                                            </div>
                                                    <hr>
                                                    
                                                    <button name="enviar" @click.prevent="Saveproduct"  type=submit class="button is-primary is-hoverable"> Guardar producto</button>

                                 <table class="table is-hoverable  is-fullwidth">
                        <thead>
                            <tr>
                            
                            <th scope="col">Imagen</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Costo</th>
                            
                            
                            <th scope="col">eliminar</th>
                            
                            </tr>
                        </thead>
                        <tbody >
                            <tr v-for="producto in productos" :key="producto.id" >
                               
                                <td><img :src="producto.imagen"  class="card-img-top"></td>
                                <td>{{ producto.nombre }}</td>
                                <td>{{ producto.costo}}</td>
                                 
                               
                                
                                <td><button class="button is-danger" @click.prevent="borrar(productos,producto.id)" >Eliminar</button></td>
                               
                            </tr>
                          
                        
                        </tbody>
                    </table>
          
           </div>
           
          </div>
    </div>          

             
</template>
<script>

import '@/firebase/init'
import firebase from 'firebase'
import {storage} from '../firebase/init'
const ref =storage.ref()


export default {
    data(){
        return{
            nombre:'',
            costo:"",
            curso:'',
            error:'',
            productos:[],
            producto: {
                
                nombre:'',
                costo:'',
                
                imagen:'',
                leido: '' 
             },

        }
        

    },
    mounted(){
        this.mostrarPresentacion()
       

    },

    methods:{
        borrar(video,valor){
           var user = firebase.auth().currentUser;
            var db=firebase.firestore();

           console.log(video.length)
             
                
                    video.shift()
                    console.log(valor) 
                    db.collection("usuarios").doc(user.photoURL)
                                    
                                    .update({
                                        
                                    productos: video

                                    }).then(result=>{
                                            console.log("Guardo correctamente")
                                            console.log(result)

                                    })



        },
         mostrarPresentacion(){
            
            var db=firebase.firestore();
            

             db.collection("usuarios").where("productos",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                    
                    
                    this.productos=doc.data().productos
                    console.log(this.productos)
                    
                    
                    //tabla.innerHTML =' <tr> <th scope="row">'+ doc.data().array_id +'</th> <td> <br>'+ doc.data().array_nombrevideo+'</td><br> <td><br>'+ doc.data().array_categoria +'</td><br>  <td><br>'+ doc.data().array_subcategoria +'</td><br> <td><br>'+ doc.data().array_enlace +'</td><br>  </tr'
                    

                    
                });

            });
                


            },
          
        uploadimage(e){
            

            let file= e.target.files[0];
           var storageref= ref.child('portafolio/' + file.name);
            let uploadtask= storageref.put(file);

            uploadtask.on('state_changed', ()=>{
                
                
                }, (error) =>{
                    console.log(error)
                }, () =>{
                
                uploadtask.snapshot.ref.getDownloadURL().then((downloadURL) =>{
                    this.producto.imagen=downloadURL;
                    console.log('File available at', downloadURL);
                 });
                });

        },

         Saveproduct(){
          
            
            var db=firebase.firestore();
                                 
            

          if(this.nombre && this.costo && this.curso ){


                          
                         
                          

                           var aux_mensaje=[]

                        
                          db.collection("usuarios").where("productos",'!=',null)
                            .get()
                            
                            .then((querySnapshot) => {
                                
                            
                                querySnapshot.forEach((doc)=> {
                                    
                                    console.log("entro2")
                                    aux_mensaje=doc.data().productos
                                    console.log(aux_mensaje,"entos es aux")


                                    
                                 console.log("entrooooooooooooo3")
                                this.producto.nombre=this.nombre
                                this.producto.costo=this.costo
                                
                                this.producto.leido="false"
                                
                                aux_mensaje.push(this.producto)
                                    
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
                                    this.costo=''
                                    this.leido=''
                                    
                                    
                                    
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