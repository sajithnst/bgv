<template>
  <v-container>
    
    <v-row>
      <v-col>
        <v-card width="99%">
          <v-container class="text-center">
            <h4>&ensp; Current Login: &ensp; &ensp;{{ pdata.login_date }}</h4>

          </v-container>
        </v-card>
      </v-col>
      <v-col>
        <v-card width="97%">
          <v-container class="text-center">
            <h4 v-if="pdata.last_login">&ensp; Last Login: &ensp;&ensp;{{ pdata.last_login }}</h4>

          </v-container>

        </v-card>
      </v-col>
    </v-row>
    <br><br>
    <v-container class="text-center" fluid style="width:30%">
      <v-text-field label="Enter Email Address" v-model="email"></v-text-field>
      <br>
      <v-btn color="indigo darken-4" style="color:white" @click="search()">Search</v-btn><br/><br/>

    </v-container>
    <v-container>

    </v-container>
    <v-container v-if="user_yes" >
      <h2 class="text-center" style="color: darkblue;"> Profiles</h2><br /><br/>

      <v-card
    class="mx-auto pa-2"
    style="width: 80%;"
    >
    <v-list density="compact">
      <v-list-item
      >
        <v-list-item-title v-text="users.name"></v-list-item-title>
        <v-list-item-subtitle v-text="users.email"></v-list-item-subtitle>
        <v-btn icon @click="view(users.email)"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
        <!--<v-btn icon @click="approve(profile.email)"><v-icon color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
        <v-btn icon @click="deny(profile.email)"><v-icon color="error">mdi-account-remove-outline</v-icon></v-btn>-->
      </v-list-item>
    </v-list>
    </v-card>
    </v-container>
    

  </v-container>
</template>

<script>
export default {
  name:"hrsearch",
  async mounted(){
        this.$vuetify.theme.dark=false;
        this.company_mail = this.$storage.getUniversal('hrmail')
        let nurl = "http://127.0.0.1:8000/hr"
        let nres = await this.$axios.get(nurl,{params:{ company_mail :this.company_mail}});
        this.pdata = nres.data
        console.log(this.pdata)
    },
    data:() =>({
        email:"",
        login_date:"",
        last_login:"",
        company_mail:"",
        users:[],
        pdata:{},
        user_yes: false,
        user_no: false
    }),
    methods:{

      async fileselect(event){
        this.file=event
      },
      async search(){
        let url = "http://127.0.0.1:8000/user"
        let user_data =  {params : {'email': this.email}}
        let res = await this.$axios.get(url, user_data)
        this.users = res.data
        console.log(res.data)

        if(res.data = true){
          this.user_yes = true
        }

      },

      async view(email){
        this.$storage.setUniversal('search_email', email)
        this.$router.push('/User_companyprofile')
      },
      async upload(){
        this.company_mail = await this.$storage.getUniversal('hrmail')
        console.log(this.company_mail)
        let formdata= new FormData()
            formdata.append('company_mail',this.company_mail)
            formdata.append('file',this.file)
            let furl = "http://127.0.0.1:8000/hr/uploadcsv"
            let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
      }
    }
  }

</script>

