<template>
  <v-container style="width: 80%; ">
    <v-card>
      <v-card-title>HSE Details</v-card-title>
      <v-card-content>
        <v-container>
          <v-row>
            <v-col style="padding-left: 4%;">
              <h3 class="text-subtitle-1"> Register Number :{{ data.regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.marks }}</h3>
          <h3 class="text-subtitle-1"> School : {{ data.school }} </h3>
          <h3 class="text-subtitle-1"> Board : {{ data.board }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.passout }}</h3>
          <h3 class="text-subtitle-1"> Status : {{ data.status }}</h3>
            </v-col>
            <v-col >
              <v-container v-if="pending">
                <v-icon x-large>mdi-av-timer</v-icon>
              </v-container>
              <v-container v-if="verified">
                <v-icon x-large>mdi-check-decagram</v-icon>

              </v-container>
              <br>
              <br>
              <v-card-action>
                <v-btn>Document</v-btn>
              </v-card-action>
            </v-col>


          </v-row>
        </v-container>
      </v-card-content>



    </v-card>


      </v-container>
</template>
<script>
export default{
  name: 'hse',
  async mounted (){
      this.$vuetify.theme.dark =false;
      this.email = this.$storage.getUniversal('login_mail')
      let url = "http://127.0.0.1:8000/hse"
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      if (this.data.status == "pending"){
          this.pending = true
          this.verified = false
        }
        if(this.data.status == "verified"){
          this.verified = true
          this.pending = false
        }

  },
  data: () =>({
      email:"",
      data:{},
      pending: false,
      verified: false,


  }),
}
</script>
