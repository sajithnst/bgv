<template>
  <main id="app">

      <section class='intro'>
        <div class='introDescription'
          data-aos="zoom-in"
             data-aos-duration="800"
            data-aos-delay='100'>
                <h1> VERIFI EDGE <br> Effortless Background Checks</h1>
          </div>
   
          <img data-aos="zoom-in" class='guide2Image'
          data-aos-duration="800"
          data-aos-delay='100'    src='https://i.ibb.co/xY726vT/verify.png'>
      </section>
      <section class='guide2'>
        <img class='guide2Image' data-aos="slide-right"
        data-aos-duration="800"
       data-aos-delay='100'  src='https://studentidentify.com/img/illustration-1.png'>
          <div class='guide4Description'
          data-aos="slide-up"
             data-aos-duration="800"
            data-aos-delay='100'>
                <h1> A Platform  <br> to store your </h1>
             <div>
              Identity,
               <br>
              
              Educational Qualification, 

              <br>
              and Work Experience,
              <br>
              on a private permissioned blockchain networked named VerifiChain.

       
             </div>
          </div>
          
  
      </section>
  

    <!--<v-row>
        <v-col>
          <v-container class="text-center">
            <h1 class="text-h2 text" style="color: black; margin-top: 25% ;" data-aos="zoom-in"
            data-aos-duration="1500"
            data-aos-delay='500'> VERIFI EDGE</h1><br/><br/>
            <h1 class="text-h4" style="color: black;" data-aos="zoom-in"
            data-aos-duration="1500"
            data-aos-delay='500'> Effortless Background Checks </h1>
          </v-container>

        </v-col>
            &ensp; &ensp; &ensp; &ensp;
            <v-col>
              <v-img data-aos="zoom-in"
              data-aos-duration="1500"
              data-aos-delay='500' 
                :aspect-ratio="4/3" src="https://studentidentify.com/img/illustration-1.png"/>
            </v-col>
    </v-row>-->

      

          <section class='guide3'>
            <div class='guide2Description'
            data-aos="slide-down"
              data-aos-ease = 'ease'
               data-aos-duration="800"
              data-aos-delay='100'>
                  <h1> Plan your  <br> day ahead. </h1>
               <div>
                 If you have one,
                 <br>
                follow the schedule provided by your school.
                <br>
                If you just have a list of things to study, 
                <br>
               break it down into small tasks and 
                <br>
                plan to do the hardest ones 
                <br>
                when you have the most energy.
               </div>
            </div>
              <img class='guide2Image' src='https://res.cloudinary.com/dsderm9xw/image/upload/v1622028057/3D%20Illustrations/3d-illustration1_j06j0a.png' 
              alt='3d illustration of boy with laptop sitting'
              data-aos="slide-up"
               data-aos-duration="800"
              data-aos-ease = 'ease'
              data-aos-delay='100'
              />
          </section>
   

      <section id="download">
        <v-container class="text-center">
          <br>
          <h1 style="text-align: center; color:white;" class="font-bold text-5xl">Who need us?</h1>

          <v-container>
            <v-row align="center" justify="center">
              <v-col cols="10">
                <v-row align="center" justify="center">
                <v-spacer></v-spacer>
                  <v-col class="white--text text-left">
                    
                    <v-row>
            
                        <v-btn rounded outlined  large color="white" class="mt-4" @click="hr()">
                          <v-icon class="mr-2">
                            mdi-office-building-outline
                          </v-icon>
                          Company
                        </v-btn>
                     
                      
                    </v-row>
                    
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col class="white--text text-left">
                    
                    <v-row>
                      <v-btn rounded outlined  large color="white" class="mt-4" @click="notary()">
                        <v-icon class="mr-2">
                          mdi-account
                        </v-icon>
                        Admin
                      </v-btn>
                    </v-row>
                    
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-col class="white--text text-left">
                    <v-row>
                      <v-btn rounded outlined   large color="white" class="mt-4" @click="agencies()">
                        <v-icon class="mr-2">
                          mdi-account
                        </v-icon>
                        Agencies
                      </v-btn>
                    </v-row>
                    
                  </v-col>
                  <v-spacer></v-spacer>
                </v-row>
              </v-col>
            
            </v-row>
          </v-container>
         

        </v-container>
      </section>
      <section class="need">
        <howitworks/>
      </section>
      <br/><br/>
      <partners/>
  </main>
</template>

<script>
import AOS from 'aos';
  import 'aos/dist/aos.css'
export default {
    name: "IndexPage",
    
    async mounted(){
        this.$vuetify.theme.dark=false
        AOS.init()
    },
    data: () => ({}),
    methods: {

      async hr() {
          this.$router.push("/hrsignin");
      },
      async agencies(){
        this.$router.push("/hrsignin");
      },
      async notary(){
        this.$router.push("/notarysignin");
      }
      },

}
</script>
<style>
#download {
  background-image: url("https://i.ibb.co/DYnMj7j/kwjdlk.png");
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  height: 500px;
}

#download .container,
#download .row {
  height: 90%;
}


*{
  margin:0;
  padding:0;
}

.intro{
  display:flex;
  background: whitesmoke;
  justify-content: space-evenly;
  padding-top:80px;
  height: 800px;
}
.need{
    display:flex;
    background: whitesmoke;
    justify-content: space-evenly;
    padding-top:80px;
    height: auto;

}
.introDescription {
  font-size:30px;
  color:#632b2b;
  padding-top:200px;
}
.introDescription p{
  font-size:50px;
  color:#632b2b;
  font-weight: 900;
}

.guide1{
  background: #ffd4a9;
  justify-content: space-evenly;
  padding-top:80px;
  height: 500px;
   overflow:hidden;
}
.guide1Description h1{
  font-size:48px;
  color:#632b2b;
  padding: 120px 0px 20px 0px;
}
.guide1Description div{
  background:#fff3e2 ;
  color:#632b2b;
  font-size:20px;
  padding:10px;
  border-radius:10px;
}


.guide2{
  display:flex;
  background: #fff3e2;
  justify-content: space-evenly;
  height: 800px;
   overflow:hidden;
}

.guide3{
  display:flex;
  background: #afa9a2;
  justify-content: space-evenly;
  height: 800px;
   overflow:hidden;
}

.guide2Description h1{
  font-size:48px;
  color:#632b2b;
  padding: 120px 0px 20px 0px;
}
.guide2Description div{
  color:#632b2b;
  font-size:20px;
  padding:10px;
  border-radius:10px;
}

.guide4Description h1{
  font-size:48px;
  color:#632b2b;
  padding: 120px 0px 20px 0px;
}
.guide4Description div{
  color:#632b2b;
  font-size:20px;
  padding:10px;
  border-radius:10px;
}

footer{
  background: #ffd4a9;
  color:#632b2b;
  padding:10px;
  text-align: right;
  font-weight: 900;
}

/* responsiveness */
@media screen and (max-width: 500px){

  .intro{
  display:block;
  padding-top:10px;
  height:auto;
}
.introImage{
  width:100%;
}
.introDescription {
  padding: 30px 0px 0px 20px;
}

 .guide1{
 display:block;
  padding-top:10px;
  height:auto;
}
.guide1Image{
  width:100%;
}
.guide1Description {
  padding: 20px;
}
.guide1Description h1{
  padding:30px 0px;
}

.guide2{
 display:block;
  height:auto;
}
.guide2Image{
  width:100%;
  overflow:hidden;
}
.guide2Description {
  padding: 20px;
}
.guide2Description h1{
  padding:30px 0px;
}

}

</style>