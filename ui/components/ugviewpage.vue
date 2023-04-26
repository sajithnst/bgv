<template>
  <v-container style="width: 80%; ">
    <v-card>
      <v-card-title>UG Details</v-card-title>
      <v-card-content>
        <v-container>
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Register Number :{{ data.regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.marks }}</h3>
          <h3 class="text-subtitle-1"> Specialization : {{ data.specialization }}</h3>
          <h3 class="text-subtitle-1"> College : {{ data.college }} </h3>
          <h3 class="text-subtitle-1"> University : {{ data.university }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.passout }}</h3>
          <h3 class="text-subtitle-1"> Status : {{ data.status }}</h3>
            </v-col>
            <v-col >
              <v-container v-if="pending">
                <v-icon >mdi-av-timer</v-icon>
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
      let url = "http://127.0.0.1:8000/ug"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      console.log(this.data)
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
      data:{

      },
      pending: false,
      verified: false,


  }),
}
</script>
