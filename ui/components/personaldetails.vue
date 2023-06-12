<template>


        <v-container style="width: 100%; ">
          <v-card>
            <v-card-title>Personal Details</v-card-title>
            <v-card-content>
              <v-container>
                <v-row>
                  <v-col style="padding-left: 4%;">
                    <h3 class="text-subtitle-1"> Aadhaar Number : {{ pdata.aadhaar }} </h3>
                    <h3 class="text-subtitle-1"> Mobile number : {{ pdata.mob }}</h3>
                    <h3 class="text-subtitle-1"> PAN Number : {{ pdata.pan }}</h3>
                    <h3 class="text-subtitle-1"> Company Name : {{ pdata.company_name }}</h3>
                    <h3 class="text-subtitle-1"> Designation : {{ pdata.designation }}</h3>
                    <h3 class="text-subtitle-1"> Status : {{ pdata.status }}</h3>

                  </v-col>
                  <v-col >
                    <v-container v-if="pending" class="text-center">
                      <v-icon color="yellow" size="100px">mdi-timer</v-icon>
                    </v-container>
                    <v-container v-if="verified" class="text-center">
                      <v-icon color="green" size="100px" >mdi-check-decagram</v-icon>


                    </v-container >
                    <v-container class="text-center">
                      <v-container></v-container>
                      <v-btn icon @click="approve(pdata.email, ndata.name)"><v-icon size="50px" color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
                      <v-btn icon @click="deny(profile.email)"><v-icon size="50px" color="error">mdi-account-remove-outline</v-icon></v-btn>
                    </v-container>
                  </v-col>
                  <v-container>

                  </v-container>

                </v-row>
              </v-container>
            </v-card-content>



          </v-card>

        </v-container>
</template>

<script>
export default{
    name: 'userprofile',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.pdata=res.data

        this.notary = this.$storage.getUniversal('notaryemail')
        let nurl = "http://127.0.0.1:8000/notary"
        let nres = await this.$axios.get(nurl,{params:{email: this.notary}})
        this.ndata = nres.data
        console.log(this.pdata)

    },
    data: () =>({
        email:"",
        pdata :{},
        ndata:{},
        pending: false,
        verified: false,
    }),
    methods:{
      async approve(email, name){
        let url = "http://127.0.0.1:8000/verify/personal"
        let verify={
          user_email: email,
          regno: null,
          notary_email: this.ndata.email,
          notary_name: name
        }
        let res = this.$axios.post(url,verify)
      }
    }
}
</script>
