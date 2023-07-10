<template>
    <v-container style="width: 100%; ">
      <v-card>
        <v-card-title>HSE Details</v-card-title>
        <v-card-content>
          <v-container>
            <v-row>
              <v-col style="padding-left: 4%;">
                <h3 class="text-subtitle-1"> Register Number :{{ data.hse_regno}}</h3>
            <h3 class="text-subtitle-1"> Marks : {{ data.hse_marks }}</h3>
            <h3 class="text-subtitle-1"> School : {{ data.hse_school }} </h3>
            <h3 class="text-subtitle-1"> Board : {{ data.hse_board }}</h3>
            <h3 class="text-subtitle-1"> Year of Completion : {{ data.hse_passout }}</h3>
            <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
          <h6 v-if="data.approved_on, verified" class="text-subtitle-3"> Approved on : {{ data.approved_on }}</h6>

              </v-col>
              <v-col >
                <v-container v-if="pending" class="text-center">
                  <v-icon size="150px" color="yellow" ></v-icon>
                </v-container>
                <v-container v-if="verified" class="text-center">
                  <v-icon size="150px" color="green">mdi-check-decagram</v-icon>
                </v-container>
                <v-container v-if="rejected" class="text-center">
                  <v-icon size="150px" color="red">mdi-cancel</v-icon>
                </v-container>



              </v-col>


            </v-row>
          </v-container>
        </v-card-content>
        <v-row>
          <v-container>
            &emsp; &emsp;
            <v-btn text outlined color="indigo darken-4"  @click="doc(data.email, data.hse_regno)">Document</v-btn>

          </v-container>
        </v-row>



      </v-card>


        </v-container>
</template>
<script>
export default{
    name: 'hse',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('search_email')
        let url = "http://127.0.0.1:8000/hse"
        let res = await this.$axios.get(url,{params:{email: this.email}})
        this.data= res.data
        if (this.data.status == false){
          this.pending = true
          this.verified = false
          this.rejected = false
        }
        if(this.data.status == "verified"){
          this.verified = true
          this.pending = false
          this.rejected = false
        }
        if(this.data.status == "rejected"){
          this.rejected = true
          this.pending = false
          this.verified = false
        }


    },
    data: () =>({
        email:"",
        data:{},
        pending: false,
        verified: false,
        rejected: false


    }),
    methods:{
    async doc(email, hse_regno){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          hse_regno: hse_regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)

        let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
      })
      console.log(hse_regno)

    }
   }
}
</script>
