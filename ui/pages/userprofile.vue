<template>
  <v-app >


    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="3">

              <v-container fluid>
                <v-card max-width="450px" class="mx-auto bg" elevation="2">
                  <br><br>
                  <v-row justify="center">
                    <v-col align-self="start" class="d-flex justify-center align-center pa-0" cols="12">
                      <v-avatar class="profile avatar-center-heigth avatar-shadow" color="grey" size="164">

                        <input ref="uploader" class="d-none" type="file" accept="image/*" :change="onFileChanged">
                        <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>


                      </v-avatar>

                    </v-col>
                    <v-btn @click="onButtonClick" class="upload-btn" x-large icon>
                      <v-icon>
                        mdi-camera
                      </v-icon>
                    </v-btn>
                  </v-row>
                  <v-row>
                    <userbannerpage/>
                    <profilepersonal/>
                  </v-row>

                </v-card>
              </v-container>

          </v-col>

          <v-col>



      <persondetails/>

      <sslcview/>

      <hseview/>

      <ugview/>

      <expview/>

          </v-col>
          <v-col cols="3">

            <v-container fluid>
              <v-card max-width="450px" height="380px" class="mx-auto bg" elevation="2">
                <br>
                <v-row justify="center">
                  <v-card-title>QR CODE</v-card-title>
                </v-row>

                <div class="text-center">


                   <v-icon color="black" size="280px">mdi-qrcode</v-icon>


                </div>
                <br>
              </v-card>
            </v-container>

        </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>

</template>
<script>
export default{
    name: 'profile',
    layout:'profile',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.name=res.data.name
    },
    data: () =>({
        name : "Sajith Surendran",
        email:"",
    }),
   methods: {

   }
}
</script>
