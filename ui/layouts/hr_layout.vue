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
                color="blue"
                v-on="on"
              >
                <v-icon color="white">mdi-account-circle</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item >

                &emsp;                &emsp;
                <v-list-item-title style="color:black"><h2>Hello {{name}}</h2></v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item @click="profile()">
                <v-divider></v-divider>
                <v-list-item-action>
                  <v-icon color="black">mdi-account</v-icon>
                </v-list-item-action>
                &emsp; &emsp;
                <v-list-item-title style="color:black">HR Profile</v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item @click="user()">
                <v-divider></v-divider>
                <v-list-item-action>
                  <v-icon color="black">mdi-account</v-icon>
                </v-list-item-action>
                &emsp; &emsp;
                <v-list-item-title style="color:black">Search Profiles</v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item @click="logout()">
                <v-divider></v-divider>
                <v-list-item-action>
                  <v-icon color="black">mdi-logout</v-icon>
                </v-list-item-action>
                &emsp; &emsp;
                <v-list-item-title style="color:black">Logout</v-list-item-title>
              </v-list-item>
              <v-divider></v-divider>
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
            this.$router.push("/");
        },
        async logout() {
            this.$router.push("/hrsignin");
            this.$storage.removeUniversal('user_email')

        },
        async user(){
          this.$router.push('/hrpage')
        },
        async profile(){
          this.$router.push('/hr_profile')
        }
    },
}
</script>
