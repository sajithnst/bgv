<template>
<v-app index >
<v-app-bar app color="white">
    <img class="mr-3" :src="require('../assets/blockedge-logo.svg')" height="40"/>
    <v-spacer></v-spacer>
    <v-btn text @click="signin()"  color="indigo darken-4" width="100px">Sign In</v-btn>
    <v-btn text @click="signup()" color="indigo darken-4"  width="100px" >Sign Up</v-btn>
</v-app-bar>
<v-main>
  <v-container class="text-center">
  </v-container>
  <v-container style="margin-bottom: 10%;">
    <v-sheet elevation="4" color="indigo darken-4">
     <h1 class="verifychain" > VERIFI EDGE</h1>
     </v-sheet>
  </v-container>
  <v-container >
    <h1 class="bgv">Credentials and Authentications  Simplified</h1>
  </v-container>
  <v-container>
    <v-divider class="border-opacity-100" color="indigo darken-6"></v-divider>
  </v-container>
  <v-container >
      <v-container style="padding: 2%;">
        <h3 class="text-center" style="font-size: x-large;" >What is VerifiEdge?</h3>
        <br/>
    <p style="font-size: medium; ">
      A Platform to store your digital profile which is created on 
      blockchain networked named <b>VerifiChain</b>. 
      The platform will verify the <b>Identity</b>, 
      <b>Eductional Qualification</b>, and 
      <b>Work Experience</b>
      of the user on the blockchain network. The genuinity of the documents
      will be recorded permently in the blockchain for future purpose.
    </p>
    <p>
      When any organization or agencies are asked for proof of experience or education the digital profile id
      on VerifiEdge and be provided for verification
    </p>
      </v-container>
      <v-container>
    <v-divider class="border-opacity-100" color="indigo darken-6"></v-divider>
  </v-container>
      <v-container class="text-center" style="padding: 2%;">
        <h3 class="text-center" style="font-size: x-large;"> Who needs us ?</h3><br/>
    <v-row>
        <v-col>
            <v-icon color="indigo darken-2"  >mdi-office-building-outline</v-icon>
            <v-btn text color="indigo darken-2" width="100px" @click="hr()"> Companies </v-btn>
        </v-col>
        <v-col>
            <v-icon color="indigo darken-2">mdi-certificate-outline</v-icon>
            <v-btn text color="indigo darken-2" width="100px" @click="notary()"> Notary </v-btn>
        </v-col>
        <v-col>
            <v-icon color="indigo darken-2"  >mdi-account</v-icon>
            <v-btn text color="indigo darken-2" width="100px" @click="agencies()"> Agencies</v-btn>
        </v-col>
    </v-row>
   </v-container>
  </v-container>
  <v-container>
    <v-divider class="border-opacity-100" color="indigo darken-6"></v-divider>
  </v-container>
  <v-container>
      <h3 class="text-center" style="font-size: x-large; padding: 5%;" >How it works?</h3>
      <v-img :src="require('@/assets/VerifiEdge.png')" style="border: 10px;" height="600px"></v-img>
  </v-container>
  <v-container>
    <v-divider class="border-opacity-100" color="indigo darken-6"></v-divider>
  </v-container>
  <v-container  class="text-center">
    <h3 style="font-size: x-large;"> Who we are ?</h3>
    <v-row dense >
    <v-col>
    <img src="../assets/blockedge-logo.svg" height="80" width="250"/><br/>
    <h4 class="text-center"> Plaform Partner</h4> 
  </v-col>
  <v-col>
    <img src="../assets/SecureKloud_Logo.jpg" height="80" width="250"/><br/>
    <h4 class="text-center">Product Partner</h4> 
  </v-col>
  <v-col>
    
    <img src="../assets/healthcaretriangle.png" height="80" width="250"/><br/>
    <h4 class="text-center"> Service Partner</h4> 
  </v-col>
    </v-row>
    <br/>
  </v-container>
</v-main>
<v-footer dark padless>
  <v-card class="flex" flat tile>
    <v-card-subtitle class="indigo darken-1">
   Copyright : Securekloud
    </v-card-subtitle>
  </v-card>
</v-footer>
</v-app>
</template>

<script>

export default {
    name: "IndexPage",
    async mounted() {
        this.$vuetify.theme.dark = false;
    },
    data: () => ({}),
    methods: {
        async signup() {
            this.$router.push("/signup");
        },
        async signin() {
            this.$router.push("/signin");
        },
        async hr() {
            this.$router.push("/hrsignin");
        },
        async agencies(){
          this.$router.push("/hrsignin");
        },
        async notary(){
          this.$router.push("/notary");
        }
    },

}
</script>
<style>
.button{
  font-family:  Helvetica, Arial, sans-serif;
}
.bgv{
  font-size: 200%;
  margin-bottom: 5%;
  text-align: center;
}
.verifychain{
  font-size: 400%;
  margin-top: 5%;
  color: whitesmoke;
  text-align: center;
}

</style>