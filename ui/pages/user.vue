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
                      <v-avatar class="profile avatar-center-heigth avatar-shadow" color="grey" size="170">
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
                  <v-row>
                    <Addaddress/>
                  </v-row>
                </v-card>
              </v-container>
             
          </v-col>
          <v-col>

      <persondetailspage/>

      <sslcviewpage/>

      <hseviewpage/>

      <ugviewpage/>

      <pgviewpage/>

      <expviewpage/>

          </v-col>
          <v-col cols="3">

            <v-container fluid>
              <v-card max-width="350px" height="365px" class="mx-auto bg" elevation="2">
                <br>
             
                <v-container class="text-center" >
                  <v-btn size="30%" :loading="isLoading" :disabled="isLoading" color="indigo darken-4"  v-if="show &&!isLoading" @click="submit(data.email)" style="color:white; width:40">Submit Profile</v-btn>

                </v-container>
                <v-container v-if="success" class="text-center">
                  <v-alert type="success" dismissible> You have submitted the profile </v-alert>

                </v-container>
                <v-container v-if="fail" class="text-center">
                  <v-alert type="error" dismissible> Check Whether you have submitted required data </v-alert>

                </v-container>
                

              </v-card>
            </v-container>

        </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    layout:'profile',
    async mounted(){
      this.email = this.$storage.getUniversal('login_mail')
      let url = "http://127.0.0.1:8000/user"
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      console.log(this.data)
      if(this.data.submit_button == false || this.data.status == "pending" || this.data.status == "verified"){
        this.show = false
      }
      else{
        this.show = true
      }


    },
    data: () => ({
      data:{},
      success: false,
      fail: false,
      show: false,
      isLoading: false,
      personal: false,
      sslc: false,
      hse: false,
      ug: false
      
    }),
    methods:{
      async submit(email){
        console.log(email)
        let nurl = "http://127.0.0.1:8000/user/submit"
        let ndata={
          email: email,
        }
        let nres = await this.$axios.post(nurl,ndata)
        this.pdata = nres.data
        if(this.pdata == true){
          this.success = true
          this.fail = false
        }
        else{
          this.success = false
          this.fail = true
        }


        this.isLoading = true;
            // Simulate an asynchronous operation, such as an API call
       


      }
    }

  }
</script>
