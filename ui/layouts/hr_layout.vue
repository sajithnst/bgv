<template>
    <v-app hr>
      <v-navigation-drawer
      color="indigo darkern-4"
      v-model="drawer"
      app

      >
      <v-list>
        <v-list-item >
          <v-divider></v-divider>
          <v-list-item-action>

          </v-list-item-action>
          &emsp;
          <v-list-item-title style="color:white"><h2>Hello {{ name }}</h2></v-list-item-title>
        </v-list-item>
    <br>
        <v-list-item @click="profile()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="white">mdi-account</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:white">HR Profile</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="user()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="white">mdi-magnify</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:white">Search User</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="logout()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="white">mdi-logout</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:white">Logout</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>

      </v-navigation-drawer>
        <v-app-bar app color="indigo darken-3">
          <v-app-bar-nav-icon color="white" variant="text" @click.stop="drawer = !drawer"><v-icon color="white">mdi-account-circle</v-icon></v-app-bar-nav-icon>
          <v-spacer></v-spacer>
           <h3 class="white--text">{{ name }}</h3>
           <v-spacer></v-spacer>
           <v-btn icon @click="logout()" ><v-icon color="white">mdi-logout</v-icon></v-btn>
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
