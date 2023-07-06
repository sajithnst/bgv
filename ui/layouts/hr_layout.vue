<template>
    <v-app hr>

        <v-app-bar app color="indigo darken-3">
          <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>

          <v-spacer></v-spacer>
           <h3 class="white--text">{{ name }}</h3>
           <v-spacer></v-spacer>
           <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn icon

                v-on="on"
              >
                <v-icon color="white">mdi-account-circle</v-icon>
              </v-btn>
            </template>
            <v-list color="indigo darken-3">


          <v-list-item @click="profile()">
            <v-divider></v-divider>
            <v-list-item-action>
              <v-icon color="white">mdi-account</v-icon>
            </v-list-item-action>
            &emsp; &emsp;
            <v-list-item-title style="color:white"> Profile</v-list-item-title>
          </v-list-item>
          <v-list-item @click="upload()">
            <v-divider></v-divider>
            <v-list-item-action>
              <v-icon color="white">mdi-account</v-icon>
            </v-list-item-action>
            &emsp; &emsp;
            <v-list-item-title style="color:white"> Upload</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logout()">
            <v-divider></v-divider>
            <v-list-item-action>
              <v-icon color="white">mdi-logout</v-icon>
            </v-list-item-action>
            &emsp; &emsp;
            <v-list-item-title style="color:white">Logout</v-list-item-title>
          </v-list-item>
        </v-list>
          </v-menu>
        </v-app-bar>
        <v-main>
            <Nuxt/>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name: "hr_layout",

    async mounted() {
        this.$vuetify.theme.dark = false;
        this.company_mail = await this.$storage.getUniversal("hrmail");
        let url = "http://127.0.0.1:8000/hrprofile";
        let hr = {
            "company_mail": this.company_mail,
        };
        let result = await this.$axios.post(url, hr);
        this.name = result.data.name;
    },
    data:()=>{

      return {
        drawer: false,
        company_mail: "",
        name: "",
      };

    },

    methods: {
        async home() {
            this.$router.push("/hrpage");
        },
        async logout() {
            this.$router.push("/hrsignin");
            this.$storage.removeUniversal('user_email')
            let url = "http://127.0.0.1:8000/hr/last_login"
            let ndata={
              company_mail:this.company_mail,
            }
            let nres =  await this.$axios.post(url, ndata)


        },
        async user(){
          this.$router.push('/hrpage')
        },
        async profile(){
          this.$router.push('/hr_profile')
        },
        async upload(){
          this.$router.push('/hr_upload')
        },

    },
}
</script>
