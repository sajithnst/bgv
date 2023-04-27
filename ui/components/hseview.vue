<template>
    <v-container style="width: 100%; ">
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

              </v-col>
              <v-col >
                <v-container v-if="pending" class="text-center">
                  <v-icon color="yellow" size="100px">mdi-timer</v-icon>
                </v-container>
                <v-container v-if="verified" class="text-center">
                  <v-icon color="green" size="100px">mdi-check-decagram</v-icon>

                </v-container>



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
        this.email = this.$storage.getUniversal('user_email')
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
