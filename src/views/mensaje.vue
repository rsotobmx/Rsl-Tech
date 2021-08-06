<template>
<div   class="container mt-50">
       <div class="columns">
           <div class="column is-10 is-offset-1">
           
                     
                  <h3 class="title is-3 has-text-centered">Carrito <i class="fas fa-shopping-cart"></i></h3> 
                  
                  <hr/>
                  
                    
                  <table class=" table is-hoverable  is-fullwidth">
                        <thead>
                            <tr>
                            
                            <th scope="col">foto</th>
                            <th scope="col">costo</th>
                            <th scope="col">Nombre</th>
                            <th scope="col"></th>
                            <th scope="col">en curso</th>
                            <th scope="col">eliminar</th>
                            
                            </tr>
                        </thead>
                        <tbody >
                          
                            <tr v-for="mensaje in datospaginados" :key="mensaje.id"  >
                               
                                <img :src="mensaje.nombre"  class="card-img-top">
                                <td>{{ mensaje.telefono}}</td>
                                <td>{{ mensaje.correo }}</td>
                                <td>{{ mensaje.mensaje }}</td>
                                <td>{{ mensaje.leido }}</td>
                               
                                <td><button class="button is-danger" @click.prevent="borrar(mensajes,mensaje.id)" >Eliminar</button></td>
                                
                                
                            </tr>
                            
                          
                        
                        </tbody>
                    </table>
               <nav class="pagination is-centered" role="navigation" aria-label="pagination">
 
                    <ul class="pagination-list">
                        <li v-for="pagina in totalpaginas()"  :key="pagina.id" v-on:click="getdatapagina(pagina)"><a class="pagination-link" aria-label="Goto page 1">{{pagina}}</a></li>
                        
                    </ul>
                </nav>
        
                  <div class="notification is-light mt-10" v-if="error">
                    
                    {{error}}
                </div>


                <button class="button is-primary" @click.prevent="leido(mensajes)">Realizar pedido</button>
               

                



                   
           </div>
        </div>

</div>


</template>
<script>
import '@/firebase/init'
import firebase from 'firebase'


export default {
    data(){
        return{
            
           page:1,
           pages:1,
           error:"",
            datospaginados:[],
             mensajes:[],
            mensaje: {
                id:'',
                nombre:'',
                categoria:'',
                subcategoria:'',
                desarrollo:'',
                url: '' 
             },
        }

    },
    mounted(){
         this.getdatapagina(1);
        this.mostrarPresentacion()
        
    },
    methods:{
        
        getdatapagina(nopagina){
            this.datospaginados=[]
            let ini =(nopagina*5) - 5
            let fin = (nopagina * 5 )
            
            this.datospaginados= this.mensajes.slice(ini,fin)
            
        },
        totalpaginas(){
            return Math.ceil( this.pages / 5)
        },
        
        leerdatos(){
           
            var db=firebase.firestore();

             db.collection("usuarios").where("mensajes",'!=',null)
            .onSnapshot((querySnapshot)=> {
                
             
                querySnapshot.forEach((doc)=> {
                   
                    
                    
                    this.total=doc.data().mensajes.length
                    console.log( this.total)
                    this.paginas = Math.ceil((this.total / this.porPagina)) // Redondea hacia arriba
                    

                    
                });

            });

         



        },
       

         mostrarPresentacion(){

             console.log("entro aqui")
             
            //var user = firebase.auth().currentUser;
            var db=firebase.firestore();
            

             db.collection("usuarios")
             
             
             .where("cantM",'>',1)
            
             
            .onSnapshot((querySnapshot)=> {
                
                
             
                querySnapshot.forEach((doc)=> {
                    
                    
                    
                    this.mensajes=doc.data().mensajes
                    
                    this.pages=doc.data().mensajes.length
                    console.log(this.pages,"entro aquii")
                    
                   
                    
                });

            });
                


            },
            leido(array){ 
            
            var db=firebase.firestore();
           
            var aux=array
            
            var n = array.length
            console.log(n)
            this.error="Su pedido fue procesado dentro de pronto nuestro delivery se comunicara con el numero registrado"
              for(let step  =0; step< n ;step++){
                  aux[step].leido="Su pedido fue procesado dentro de pronto nuestro delivery se comunicara con el numero registrado" 
          

            }
        
                    db.collection("usuarios").doc("robert")


                    
                    .update({
                        mensajes: aux
                        
                    })
                    .then(() => {
                        console.log("se guardo correctamente");
                           
                                  

                    })
                    .catch((error) => {
                        // The document probably doesn't exist.
                        console.error("Error : ", error);
                    });

                   


             
           
            
            

            
        },
        deletee(pos){
            console.log(pos)
            var db=firebase.firestore();
            if(confirm('estas seguro ?')){
                db.collection("usuarios").doc("harina pan").delete().then(() => {
                    console.log("Document successfully deleted!");
                }).catch((error) => {
                    console.error("Error removing document: ", error);
                });
            }
            else{
                console.log("holaa")
            }
            
        }
        ,
        borrar(video,valor){
           
            var db=firebase.firestore();

            console.log(video.length)
             
                    video.shift()
                   
                    console.log((valor),"este es el valor") 
                    
                   
                    db.collection("usuarios").doc("robert")
                                    
                                    .update({
                                        
                                    mensajes: video

                                    }).then(result=>{
                                            console.log("Guardo correctamente")
                                            console.log(result)

                                    })



        },
            

    },
    


}

</script>
<style scoped>

.table{
    background: white;
}

</style>