<template>
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
</template>
<script>
export default {
    name:'whoneedsus',
    data:()=>({

    }),
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