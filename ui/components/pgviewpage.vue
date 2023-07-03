<template>
  <v-container style="width: 100%; ">
    <v-container>
      <v-switch
      v-model="pgshow"
      hide-details inset
      label="Not Applicable"
      >

      </v-switch>
    </v-container>
    <v-card v-if="!pgshow">
      <v-card-title>PG Details</v-card-title>
      <v-card-content>
        <v-container v-if="data_s">
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Register Number :{{ data.pg_regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.pg_marks }}</h3>
          <h3 class="text-subtitle-1"> Specialization : {{ data.pg_specialization }}</h3>
          <h3 class="text-subtitle-1"> College : {{ data.pg_college }} </h3>
          <h3 class="text-subtitle-1"> University : {{ data.pg_university }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.pg_passout }}</h3>
          <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
          <h6 v-if="data.edited_on" class="text-subtitle-3"> Edited on : {{ data.edited_on }}</h6>
          <h6 v-if="data.approved_on, verified" class="text-subtitle-3"> Approved on : {{ data.approved_on }}</h6>

            </v-col>
            <v-col >
              <v-container v-if="pending" class="text-center">
                <v-icon size="100px" color="yellow" ></v-icon>
              </v-container>
              <v-container v-if="verified" class="text-center">
                <v-icon size="100px" color="green">mdi-check-decagram</v-icon>

              </v-container>
              <v-container v-if="rejected" class="text-center">
                <v-icon size="100px" color="red">mdi-cancel</v-icon>
                <br>
                <v-btn color="indigo darken-3" style="color: white;" @click="edit()">EDIT</v-btn>

              </v-container>

              <v-container class="text-center">
                <v-card-action>
                  <v-btn color="indigo darken-4" style="color: white;" @click="doc(data.email, data.pg_regno)">Document</v-btn>
                </v-card-action>
              </v-container>


            </v-col>

          </v-row>

        </v-container>

        <br>
      </v-card-content>

      <v-card-action >
        <v-container v-if="data_">
          <v-btn text icon @click="addpg()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>

        </v-container>

      </v-card-action>

    </v-card>

      </v-container>
</template>
<script>
export default{
  name: 'hse',
  async mounted (){
      this.$vuetify.theme.dark =false;
      this.email = this.$storage.getUniversal('login_mail')
      let url = "http://127.0.0.1:8000/pg"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      console.log(this.data)

      if(this.data == false){
        this.data_ = true,
        this.data_s = false
      }
      else{
        this.data_s = true,
        this.data_ = false
      }

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
      data:{

      },
      pending: false,
      verified: false,
      rejected: false,
      data_: false,
      data_s: false,
      pgshow: false

  }),
  methods:{
    async doc(email, pg_regno){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          pg_regno: pg_regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)

        let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
      })
      console.log(pg_regno)

    },
    async addpg(){
      this.$router.push('/pgpage')
    },
    async edit(){
      this.$router.push('/pg_edit')
    }
   }
}
</script>
