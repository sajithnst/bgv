<template>
  <v-container style="width: 100%; ">
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
              <v-container v-if="pending" class="text-center">
                <v-icon size="100px" color="yellow">mdi-timer</v-icon>
              </v-container>
              <v-container v-if="verified" class="text-center">
                <v-icon size="100px" color="green">mdi-check-decagram</v-icon>


              </v-container>
              <v-container class="text-center">
                <v-card-action>
                  <v-btn color="indigo darken-4" style="color: white;" @click="doc(data.email, data.regno)">Document</v-btn>
                </v-card-action>
                <v-container>

                  <v-btn icon @click="approve(profile.email)"><v-icon color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
                <v-btn icon @click="deny(profile.email)"><v-icon color="error">mdi-account-remove-outline</v-icon></v-btn>
                </v-container>
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
        let url = "http://127.0.0.1:8000/ug"
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
        data:{

        },
        pending:false,
        verified: false,


    }),
    methods:{
    async doc(email, regno){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          regno: regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)

        let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
      })
      console.log(regno)

    }
   }
}
</script>
